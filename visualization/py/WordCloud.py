import jieba    # 分词器
from PIL import Image    # 图片处理器
import numpy as np    # 矩阵运算
from wordcloud import WordCloud    # 词云
import matplotlib.pyplot as plt
import csv


# 读取数据
with open(r'visualization\dataSource\anjuke.csv', 'r', encoding='utf-8') as f:
    text = ''
    for row in csv.reader(f, skipinitialspace=True):
        text = text + row[0]
    # print(text)  # 打印数据

# 准备分词
cut = jieba.cut(text)
str = ''.join(cut)

# 绘图
img = Image.open(r'visualization\img\img.png')    # 打开图片的遮罩层
img_array = np.array(img)
wc = WordCloud(
    width=1000,
    height=750,  # 设置图片的宽高
    background_color='white',
    mask=img_array,
    font_path='msyhbd.ttc'
).generate_from_text(str)
plt.figure(1)    # 绘制一幅图
plt.imshow(wc)    # 显示图片
plt.axis('off')    # 关闭坐标轴
plt.show()        # 显示图片
# plt.savefig(r'visualization\img\wordcloud.jpg')    # 保存图片
