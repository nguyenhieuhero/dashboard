import dash_bootstrap_components as dbc
from dash import Dash, html, Input, Output, State,dcc
from assets.components.sidebar import offcanvas
from assets.components.page import page
from assets.components.page1 import page1
from assets.components.page2 import page2
from assets.components.page3 import page as page3
from assets.components.graphs.test import duo_chart
from assets.components.graphs.funnel import funnel
from assets.components.graphs.top import top


app = Dash(__name__,suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id="url"),
    offcanvas,
    html.Div(id="page-content",style={"width":"85%","height":"100wh"})
    ],style={'display':'flex',
                 'height':'100vh',
                 'width':'100vw',
                 'padding':'0px'})

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return page2
    elif pathname == "/page-1":
        return page
    elif pathname == "/page-2":
        return page1
    elif pathname == "/page-3":
        return page3
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )
@app.callback(
    [Output('duo', 'figure'),Output('fn', 'figure'),Output('top', 'figure')],
    [Input('duo-region', 'value'),Input('time', 'value')]
)
def update(num,time):
    return duo_chart(mien=num),funnel(day=time),top(day=time)
if __name__ == '__main__':
    app.run_server(debug=True)