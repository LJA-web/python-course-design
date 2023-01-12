**2023年1月7日**

* 完成 echarts 所需要的 json 文件，不需要再改动

**2023年1月8日**

* 修改 analysis_draw.py，将文件直接写入到json文件
* 新添 json_to_excel.py 和 excel_to_json.py 文件
* 新添 history_from_crawler.xlsx 表格
* 新添 history_from_crawler(clean).xlsx 表格
* 新添 history_from_crawler(clean).json 文件

**使用方法**

1. 运行 **crawler.py** 爬取北京市2015年到2022年每个月*含有各区房价的链接*，*时间*以及*该时间北京房价的均价*，将信息存放在 **history_average.xlsx** 文件中。（ps：最好手动将表格按照时间列进行排序）
2. 运行 **crawler_region.py** 获取 history_average.xlsx 中的链接和时间，对链接对应网页中的*地区*和*房价*进行爬取，将其存放在字典中，最后写入 **history_from_crawler.json** 文件中，供 **北京市各地区房价变化(2015-2022).html 使用**。
3. 运行 **analysis_draw.py** 对 history_from_crawler.json 文件进行分析，将信息整合成符合 echarts 多需要格式的json文件，写入到 **history_echarts.txt** 文件中，手动格式化。
4. 运行 **json_to_excel.py** 对未经处理的 history_from_crawler.json 转存入 **history_from_crawler.xlsx** 表格中。
5. 运行 **excel_to_json.py** 对人工处理后的 **history_from_crawler(clean).xlsx** 表格再处理，写入到 **history_from_crawler(clean).json** 文件中，供 **北京市各地区房价变化(2015-2022).html 使用。**
