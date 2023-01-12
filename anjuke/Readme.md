**2023年1月9日**

* 新添 anjuke(distance).py 文件

**使用方法（带02都是重新运行程序生成的备份文件）**

1. 运行 **anjuke.py** 爬虫程序生成的 **anjuke.xlsx** 表格。
2. **anjuke copy.xlsx** 是 anjuke.xlsx 的复制文件，目的是让 **location.py** 程序来对其进行操作，插入经度和纬度两类。location.py 的作用就是根据表格中的地址和小区名称来获取经纬度坐标，并写入 **anjuke(location).xlsx** 文件中。
3. 运行 **analysis.py** 程序对经纬度进行了分组，并将分组写入 **anjuke(analysis).xlsx** 表格中，并进行了绘图 **anjuke(analysis).html**
4. 运行 **anjuke(distance).py** 程序，计算各个点到市中心的距离，将信息写入到 **anjuke(distance).xlsx** 表格之中
