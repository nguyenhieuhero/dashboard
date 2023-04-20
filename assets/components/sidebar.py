import dash_bootstrap_components as dbc
from dash import Input, Output, State, html

offcanvas = html.Div(className="app-sidebar",
    children=[
        html.P("Dashboard", className="sb-name"),
        html.P("MAIN MENU", className="sb-main-menu"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact",className="nav-box"),
                dbc.NavLink("Page 1", href="/page-1", active="exact",className="nav-box"),
                dbc.NavLink("Page 2", href="/page-2", active="exact",className="nav-box"),
            ],
            vertical=True,
            pills=True,
            className="sb-menu-box"
        ),
    ]
)


