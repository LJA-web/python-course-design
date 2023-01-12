import pandas as pd
import json


# 读取excel文件
df = pd.read_excel(r'ZhangHang\DataSource\excelToJson.xlsx')

data_scatter = []
for i in range(len(df)):
    data_scatter.append({'name': df['小区'][i], 'value': int(df['月租'][i])})
with open(r'ZhangHang\json\data_scatter.json', 'w', encoding='utf8') as f:
    json.dump(data_scatter, f, ensure_ascii=False)

geoCoordMap = {}
for i in range(len(df)):
    geoCoordMap[df['小区'][i]] = [df['经度'][i], df['纬度'][i]]
with open(r'ZhangHang\json\geoCoordMap.json', 'w', encoding='utf8') as f:
    json.dump(geoCoordMap, f, ensure_ascii=False)
