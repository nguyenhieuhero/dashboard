import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, State,dcc
from assets.components.sidebar import offcanvas
from assets.components.page import page1


app = Dash(__name__)

app.layout = html.Div([
    dcc.Location(id="url"),
    offcanvas,
    html.Div(id="page-content",style={"width":"85%","height":"100wh",'backgroundColor':'green'})
    ],style={'display':'flex',
                 'height':'100vh',
                 'width':'100vw',
                 'backgroundColor':'cyan',
                 'padding':'0px'})

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return page1
    elif pathname == "/page-1":
        return page1
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )
if __name__ == '__main__':
    app.run_server(debug=True)