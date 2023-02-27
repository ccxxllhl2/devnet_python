########################
### YESLAB 网工Python ###
########################

import unitTest

# 此脚本包含一个华为CE12800路由器类，这个类可以实现如下功能：
# display_version功能可以输出设备版本
# display_interface功能可以输出接口信息
# 但是程序中存在错误导致不能执行，参照实验手册中执行成功的截图，对程序进行排错
# -------------------作业区域开始------------------------
# TODO: 修正下面代码中的错误


class huaweiCE12800:
    #hostname = "CE"
    def __init__(self, sysname):
        self.hostname = sysname

    def display_version(self):
        print("-"*40)
        print("[{}]dislay version".format(self.hostname))
        with open("data/huawei_ce_ver.txt") as ver_file:
            version_info = ver_file.read()
        print(version_info)

    def display_interface(self):
        print("[{}]dislay interface brief".format(self.hostname))
        with open("data/huawei_ce_int.txt") as if_file:
            interface_info = if_file.read()
        print(interface_info)
        print("-" * 40)


switch = huaweiCE12800("Huawei-CE12800")
switch.display_version()
switch.display_interface()

# -------------------作业区域结束------------------------
if __name__ == "__main__":
    unitTest.check_class_pri(huaweiCE12800)
    unitTest.output_error()