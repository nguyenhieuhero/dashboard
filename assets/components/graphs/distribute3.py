import pandas as pd
import plotly.graph_objects as go
data = pd.read_excel("Sale_project_export\Hoạt động bán hàng All RM Tháng 3 theo tuần.xlsx", sheet_name=None)
df1 = data['Tuần 27.02-05.03']
df2 = data['Tuần 06.03-12.03']
df3 = data['Tuần 13.03-19.03']
df4 = data['Tuần 20.03-26.03']
df5 = data['Tuần 27.03-01.04']

df_list = [df1[df1["Rm name"]=="1.Toàn chi nhánh"], df2[df2["Rm name"]=="1.Toàn chi nhánh"], df3[df3["Rm name"]=="1.Toàn chi nhánh"], df4[df4["Rm name"]=="1.Toàn chi nhánh"], df5[df5["Rm name"]=="1.Toàn chi nhánh"]]

tuan_list = ['Tuần 27.02-05.03', 'Tuần 06.03-12.03', 'Tuần 13.03-19.03', 'Tuần 20.03-26.03', 'Tuần 27.03-01.04']

dsum=[0,0,0]
labels=["Miền Bắc","Miền Trung","Miền Nam"]
for df in df_list:
    dsum[0]+=df.groupby(by="Miền").sum()["Đã phân bổ"].iloc[0]
    dsum[1]+=df.groupby(by="Miền").sum()["Đã phân bổ"].iloc[1]
    dsum[2]+=df.groupby(by="Miền").sum()["Đã phân bổ"].iloc[2]
fig = go.Figure(data=[go.Pie(labels=labels, values=dsum, textinfo='label+percent',
                             insidetextorientation='radial'
                            )])
fig.update_layout(
    title="Sự phân bố khách hàng theo từng vùng miền"
)
fig.show()

