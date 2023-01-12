import openpyxl
import requests
import re
import json


# 读取 excel 文件中的链接信息，返回一个字典，键为链接，时间和均价
def read_excel(filename):
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    data = {}
    for column in sheet.columns:
        data[column[0].value] = [cell.value for cell in column[1:]]
    return data


# 爬取每个月份每个区的信息，返回一个列表，列表中的每个元素为一个列表，包含区名和均价
def analize_link(url):
    all_info = []
    # 模拟浏览器的头部
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        'cookie': 'aQQ_ajkguid=10F11409-85D7-F5F9-8DF2-63E6085E706A; ajk-appVersion=; seo_source_type=1; id58=CrIfoWOnwrwtR+0qeYYaAg==; ctid=14; cmctid=1; wmda_visited_projects=%3B6289197098934; wmda_uuid=09dc92a2d975d280d961bb907da8f084; wmda_new_uuid=1; sessid=2E6F7242-3F42-4339-80C9-406DE68F8355; fzq_h=1c82eae7330be35f2ff97d45c55aa3a1_1672798009960_8dc7b232b74442f4a3411c2a8d1203c9_2029148559; wmda_session_id_6289197098934=1672798013393-1ba4600f-c823-ee1b; obtain_by=2; twe=2; lps=https%3A%2F%2Fbj.zu.anjuke.com%2F%3Ffrom%3DHomePage_TopBar%7Chttps%3A%2F%2Fbeijing.anjuke.com%2F; xxzl_cid=3c9c4d51dd0748df853288f1963d4106; xxzl_deviceid=5q1/DpidANlwOfCzJeIUu5Ip49w+ujVWrTQjWM4rwsf9TFm641cHd1kWBbaAsvcZ'
    }
    # 由于这个网站要不断访问，所以用 requests 模块来进行爬取
    # 如果发现爬取速度不正常，但也没有报错，需要按住 ctrl+单击 链接进行人工验证，再使用爬虫
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print('爬取失败：{}'.format(response.status_code))
        return None
    else:
        print(url, '\t爬取成功')

    block_partten = r'<td class="block-name">(.*?)</td>'
    price_partten = r'<td>(\d+)元/m²</td>'

    block = re.findall(block_partten, response.text, re.S)
    for i in range(len(block)):
        block[i] = re.sub('\n', '', block[i].strip())
    price = re.findall(price_partten, response.text, re.S)

    for i in range(len(block)):
        all_info.append([block[i], price[i]])

    return all_info


# 将爬取的信息存入字典
def info_to_json(info, region_dict, time):
    for i in range(len(info)):
        # 如果字典中没有这个键，就新建一个键
        if info[i][0] not in region_dict.keys():
            region_dict[info[i][0]] = {}
        # 如果字典中有这个键，就在这个键的值中添加一个键值对，键为时间，值为均价
        region_dict[info[i][0]][time] = info[i][1]
    return region_dict


# 将字典转换为 json 文件
def dict_to_json(region_dict):
    with open(r'anjuke_history\history_from_crawler.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(region_dict, ensure_ascii=False, indent=2))
        f.close()


def main():
    region_info = read_excel(r'anjuke_history\history_average.xlsx')
    region_dict = {}
    for i in range(len(region_info['链接'])):
        # 记录爬取的时间
        time = region_info['时间'][i]
        # 爬取每个月份每个区的信息
        all_info = analize_link(region_info['链接'][i])
        # 将爬取的信息存入字典
        info_to_json(all_info, region_dict, time)
    # 将字典转换为 json 文件
    dict_to_json(region_dict)


if __name__ == '__main__':
    main()
