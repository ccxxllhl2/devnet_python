########################
### YESLAB 网工Python ###
########################

import unitTest
import random

# 此脚本需要完成以下任务：
# 编写两个函数：
# 第一个函数模拟网络接口信息，随机产生发包量与收包量
# 第二个函数模拟对接口状态进行查询的过程，了解目前网络接口的发包量与收包量
# 但是程序中存在错误导致不能执行，参照实验手册中执行成功的截图，对程序进行排错
# -------------------作业区域开始------------------------
# TODO: 修正下面代码中的错误


def interface_work():
    RCV_PKG = random.randint(0, 10000)
    SED_PKG = random.randint(0, 10000)
    return RCV_PKG, SED_PKG


def show_interface_status(DATAS):
    print("目前接口收包量为：{}".format(DATAS[0]))
    print("目前接口发包量为：{}".format(DATAS[1]))


net_datas = interface_work()
show_interface_status(net_datas)
# -------------------作业区域结束------------------------


if __name__ == "__main__":
    unitTest.output_error()