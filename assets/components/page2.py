from dash import html,dcc
from assets.components.graphs.distribute2 import fig as db2
page2=html.Div(className="app-page",
               children=[
                html.H1("Trực quan dữ liệu",className="p-label"),
                html.Div([
                    html.Div([
                        dcc.Graph(figure=db2,className="fit",id="db2"),
                    ],className="r4")
                    
                ],className="row-wrapper")
               ])