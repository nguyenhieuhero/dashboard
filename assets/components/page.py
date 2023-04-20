from dash import html,dcc
from assets.components.graphs.test import fig as f1
page1=html.Div(className="app-page1",
               children=[
                html.H1("Truc quan du lieu",className="p1-label"),
                html.Div([
                    html.Div([
                        dcc.Graph(figure=f1,className="r2"),
                    ],className="r3"),
                    
                    html.Div([
                        html.Div([],className="r2"),
                        html.Div([],className="r1"),
                    ],className="r-wrapper")
                ],className="main-page")
               ])