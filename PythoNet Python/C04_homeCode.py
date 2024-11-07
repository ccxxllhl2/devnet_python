########################
### YESLAB 网工Python ###
########################

import re
import unitTest

with open("data/interfaceLOG.log") as file:
    ifDatas = file.readlines()

# 按照实验手册内容，编写下面的两个正则表达式
# -------------------作业区域开始------------------------
Pattern1 = r"  "
Pattern2 = r"  "


def port_and_mac(pattern1, pattern2):
    if_info = {}
    for data in ifDatas:
        if_status = re.search(pattern1, data)
        if if_status is not None:
            if_name = if_status.group()
        if_mac = re.search(pattern2, data)
        if if_mac is not None:
            mac_address = if_mac.group()
            if ('UP' in if_name) and ('GigabitEthernet' in if_name):
                if_info[if_name.split(" ")[1]] = mac_address
    return if_info

# -------------------作业区域结束------------------------


if __name__ == "__main__":
    interface_info = port_and_mac(Pattern1, Pattern2)
    unitTest.check_if_info(interface_info)
    for info in interface_info:
        print("{}:{}".format(info, interface_info[info]))
    unitTest.output_error()
