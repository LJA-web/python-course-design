import pandas as pd
import json


# 载入anjuke_history\history_from_crawler(clean).xlsx
df = pd.read_excel(r'anjuke_history\history_from_crawler(clean).xlsx')

# 将 时间 转换为xxxx-xx格式
df['时间'] = df['时间'].map(lambda x: x.replace('年', ''))
df['时间'] = df['时间'].map(lambda x: x.replace('月', ''))



all_info = [["Price", "XX", "XX", "Block", "Month"]]
# 按行遍历df
for row in df.iterrows():
    for i in range(1, len(row[1].index)):
        all_info.append([int(row[1][i]), 0, 0, row[1].index[i], int(row[1][0])])

# 将all_info格式化为json文件
with open('anjuke_history\history_echarts(clean).json', 'w', encoding='utf8') as f:
    json.dump(all_info, f, indent=2, ensure_ascii=False)
    f.close()
