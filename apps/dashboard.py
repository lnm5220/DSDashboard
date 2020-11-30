# Import required libraries
import copy
import pathlib
import dash
import math
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_core_components as dcc
import dash_html_components as html
import plotly
import plotly.graph_objects as go
import plotly.express as px
from dash.dash import no_update
import plotly.io as pio
import dash_bootstrap_components as dbc


from app import app
from controls import Sectors, Company_Sizes

# Create controls
sector_options = [
    {"label": str(Sectors[sector]), "value": str(sector)} for sector in Sectors
]

company_size_options = [
    {"label": str(Company_Sizes[size]), "value": str(size)}
    for size in Company_Sizes
]

# get relative data folder
PATH = pathlib.Path(__file__).parent.parent
DATA_PATH = PATH.joinpath("data").resolve()

# Load data
df = pd.read_csv(DATA_PATH.joinpath("data.csv"), low_memory=False)
df["avg_salary"] = df["avg_salary"].apply(pd.to_numeric)
coordinates = pd.read_csv(DATA_PATH.joinpath("coordinates.csv"), low_memory=False)

# Create app layout
layout = html.Div(
    [
    dbc.Row(
            [
                dbc.Col(html.Div(
                    [html.H3("Data Science Job Visualization"),
                    html.P("Explore job data through different applications of Data Visualization.")]
                    )
                )
                ]
        ),
    dbc.Row(
            [
                dbc.Col(html.Div(
                    [html.P("Total No. of Jobs")],
                    id="total_jobs",
                    className="mini_container")),
                dbc.Col(html.Div(
                    [html.P("Average Salary")],
                    id="avgerage_salary",
                    className="mini_container")),
                dbc.Col(html.Div(
                    [html.P("Most Common City")],
                    id="common_city",
                    className="mini_container")),
            ]
        ),
        dbc.Row(
            [dbc.Col(html.Div([
                html.P('Use these controls to customize the data being shown!'),
                html.P("Filter by salary range:",className="control_label"),
                dcc.RangeSlider(
                    id="salary_slider",
                    min=0,
                    max=300000,
                    value=[50000, 75000],
                    marks={0: {'label': '$0'},300000: {'label': '$300,000'}},
                    className="dcc_control"),
                html.Div([dcc.Markdown(id="salaryouput")]),
                html.P("Filter by company size:", className="control_label"),
                dcc.RadioItems(
                    id="size_type_selector",
                    options=[
                            {"label": "All Companies", "value": "all"},
                            {"label": "Small Companies", "value": "small"},
                            {"label": "Large Companies", "value": "large"},
                            {"label": "Customize", "value": "custom"},
                            ],
                    value="all",
                    labelStyle={"display": "inline-block"},
                    className="dcc_control"),
                dcc.Dropdown(
                    id="company_size_selector",
                    options=company_size_options,
                    multi=True,
                    value=list(Company_Sizes.keys()),
                    className="dcc_control"),
                html.P("Filter by sector:", className="control_label"),
                dcc.RadioItems(
                    id="sector_type_selector",
                    options=[
                            {"label": "All ", "value": "all"},
                            {"label": "IT Only", "value": "it"},
                            {"label": "Customize ", "value": "custom"},
                            ],
                    value="it",
                    labelStyle={"display": "inline-block"},
                    className="dcc_control"),
                dcc.Dropdown(
                    id="sector_types",
                    options=sector_options,
                    multi=True,
                    value=list(Sectors.keys()),
                    className="dcc_control")],
                id="cross-filter-options",
                className="pretty_container")),
            dbc.Col(html.Div([
                dcc.Graph(id="count_graph")],
                className="new_container")
            )],no_gutters=True),
        dbc.Row(dbc.Col(
            html.Div([
                dcc.Graph(
                    id="listing-table")],
                className="pretty_bare_container"))),
        dbc.Row(dbc.Col(html.Div([
                    html.H5("Jobs on the Map"),
                    html.P("Use your cursor to move around the map and view jobs by location."),
                    dcc.Graph(id="map_graph")],
                    className="pretty_bare_container",
                ))),
    ]
)


@app.callback(Output("sector_types", "value"), [Input("sector_type_selector", "value")])
def display_type(selector):
    if selector == "all":
        return list(Sectors.keys())
    elif selector == "it":
        return ["Information Technology"]
    return []

@app.callback(Output("company_size_selector", "value"), [Input("size_type_selector", "value")])
def display_type(selector):
    if selector == "large":
        return ["1001 to 5000 employees","5001 to 10000 employees","10000+ employees"]
    elif selector == "small":
        return ["1 to 50 employees","51 to 200 employees","201 to 500 employees","501 to 1000 employees"]
    elif selector == 'all':
        return list(Company_Sizes.keys())
    return []

@app.callback(
    Output('salaryouput', 'children'),
    [Input('salary_slider', 'value')])

def update_output(value):
    start = value[0]
    end = value[1]
    statement = "Range Selected: ${:,.2f} to ${:,.2f}".format(start,end)
    return statement

@app.callback(
    [Output("count_graph", "figure"),
    Output('total_jobs', 'children'),
    Output('avgerage_salary', 'children'),
    Output('common_city', 'children')],
    [Input("salary_slider", "value"),
    Input('company_size_selector','value'),
    Input("sector_types", "value")])

def make_main_figure(salary_range, size_selected, sector_selected):

    dff = df[(df['avg_salary'] >= salary_range[0]) & (df['avg_salary'] <= salary_range[1])]
    dff = dff[dff.Sector.isin(sector_selected)]
    dff = dff.loc[df['Size'].isin(size_selected)]

    if len(dff) == 0:
        string = 'Average Salary:'
        count = ''
        city_max= ''
        return no_update, f"Total No. Jobs: {count}", string, f"Most Common City: {city_max}"

    count = len(dff)
    if len(sector_selected) > 0 and len(size_selected)>0:
        average = dff["avg_salary"].mean()
        city_series = dff['Location'].value_counts()
        city_max = city_series.idxmax()
        string =  "Avg. Salary: ${:,.2f}".format(average)
    else:
        string = 'Average Salary:'
        count = ''
        city_max= ''
        return no_update, f"Total No. Jobs: {count}", string, f"Most Common City: {city_max}"

    fig = px.histogram(dff, x="avg_salary", color="Sector",opacity=.7,color_discrete_sequence=px.colors.cyclical.IceFire)
    fig.update_layout(
    plot_bgcolor='#f9f9f9',
    paper_bgcolor='#f9f9f9',
    showlegend=False,
    title='Distribution of Data Science Jobs', # title of plot
    xaxis_title_text='Average Salary', # xaxis label
    yaxis_title_text='Number of Jobs', # yaxis label
    bargap=0.2, # gap between bars of adjacent location coordinates
    bargroupgap=0.1 # gap between bars of the same location coordinates
    )


    return fig, f"Total No. Jobs: {count}", string, f"Most Common City: {city_max}"

@app.callback(
    Output('listing-table', 'figure'),
    [Input("salary_slider", "value"),
    Input("sector_types", "value"),
    Input('company_size_selector','value')])

def make_table(salary_range, sector_selected, size_selected):
    if len(sector_selected) > 0 and len(size_selected) >0:
        pass
    else:
        return no_update


    dff = df[(df['avg_salary'] >= salary_range[0]) & (df['avg_salary'] <= salary_range[1])]
    dff = dff[dff.Sector.isin(sector_selected)]
    dff = dff.loc[df['Size'].isin(size_selected)]

    if len(dff) == 0:
        return no_update

    figure = go.Figure(data=[go.Table(
        header=dict(
            values=['Job Title','Company Name','Size','Location','Sector','Estimated Salary'],align='left'),
        cells=dict(
            values=[dff['Job Title'], dff['Company Name'],dff['Size'],dff['Location'],dff['Sector'],dff['avg_salary']],
            align='left'))]
    )
    figure.update_layout(template='ggplot2',plot_bgcolor='#f9f9f9',
    paper_bgcolor='#f9f9f9')
    figure.update_layout(
    title={
        'text': "Job Details",
        'xanchor': 'center',
        'yanchor': 'top'})
    figure.update_layout(font=dict(color="#2A3F5F"))

    return figure

@app.callback(
    Output("map_graph", "figure"),
    [Input("salary_slider", "value"),
    Input('company_size_selector','value'),
    Input("sector_types", "value")])

def make_map(salary_range, size_selected, sector_selected):
    if len(sector_selected) > 0 and len(size_selected) >0:
        pass
    else:
        return no_update

    dff = df[(df['avg_salary'] >= salary_range[0]) & (df['avg_salary'] <= salary_range[1])]
    dff = dff[dff.Sector.isin(sector_selected)]
    locations_selected = dff['Location']
    coordinates_for_map = coordinates.loc[coordinates['Location'].isin(locations_selected)]
    #full map has company name, Long, Lat, Location
    full_map = pd.merge(dff, coordinates_for_map, on='Location')


    if len(full_map) == 0:
        return no_update

    fig = px.scatter_mapbox(full_map,lat="lat", lon="lng", hover_name="Company Name", hover_data=["Location", "Size"],
    color='Sector',color_continuous_scale=px.colors.cyclical.IceFire, opacity=.50,zoom=3, height=500).for_each_trace(lambda t: t.update(name=t.name.split("=")[1]))
    fig.update_layout(mapbox_style="carto-positron",plot_bgcolor='#f9f9f9',paper_bgcolor='#f9f9f9')
    fig.update_layout(legend=dict(
    yanchor="top",
    y=0.99,
    xanchor="left",
    x=0.01))
    fig.update_traces(marker=dict(size=10))

    return fig



