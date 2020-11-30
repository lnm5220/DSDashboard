import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H2("Exploring Data Science", className="text-center"), className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.P(children='Welcome to Exploring Data Sciences (created by an actual data science student)! On this web app you will find a dashboard \
              for exploring data science jobs and information about being a data science student in the College of IST at Penn State. Take some time to explore the dashboard\
              and learn about the process of transforming data into an interactive visualization.')
                    , className="mb-4")
            ]),
        dbc.Row([
            dbc.Col(dbc.Card(children=[
              html.H5(children='Explore data science jobs!',className="text-center"),
              dbc.Row([
                dbc.Col([
                  dbc.CardImg(src="/assets/dataimage.jpg"),
                  html.P(""),
                  dbc.Button("Launch the Dashboard", href="/dashboard",color="primary",block=True)
                  ],className="mt-3")],
                justify="center")],
              body=True, color="light", outline=True),
            width=4, className="mb-4"),
            dbc.Col(dbc.Card(children=[
              html.H5(children='Learn about life as a DS Student!',className="text-center"),
              dbc.Row([
                dbc.Col([
                  dbc.CardImg(src="/assets/lionimage.jpg"),
                  html.P(""),
                  dbc.Button("Read more here", href="/aboutme",color="primary",block=True)],
                  className="mt-3")],
                justify="center")],
              body=True, color="light", outline=True),
            width=4, className="mb-4"),
            dbc.Col(dbc.Card(children=[
              html.H5(children='Learn about Applied Data Sciences at IST!',className="text-center"),
              dbc.Row([
                dbc.Col([
                  dbc.CardImg(src="/assets/ist.jpg"),
                  html.P(""),
                  dbc.Button("Learn more", href="https://ist.psu.edu/prospective/undergraduate/academics/data-sciences",color="primary",block=True)],
                  className="mt-3")],
                justify="center")],
              body=True, color="light", outline=True),
            width=4, className="mb-4"),
            ])
        ])
    ])