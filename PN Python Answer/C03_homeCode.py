########################
### YESLAB 网工Python ###
########################


import unitTest
from funSystem import funRouter

R1 = funRouter.CiscoNXOS("eastDC")
R2 = funRouter.CiscoNXOS("westDC")
R3 = funRouter.CiscoIOSXE("baseSwitch")
R4 = funRouter.CiscoIOS("branchSwitch")
Routers = [R1, R2, R3, R4]


def ssh(router, username, password):
    unitTest.ssh_check(router, username, password)

# -------------------作业区域开始------------------------
# 上面的Routers已经初始化了4台路由器，每台路由器的型号可以通过device_type属性进行查看，例如R1.device_type会得到R1的设备型号为Cisco NX-OS
# 每台设备都有对应的型号、用户名和密码，具体参见实验手册
# 下面的代码是通过SSH连接一台设备的代码，你需要将其改为通过for循环依次登录Routers列表中4台设备的程序
# 注意在for循环中还要编写if判断语句，为每一台设备的SSH登录提供合适的密码
# 以下是登录R1的代码：
for device in Routers:
    if device.device_type == 'Cisco IOS':
        username = "admin"
        password = "admin"
    elif device.device_type == 'Cisco IOS-XE':
        username = "Cadmin"
        password = "GuangdongHAHA"
    elif device.device_type == 'Cisco IOS-XR':
        username = "ciscoSuper"
        password = "Super@super"
    else:
        username = "NXoperator"
        password = "WoShiXinWangGong"
    ssh(device, username, password)





# -------------------作业区域结束------------------------

if __name__ == "__main__":
    unitTest.output_error()




