import requests
import re
from urllib.request import urlopen


"""
    爬取中国工程院网页上，把每位院士的简介保存为本地文本文件，
    把每位院士的照片保存为本地图片，文本文件和图片文件都以院士的姓名为主文件名。
"""

# 模拟浏览器的头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
}
# 爬取 https://www.cae.cn/cae/html/main/col48/column_48_1.html 内容
# 由于这个网站要不断访问，所以用 requests 模块来进行爬取
response = requests.get(
    'https://www.cae.cn/cae/html/main/col48/column_48_1.html', headers=headers)

# 正则表达式匹配 介绍链接 和 姓名，以字典 姓名:链接 的形式存储
pattern = r'<li class="name_list"><a href="(.*?)" target="_blank">(.*?)</a></li>'
linkAndName = re.findall(pattern, response.text, flags=re.S)
dictionary = {}
for info in linkAndName:
    dictionary[info[1]] = 'https://www.cae.cn' + info[0]

for name, link in dictionary.items():
    # 爬取 介绍链接 内容
    info = requests.get(link, headers=headers).text
    # 正则表达式匹配 图片链接 和 简介
    img_pattern = r'<img src="/cae/admin/upload/img/(.*?)".*?>'
    intro_pattern = r'<div class="intro">(.*?)</div>'

    # 获取图片并存储到本地
    img_src = re.findall(img_pattern, info, flags=re.S)[0]
    # 有的院士正则表达式匹配部分存在空格，需要特别注意
    img_src = 'https://www.cae.cn/cae/admin/upload/img/' + img_src.replace(' ', '%20')
    with open(r'images\\'+name+'.jpg', 'wb') as img_file:
        # 把链接上的图片先读取出来,然后写入本地
        img_file.write(urlopen(img_src).read())
        img_file.close()

    # 获取简介的 html 代码段，再通过 re.sub() 进行筛检多余部分
    intro = re.findall(intro_pattern, info, flags=re.S)[0]
    intro = re.sub('\n|<p.*?>|</p>|<a.*?>|</a>|<strong>|</strong>|<img.*?>|&nbsp;|&ensp;', '', intro.strip())
    with open(r'introductions\\'+name+'.txt', 'w', encoding='utf8') as intro_file:
        intro_file.write(intro)
        intro_file.close()