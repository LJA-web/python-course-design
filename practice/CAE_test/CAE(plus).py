import requests
import re
from urllib.request import urlopen


"""
    爬取中国工程院网页上，把每位院士的简介保存为本地文本文件，
    把每位院士的照片保存为本地图片，文本文件和图片文件都以院士的姓名为主文件名。
"""


# 爬取 https://www.cae.cn/cae/html/main/col48/column_48_1.html 内容
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
}
response = requests.get(
    'https://www.cae.cn/cae/html/main/col48/column_48_1.html', headers=headers)

pattern = r'<li class="name_list"><a href="(.*?)" target="_blank">(.*?)</a></li>'
linkAndName = re.findall(pattern, response.text, flags=re.S)
dictionary = {}
for info in linkAndName:
    dictionary[info[1]] = 'https://www.cae.cn' + info[0]

for name, link in dictionary.items():
    info = requests.get(link, headers=headers).text
    img_pattern = r'<img src="/cae/admin/upload/img/(.*?)".*?>'
    intro_pattern = r'<div class="intro">(.*?)</div>'

    img_src = re.findall(img_pattern, info, flags=re.S)[0]
    img_src = 'https://www.cae.cn/cae/admin/upload/img/' + img_src.replace(' ', '%20')
    with open(r'images\\'+name+'.jpg', 'wb') as img_file:
        # 把链接上的图片先读取出来,然后写入本地
        img_file.write(urlopen(img_src).read())
        img_file.close()

    intro = re.findall(intro_pattern, info, flags=re.S)[0]
    intro = re.sub(
        '\n|<p.*?>|</p>|<a.*?>|</a>|<strong>|</strong>|<img.*?>', '', intro.strip())
    with open(r'introductions\\'+name+'.txt', 'w', encoding='utf8') as intro_file:
        intro_file.write(intro)
        intro_file.close()
