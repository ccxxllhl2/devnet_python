########################
### YESLAB 网工Python ###
########################
'''
LAB：此脚本是一个为网络设备信息自动生成EXCEL表格的程序
你需要编写所有带TODO标记处描述的任务，以补完这个脚本
作业部分已经用分割线标记位置了，不在作业区域的代码不建议更改

注意：Pandas最新版本自己不会安装依赖的openpyxl, 在PyCharm的库管理中记得自己安装一下，安装方法与pandas一样
'''

import pandas as pd
from unitTest import *

# -------------------作业区域开始------------------------
# TODO：此脚本所在目录中包含了一个“data/”文件夹用于存放网络数据，将文件夹路径赋值给下面的变量file_path
file_path = "data/"

# TODO：给最后生成的文档编写一个文件名，文件名后缀为.xlsx(EXCEL格式)，并将文件名赋值给下面的变量file_name
file_name = "test_file.xlsx"

# TODO：为下面的ip_list与on_time_list两个列表写入内容
## ip_list里面填入三台设备的IP地址（字符串）
## on_time_list填入三台设备的运行时间（整数）
ip_list = ["192.168.1.1", "192.168.100.1", "172.17.11.32"]
on_time_list = [1567, 316, 971]
# -------------------作业区域结束------------------------

device_name_list = ["生产核心",
                    "防火墙网关",
                    "DMZ核心"]
title_list = ["设备名称", "设备IP", "运行时间（分钟）"]


def create_file():
    data = pd.DataFrame({title_list[0]: device_name_list,
                         title_list[1]: ip_list,
                         title_list[2]: on_time_list},
                         columns=title_list)
    data.to_excel(file_path + file_name)


if __name__ == "__main__":
    is_dir_exist(file_path)
    check_file_name(file_name)
    check_data(device_name_list, ip_list, on_time_list, title_list)
    has_error = output_error()
    if not has_error:
        create_file()
        print("文档 {} 已生成".format(file_path + file_name))