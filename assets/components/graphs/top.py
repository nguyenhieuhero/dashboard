import pandas as pd
import plotly.express as px
data = pd.read_excel("Sale_project_export\Hoạt động bán hàng All RM Tháng 3 theo tuần.xlsx",sheet_name=None)
colors=['#636EFA','#EF553B','#00CC96']
def top(day='Tuần 27.02-05.03'):
    df1=data[day].copy()
    df1=df1[df1["Rm name"]=="1.Toàn chi nhánh"]
    df1.dropna(subset=['Đã phân bổ', 'Đã active hạn mức'])
    df1["efficency"]=df1["Đã active hạn mức"]/df1["Đã phân bổ"]
    df1.sort_values(by=["efficency"],ascending=False,inplace=True)
    fig=px.bar(df1[:10],x='Hub',y='efficency')
    fig.update_traces(marker_color=[colors[int(i)-1] for i in df1["Miền"]])
    fig.update_layout(
        title=f"Top các chi nhánh có hiệu suất tốt nhất {day}"
    )
    return fig
