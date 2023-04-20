from dash import html,dcc

page1=html.Div(className="app-page",
               children=[
                html.H1("Trực quan dữ liệu",className="p-label"),
                html.Div([
                    html.Div([
                        dcc.Graph(figure={},className="fit",id="duo"),
                        html.Div([
                            dcc.Dropdown(
                                options=[
                                {'label': 'Miền Bắc', 'value': 1},
                                {'label': 'Miền Trung', 'value': 2},
                                {'label': 'Miền Nam', 'value': 3},
                                ],value=1, className="r4-subbar",id="duo-region"),
                            dcc.Dropdown(
                                ['Tuần 27.02-05.03', 'Tuần 06.03-12.03', 'Tuần 13.03-19.03', 'Tuần 20.03-26.03', 'Tuần 27.03-01.04']
                                ,'Tuần 27.02-05.03', className="r4-subbar",id="time"),
                        ])
                    ],className='r3'),
                    
                    html.Div([
                        html.Div([
                            dcc.Graph(figure={},className="fit",id="fn")
                        ],className="r2"),
                        html.Div([
                            dcc.Graph(figure={},className="fit",id="top")
                        ],className="r15"),
                    ],className="r-wrapper")
                ],className="main-page")
               ])