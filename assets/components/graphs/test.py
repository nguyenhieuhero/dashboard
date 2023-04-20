import plotly.graph_objs as go
import plotly.express as px
import pandas as pd

sheets=['Tuần 27.02-05.03', 'Tuần 06.03-12.03', 'Tuần 13.03-19.03', 'Tuần 20.03-26.03', 'Tuần 27.03-01.04']
xl = pd.ExcelFile('Sale_project_export\Hoạt động bán hàng All RM Tháng 3 theo tuần.xlsx')
labels=["Miền Bắc","Miền Trung","Miền Nam"]
def duo_chart(mien=1,left='Đã phân bổ',right='Đã active hạn mức'):
    total_allocated = []
    call_rate = []
    for sheet in sheets:
        df=xl.parse(sheet)
        filtered_df = df[(df['Miền'] == mien) & (df['Rm name'] == '1.Toàn chi nhánh')]
        sum=filtered_df[left].sum()
        total_allocated.append(sum)
        call_rate.append(filtered_df[right].sum() / sum)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=xl.sheet_names, y=total_allocated, name=f'Số lượng {right.lower()}', marker_color='blue', opacity=0.5))
    fig.add_trace(go.Scatter(x=xl.sheet_names, y=call_rate, name=f'Tỉ lệ {right.lower()}', mode='lines+markers', yaxis='y2', line=dict(color='red')))
    fig.update_layout(title=f'Bảng tổng số lượng {left.lower()} và tỉ lệ {right.lower()} theo sau của {labels[mien-1]}',
                    xaxis_title='Thời gian',
                    )
    fig.update_layout(yaxis=dict(range=[0, 9000], tickmode='linear', tick0=0, dtick=1000, title='Số lượng đã phân bổ'),
                  yaxis2=dict(range=[0, 0.1], tickmode='linear', tick0=0, dtick=0.01, title='Tỉ lệ gọi', overlaying='y', side='right'))
    fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return fig
