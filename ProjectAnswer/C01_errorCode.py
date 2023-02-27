########################
### YESLAB 网工Python ###
########################


# -------------------作业区域开始------------------------
# TODO: 修正代码错误
# 接口数据

interfaces_msg = [{"name": "ge0/0", "description": "manager", "status": "up"},
                  {"name": "ge0/1", "description": "core01", "status": "up"},
                  {"name": "ge0/2", "description": "core02", "status": "up"},
                  {"name": "ge0/3", "description": "branch01", "status": "up"},
                  {"name": "ge0/4", "description": "branch02", "status": "up"}]
# IP数据
ip_datas = {"interface0": "10.10.10.1",
            "interface1": "172.16.1.1",
            "interface2": "172.17.1.1",
            "interface3": "172.18.1.1",
            "interface4": "192.168.25.1"}
# -------------------作业区域结束------------------------

# 命令行输出数据
for int_index in range(5):
    int_name = list(interfaces_msg[int_index].values())[0]
    int_des = list(interfaces_msg[int_index].values())[1]
    int_status = list(interfaces_msg[int_index].values())[2]
    int_ip = list(ip_datas.values())[int_index]
    print(f"{int_des} 接口 {int_name} 目前的状态是 {int_status}，其IP地址为：{int_ip}")
