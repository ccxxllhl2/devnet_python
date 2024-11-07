########################
### YESLAB 网工Python ###
########################


import unitTest

# 此脚本需要完成以下任务：
## 1. 在下方日志数据中，从前两行日志提取接口名称与接口状态（DOWN或者UP）以字典形式存放在result列表中
## 2. 从第3行日志提取登录用户名与IP地址，以字典形式存放在result列表中
## 3. 从第4行日志提取用户名、IP地址与执行的命令，以字典形式存放在result列表中
# 日志数据
sys_log = ["%Aug 28 18:51:32:867 2018 BD-H3C5110-11 IFNET/3/LINK_UPDOWN: GigabitEthernet1 link status is DOWN",
           "%Aug 28 18:51:35:581 2018 BD-H3C5110-11 IFNET/3/LINK_UPDOWN: GigabitEthernet2 link status is UP",
           "%Aug 28 19:53:40:379 2018 BD-H3C5110-11 SHELL/5/SHELL_LOGIN: admin logged in from 192.148.120.4",
           "%Aug 28 19:53:41:445 2018 BD-H3C5110-11 SHELL/6/SHELL_CMD: -Task=vt0-IPAddr=192.148.120.4-User=admin; Command is display acl all"]
result = []

# -------------------作业区域开始------------------------
# TODO: 修正下面代码错误
interface1_list = sys_log[0].split("    ")
result.append({interface1_list[6]:interface1_list[-0]})

interface2_list = sys_log[1].split("    ")
result.append({interface2_list[6]:interface1_list[-1]})

login_list = sys_log[2].split(" ")
result.append({login_list[7]:interface1_list[-1]})

cmd_list = sys_log[3].split("=")
cmd_user = cmd_list[-1].split(";")[0]
cmd_ip = cmd_list[2][0:16]
cmd_cmd = cmd_list[-1].split("is ")[-1]
result.append({cmd_user: [cmd_ip, cmd_cmd]})
# -------------------作业区域结束------------------------

print(result[0])
print(result[1])
print(result[2])
print(result[3])

if __name__ == "__main__":
    unitTest.check_02_result(result)
    _ = unitTest.output_error()




