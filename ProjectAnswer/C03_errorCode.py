########################
### YESLAB 网工Python ###
########################


import unitTest

# 此脚本需要完成以下任务：
## 1. 一台交换机有5个端口，但是目前没有配置IP地址
## 2. 将每个端口从字符串改为字典，键为端口名称，值为IP地址

switch_ports = ["GigabitEthernet1/1/1",
                "GigabitEthernet1/1/2",
                "GigabitEthernet1/1/3",
                "Loopback1",
                "Loopback100"]

# -------------------作业区域开始------------------------
# TODO: 修正下面代码错误
new_list = []
sub_net_ip = 0
for index in range(len(switch_ports)):
    port_name = switch_ports[0]
    sub_net_ip += 1
    ip_address = "192.168.1." + str(sub_net_ip)
    new_list.append({port_name: ip_address})
    
switch_ports = new_list

# -------------------作业区域结束------------------------

if __name__ == "__main__":
    for info in switch_ports:
        unitTest.check_03_info(info)
        print(info)
    unitTest.output_error()




