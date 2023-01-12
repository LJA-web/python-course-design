import pandas as pd
import json
import matplotlib.pyplot as plt


# 载入history.json数据
df = pd.read_json(r'anjuke_history\history_from_crawler.json')

# 将index转换为xxxx-xx格式
df.index = df.index.map(lambda x: x.replace('年', ''))
df.index = df.index.map(lambda x: x.replace('月', ''))

all_info = [["Price", "XX", "XX", "Block", "Month"]]
# 按行遍历df
for index, row in df.iterrows():
    for block in row.index:
        # 将nan替换为0，将.0替换为空，再将字符串转化为int
        if pd.isnull(row[block]):
            row[block] = 0
        row[block] = str(row[block]).replace('.0', '')
        row[block] = int(row[block])

        all_info.append([row[block], 0, 0, block, int(index)])

print(all_info)
# 将all_info写入txt文件
with open('anjuke_history\history_echarts.json', 'w', encoding='utf8') as f:
    json.dump(all_info, f, indent=2, ensure_ascii=False)
    f.close()
    # f.write(str(all_info))
    # f.close()


# # 根据df绘制折线图
# plt.figure(figsize=(20, 8), dpi=80)
# plt.plot(df.index, df['西城'])
# plt.plot(df.index, df['朝阳'])
# plt.plot(df.index, df['海淀'])
# plt.plot(df.index, df['丰台'])
# plt.plot(df.index, df['石景山'])
# plt.plot(df.index, df['通州'])
# plt.plot(df.index, df['顺义'])
# plt.plot(df.index, df['昌平'])
# plt.plot(df.index, df['大兴'])
# plt.plot(df.index, df['房山'])
# plt.plot(df.index, df['门头沟'])
# plt.plot(df.index, df['平谷'])
# plt.plot(df.index, df['怀柔'])
# plt.plot(df.index, df['密云'])
# plt.plot(df.index, df['延庆'])
# plt.plot(df.index, df['东城'])
# # 横坐标倾斜，仅显示年份
# plt.xticks(range(0, len(df.index), 12), df.index[::12], rotation=45)

# # 增加图例
# plt.legend(['西城', '朝阳', '海淀', '丰台', '石景山', '通州', '顺义', '昌平', '大兴', '房山', '门头沟', '平谷', '怀柔', '密云', '延庆', '东城'], loc='upper left')
# # 设置字体族
# plt.rcParams['font.sans-serif'] = ['SimHei']

# plt.xlabel('date')
# plt.ylabel('price')
# plt.title('Anjuke history price')
# plt.show()
