from dash import html,dcc
from assets.components.graphs.distribute4 import fig as db4
page=html.Div(className="app-page",
               children=[
                html.H1("Trực quan dữ liệu",className="p-label"),
                html.Div([
                    dcc.Graph(figure=db4,className="r4",style={"width":"96%"}),
                ],className="main-page")
               ])