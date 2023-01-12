import webbrowser
import folium
from folium.plugins import HeatMap
import pandas as pd


def read_excel(filename):
    # 读取excel
    df = pd.read_excel(filename)
    return df


# 读取excel
df = read_excel(r'anjuke\anjuke(location)02.xlsx')

# 获取第四列和第五列
lon_lat = df.iloc[:, [3, 4]]

# 经纬度保留到小数点后四位
# lon_lat['经度'] = lon_lat['经度'].apply(lambda x: round(x, 4))
# lon_lat['纬度'] = lon_lat['纬度'].apply(lambda x: round(x, 4))

# 计算重复值
tabel = lon_lat.groupby(['经度', '纬度']).size().reset_index(name='counts')
print(tabel)

# 保存为excel文件
tabel.to_excel(r'anjuke\anjuke(analysis)02.xlsx', index=False)

# 北京市在东经115.7°—117.4°，北纬39.4°—41.6°之间
# 北京市中心位于北纬39°54′20″，东经116°25′29″ (116.41348,39.91135)
# 筛选在范围内的数据
tabel = tabel[(tabel['经度'] > 115.7) & (tabel['经度'] < 117.4)
              & (tabel['纬度'] > 39.4) & (tabel['纬度'] < 41.6)]

lon = tabel['经度'].tolist()  # 经度 longitude
lat = tabel['纬度'].tolist()  # 纬度 latitude
counts = tabel['counts'].tolist()
lon_lat = list(zip(lon, lat, counts))


LOC = []
# 此处必须使用zip构成元组
for lng, lat, num in zip(lon, lat, counts):
    LOC.append([lat, lng, num])

center = [39.91135, 116.41348]
m = folium.Map(location=center, zoom_start=8.5)
HeatMap(LOC).add_to(m)

# 保存格式为html文件
# 完成之后，要自己去看一下，把 </body> 的 script 标签里面的内容挪到 </body> 之前
name = r'anjuke\anjuke(analysis)02.html'
m.save(name, encoding='utf-8')

# 将结果文件打开进行显示
webbrowser.open(name, new=2)
