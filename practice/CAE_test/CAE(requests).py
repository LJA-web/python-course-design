import requests
import re
from urllib.request import urlopen

# 网站地址
url = 'http://www.cae.cn/cae/html/main/col48/column_48_1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
    }

# 模拟访问,通过requests.get来向网页发出请求并得到返回结果,返回结果respond变量里的text就是html页面
respond = requests.get(url, headers)
respond.encoding = 'utf-8'

# print(respond.text)
# 姓名所在的位置：存在于class = name_list的li标签下的a标签中,通过正则表达式来在网页的源代码中寻找a标签
# 因为网页中的包含姓名的a标签不止一个,因此用一个list来保存网页中包含姓名的a标签
# findall中指定正则表达式作用的对象是respond.text,寻找的内容是上文所说的a标签,\d+表示匹配后方的所有数字
# 通过调试可以发现num_name_list中存放的都是正则表达式\d+匹配到的数字'63775817', '35791989'....
num_name_list = re.findall('<a href="/cae/html/main/colys/(\d+).html" target="_blank">', respond.text)

count = 1

# 1:遍历num_name_list列表,2:模拟点击进入二级页面
for people in num_name_list[:len(num_name_list)]:
    # 将每个院士的姓名的a标签位置对应的正则表达式匹配到的数字和原始链接合成为指定院士对应的a标签链接
    people_url = 'http://www.cae.cn/cae/html/main/colys/{}.html'.format(people)
    # 通过request.get来模拟点击,并且获得请求的respond
    people_respond = requests.get(people_url, headers)
    people_respond.encoding = 'utf-8'

    # 找到简介的位置: class = intro里的p标签里的内容
    # 先找到class = intro 的div标签
    # (.*?)表示匹配任意字符到下一个符合条件的字符
    # 例子：正则表达式a. *?xxx
    # 可以匹配
    # abxxx
    # axxxxx
    # abbbbbxxx

    # re.S的作用的 . 表示可以对指定的字符串做跨行的匹配,如果不用re.S,则只能在people_respond.text中做单行匹配
    text1 = re.findall('<div class="intro">(.*?)</div>', people_respond.text, re.S)
    # 观察html页面可以看到<p>标签中有一些其余的内容&nbsp;&ensp;之类的,需要把这些字符串剔除,并提取出剔除后的内容

    # sub函数中r的作用：应该将r与字符串放在一起。
    # 前缀r是字符串语法的一部分。使用r，Python不会解释引号中的反斜杠序列，如\n、\t等。如果没有r，则必须键入每个反斜杠两次才能将其传递给re.sub。
    # r'\]\n'
    # 以及
    # '\\]\\n'
    # 是两种编写同一字符串的方法。

    # re.sub函数解析:
    # 方法中含有5个参数，下面进行一一说明（加粗的为必须参数）：
    # （1）pattern：该参数表示正则中的模式字符串；
    # （2）repl：该参数表示要替换的字符串（即匹配到pattern后替换为repl），也可以是个函数；
    # （3）string：该参数表示要被处理（查找替换）的原始字符串；
    # （4）count：可选参数，表示是要替换的最大次数，而且必须是非负整数，该参数默认为0，即所有的匹配都会被替换；
    # （5）flags：可选参数，表示编译时用的匹配模式（如忽略大小写、多行模式等），数字形式，默认为0。
    # 使用r,将不会解析\n,\t,<p>|&ensp;|&nbsp;|</p>是要被替换的字符串,''是要替换成的字符串,text[0]是原始字符串,strip()方法去除字符串前面和后面的所有设置的字符串\n \t等等，默认为空格
    text2 = re.sub(r'<p>|&ensp;|&nbsp;|</p>', '', text1[0]).strip()

    # 将简介信息保存在本地文件中,题目意思是要求文件名和人名一致,因此通过正则表达式获取人名,因为返回的是一个list,为了以防获取到多个值,取[0]下标的元素作为file_name
    file_name = re.findall('<div class="right_md_name">(.*?)</div>', people_respond.text)[0]

    # 保存信息
    with open(r'introductions\\'+file_name+'.txt', mode='a+', encoding='utf-8') as file:
        file.write('{}. '.format(count) + text2 + '\n')
        count += 1

    # re.I
    # 使匹配对大小写不敏感
    # re.L
    # 做本地化识别（locale - aware）匹配
    # re.M
    # 多行匹配，影响 ^ 和 $
    # re.S
    # 使.匹配包括换行在内的所有字符
    # re.U
    # 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
    # re.X
    # 获取图片信息xxxxxxxxxxx.jpg
    image = re.findall(
        r'<img src="/cae/admin/upload/img/(.+)" style=', people_respond.text, re.I)
    print(image)
    if image:
        # 图片的http地址
        image_url = r'http://www.cae.cn/cae/admin/upload/img/{0}'.format(
            image[0].replace(' ', r'%20'))
        # 图片名
        image_Name = re.findall(
            '<div class="right_md_name">(.*?)</div>', people_respond.text)[0]
        with open(r'images\\'+image_Name+'.jpg', mode='wb') as imagefile:
            # 把链接上的图片先读取出来,然后写入本地
            imagefile.write(urlopen(image_url).read())
