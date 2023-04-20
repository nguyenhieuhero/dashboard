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
    df2=df.groupby(by="Phân khúc")["Đã active hạn mức"].sum()
    # print(df2)
    fig.add_trace(go.Bar(x=df2.index, y=df2.values, name='SME', marker=dict(color=['#EB89B5','#3EB2D8','#96D38C']),
                        text=df2.values,legendgroup="g1",showlegend=False,
                        textposition='outside'), row=1, col=i+1)
    fig.update_layout(
                      title={
                          'text': 'Số lượng tín dụng đã active hạn mức theo phân khúc',
                          'x': 0.5, # căn giữa
                          'font': {'size': 20},
                      },
                  )
    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    fig.update_yaxes(range=[0, 80], row=1, col=i+1,title="Tổng số tín dụng đã được active",visible=flag)
    flag=False
    fig.update_xaxes(categoryorder='array', categoryarray= ["SSE","SME","LC"])

