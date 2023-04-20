from cv2 import applyColorMap
from dash import html
import base64
region = ['LC', 'a', 'c']
iVN = base64.b64encode(open("assets\image\VN.png", 'rb').read())
iLC = base64.b64encode(open("assets\image\LC.png", 'rb').read())
iSME = base64.b64encode(open("assets\image\SME.png", 'rb').read())
iSSE = base64.b64encode(open("assets\image\SSE.png", 'rb').read())

page1=html.Div(className=".app-page1",
               children=[
                    html.H3("Data Overview",className="h1", style= {"margin-bottom": "0px", 'color' : 'black'}),
                    html.H5('Tháng 4', style = {"margin-top": "0px", 'color' : 'black'}),
                    
                    html.H4("HUB", className="h4"),
                    html.Img(src='data:image/png;base64,{}'.format(iVN.decode()),style={'width':"90vh"}),
                    
                    html.H4("Phân khúc", className = "h4"),
                    html.Div(className = "three", 
                             children = [
                                 html.Img(src='data:image/png;base64,{}'.format(iLC.decode()),style={'width':"50vh"}),
                                 html.Img(src='data:image/png;base64,{}'.format(iSME.decode()),style={'width':"50vh"}),
                                 html.Img(src='data:image/png;base64,{}'.format(iSSE.decode()),style={'width':"50vh"}),
                             ])       

                ]
               )