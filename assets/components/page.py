from dash import html,dcc
import base64
from assets.components.graphs.distribute import fig
iLC = base64.b64encode(open("assets\image\LC.png", 'rb').read())
iSME = base64.b64encode(open("assets\image\SME.png", 'rb').read())
iSSE = base64.b64encode(open("assets\image\SSE.png", 'rb').read())
page=html.Div(className="app-page",
               children=[
                html.H1("Trực quan dữ liệu",className="p-label"),
                html.Div([
                    html.Div([
                        dcc.Graph(figure=fig,className="fit",id="db"),
                    ],className="r3"),
                    
                    
                    html.Div([
                        html.Img(src='data:image/png;base64,{}'.format(iSSE.decode())),
                        html.Img(src='data:image/png;base64,{}'.format(iSME.decode())),
                        html.Img(src='data:image/png;base64,{}'.format(iLC.decode())),
                    ],className="r-wrapper")
                ],className="main-page")
               ])