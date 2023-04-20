import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

data = pd.read_excel("Sale_project_export\Hoạt động bán hàng All RM Tháng 3 theo tuần.xlsx", sheet_name=None)
df1 = data['Tuần 27.02-05.03']
df2 = data['Tuần 06.03-12.03']
df3 = data['Tuần 13.03-19.03']
df4 = data['Tuần 20.03-26.03']
df5 = data['Tuần 27.03-01.04']

df_list = [df1, df2, df3, df4, df5]
tuan_list = ['Tuần 27.02-05.03', 'Tuần 06.03-12.03', 'Tuần 13.03-19.03', 'Tuần 20.03-26.03', 'Tuần 27.03-01.04']

fig = make_subplots(rows=1, cols=5, subplot_titles=tuan_list)
flag=True
for i, df in enumerate(df_list):
    phan_khuc = df['Phân khúc'].value_counts()
    sme = df.loc[df['Phân khúc'] == 'SME', 'Miền'].value_counts()
    sse = df.loc[df['Phân khúc'] == 'SSE', 'Miền'].value_counts()
    lc = df.loc[df['Phân khúc'] == 'LC', 'Miền'].value_counts()

    fig.add_trace(go.Bar(x=sse.index, y=sse.values, name='SSE', marker=dict(color='#96D38C'),
                        text=sse.values,legendgroup="g2",showlegend=flag,
                        textposition='outside'), row=1, col=i+1)
    fig.add_trace(go.Bar(x=sme.index, y=sme.values, name='SME', marker=dict(color='#3EB2D8'),
                        text=sme.values,legendgroup="g1",showlegend=flag,
                        textposition='outside'), row=1, col=i+1)
    fig.add_trace(go.Bar(x=lc.index, y=lc.values, name='LC', marker=dict(color='#EB89B5'),
                        text=lc.values,legendgroup="g3",showlegend=flag,
                        textposition='outside'), row=1, col=i+1)
    flag=False
    fig.update_xaxes( ticktext=['Miền Bắc', 'Miền Trung', 'Miền Nam'],
                     tickvals=[1, 2, 3], row=1, col=i+1)
    fig.update_yaxes(range=[0, 250], row=1, col=i+1)
    fig.update_layout(
                      title={
                          'text': 'Biểu đồ phân bố số lượng phân khúc theo từng tuần',
                          'x': 0.5, # căn giữa
                          'font': {'size': 20},
                      },
                  )
    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    })

