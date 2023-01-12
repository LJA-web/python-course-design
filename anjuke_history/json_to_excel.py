import json
import pandas as pd


# 将json文件写入到excel中
# 载入json文件
j = json.load(open(r'anjuke_history\history_from_crawler.json', 'r', encoding='utf-8'))

# 将json文件写入到excel中
df = pd.DataFrame(j)
df.to_excel(r'anjuke_history\history_from_crawler.xlsx', index=False)