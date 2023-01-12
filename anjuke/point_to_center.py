import pandas as pd


# 读取 anjuke\anjuke(location).xlsx 文件
df = pd.read_excel(r'anjuke\anjuke(location).xlsx', sheet_name='安居客')

# [116.391389, 39.905555] 为北京市中心经纬度，计算每个小区与北京市中心的距离
for i in range(len(df)):
    df['距离(km)'] = (((df['经度'] - 116.391389)*111) ** 2 + ((df['纬度'] - 39.905555)*111) ** 2) ** 0.5

# 保存为 anjuke\anjuke(distance).xlsx 文件
df.to_excel(r'anjuke\anjuke(distance).xlsx', sheet_name='安居客', index=False)