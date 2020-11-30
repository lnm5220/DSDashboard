import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
# import all pages in the app
from apps import dashboard, home, aboutme

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("Home")),
                    ],
                justify="end"),
                href="/home",
            ),
            html.A(
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("About Me")),
                    ],
                justify="around"),
                href="/aboutme",
            ),html.A(
                dbc.Row(
                    [
                        dbc.Col(dbc.NavbarBrand("Dashboard"))
                    ],
                justify="end"),
                href="/dashboard",
            )
        ]
    ),
    color="dark",
    dark=True,
)

nav = dbc.Container([
    dbc.Nav([
        dbc.NavLink("Home", href="/home"),
        dbc.NavLink("About Me", href="/aboutme"),
        dbc.NavLink("Dashboard", href="/dashboard")],
        justified=True,
        horizontal='center',
        pills=True),    
    ])

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard.layout
    elif pathname == '/aboutme':
        return aboutme.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)