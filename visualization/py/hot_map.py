import pandas as pd
import json


# 房源热力图分布
def distribution():
    # 载入visualization\json\beijing_heatmap.json
    with open(r'visualization\json\beijing_heatmap.json', 'r', encoding='utf-8') as f:
        j = json.load(f)
        # 修正j中的result中的data中的bound
        j['result']['data'][0]['bound'] = []
        
    # 载入visualization\dataSource\anjuke(analysis).xlsx
    df = pd.read_excel(r'visualization\dataSource\anjuke(analysis).xlsx')
    # 将每一行数据转换为list
    data = df.values.tolist()
    # 将列表中每一个数据转换为str
    data = [[str(i) for i in j] for j in data]


    j['result']['data'][0]['bound'] = data

    # 将j转换为json格式
    j = json.dumps(j)
    # 将j写回visualization\json\beijing_heatmap.json
    with open(r'visualization\json\beijing_heatmap.json', 'w', encoding='utf-8') as f:
        f.write(j)
        f.close()


# 价格分布热力图
def price():
    with open(r'visualization\json\beijing_heatmap.json', 'r', encoding='utf-8') as f:
        j = json.load(f)
        # 修正j中的result中的data中的bound
        j['result']['data'][0]['bound'] = []
        
    # 载入visualization\dataSource\anjuke(analysis).xlsx
    df = pd.read_excel(r'visualization\dataSource\anjuke(location).xlsx')
    df = df[['经度', '纬度', '月租']]
    # 将每一行数据转换为list
    data = df.values.tolist()
    # 将列表中每一个数据转换为str
    data = [[str(i) for i in j] for j in data]


    j['result']['data'][0]['bound'] = data

    # 将j转换为json格式
    j = json.dumps(j)
    # 将j写回visualization\json\beijing_heatmap.json
    with open(r'visualization\json\beijing_heatmap(price).json', 'w', encoding='utf-8') as f:
        f.write(j)
        f.close()


price()