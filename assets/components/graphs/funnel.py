import pandas as pd
import plotly.graph_objects as go
data = pd.read_excel("Sale_project_export\Hoạt động bán hàng All RM Tháng 3 theo tuần.xlsx", sheet_name=None)
df1 = data['Tuần 27.02-05.03']
df2 = data['Tuần 06.03-12.03']
df3 = data['Tuần 13.03-19.03']
df4 = data['Tuần 20.03-26.03']
df5 = data['Tuần 27.03-01.04']

df_list = [df1[df1["Rm name"]=="1.Toàn chi nhánh"], df2[df2["Rm name"]=="1.Toàn chi nhánh"], df3[df3["Rm name"]=="1.Toàn chi nhánh"], df4[df4["Rm name"]=="1.Toàn chi nhánh"], df5[df5["Rm name"]=="1.Toàn chi nhánh"]]


# print(df1[['Đã phân bổ',
#        'Đã gọi', 'Đã gặp', 'Thu thập hồ sơ', 'Định giá', 'Đã trình',
#        'Đã phê duyệt', 'Đã active hạn mức']])
# print(df1[df1["Miền"]==1][['Đã phân bổ',
#        'Đã gọi', 'Đã gặp', 'Thu thập hồ sơ', 'Định giá', 'Đã trình',
#        'Đã phê duyệt', 'Đã active hạn mức']].sum())


def funnel(day="Tuần 27.02-05.03"):
    fig = go.Figure()
    df=data[day].copy()
    df=df[df["Rm name"]=="1.Toàn chi nhánh"]
    fig.add_trace(go.Funnel(
        name = 'Miền Bắc',
        y = ['Đã phân bổ',
        'Đã gọi', 'Đã gặp', 'Thu thập hồ sơ', 'Định giá', 'Đã trình',
        'Đã phê duyệt', 'Đã active hạn mức'],
        x = df[df["Miền"]==1][['Đã phân bổ',
        'Đã gọi', 'Đã gặp', 'Thu thập hồ sơ', 'Định giá', 'Đã trình',
        'Đã phê duyệt', 'Đã active hạn mức']].sum(),
        textinfo = "value+percent initial"))

    fig.add_trace(go.Funnel(
        name = 'Miền Trung',
        y = ['Đã phân bổ',
        'Đã gọi', 'Đã gặp', 'Thu thập hồ sơ', 'Định giá', 'Đã trình',
        'Đã phê duyệt', 'Đã active hạn mức'],
        x = df[df["Miền"]==2][['Đã phân bổ',
        'Đã gọi', 'Đã gặp', 'Thu thập hồ sơ', 'Định giá', 'Đã trình',
        'Đã phê duyệt', 'Đã active hạn mức']].sum(),
        textinfo = "value+percent initial"))

    fig.add_trace(go.Funnel(
        name = 'Miền Nam',
        y = ['Đã phân bổ',
        'Đã gọi', 'Đã gặp', 'Thu thập hồ sơ', 'Định giá', 'Đã trình',
        'Đã phê duyệt', 'Đã active hạn mức'],
        x = df[df["Miền"]==3][['Đã phân bổ',
        'Đã gọi', 'Đã gặp', 'Thu thập hồ sơ', 'Định giá', 'Đã trình',
        'Đã phê duyệt', 'Đã active hạn mức']].sum(),
        textinfo = "value+percent initial"))
    fig.update_layout(
        title=f"Biểu đồ phễu {day}"
    )
    return fig