import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

sheets=['Tuần 27.02-05.03', 'Tuần 06.03-12.03', 'Tuần 13.03-19.03', 'Tuần 20.03-26.03', 'Tuần 27.03-01.04']
xl = pd.ExcelFile('Sale_project_export\Hoạt động bán hàng All RM Tháng 3 theo tuần.xlsx')
total_allocated = []
call_rate = []
for sheet in sheets:
    df=xl.parse(sheet)
    filtered_df = df[(df['Miền'] == 1) & (df[' Rm name'] == '1.Toàn chi nhánh')]
    sum=filtered_df['Đã phân bổ'].sum()
    total_allocated.append(sum)
    call_rate.append(filtered_df['Đã gọi'].sum() / sum)

fig = go.Figure()
fig.add_trace(go.Bar(x=xl.sheet_names, y=total_allocated, name='Số lượng đã phân bổ', marker_color='blue', opacity=0.5))
fig.add_trace(go.Scatter(x=xl.sheet_names, y=call_rate, name='Tỉ lệ gọi', mode='lines+markers', yaxis='y2', line=dict(color='red')))
fig.update_layout(title='Bảng tổng số lượng đã phân bổ và tỉ lệ gọi của Miền Bắc')
fig.update_layout(title='Bảng tổng số lượng đã phân bổ và tỉ lệ gọi của Miền Bắc',
                xaxis_title='Thời gian',
                )
fig.update_layout(yaxis=dict(range=[0, 9000], tickmode='linear', tick0=0, dtick=1000, title='Số lượng đã phân bổ'),
                  yaxis2=dict(range=[0, 1], tickmode='linear', tick0=0, dtick=0.2, title='Tỉ lệ gọi', overlaying='y', side='right'))
fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
})
# fig.show()
