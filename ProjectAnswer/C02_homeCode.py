########################
### YESLAB 网工Python ###
########################
'''
LAB：此脚本是一个从给定文件提取网络设备日志的程序
你需要编写所有带TODO标记处描述的任务，以补完这个脚本
作业部分已经用分割线标记位置了，不在作业区域的代码不建议更改
'''

import unitTest

with open("data/HWLOG.log") as file:
    log_datas = file.read()
# -------------------作业区域开始------------------------
# TODO：完成下面的代码，按实验手册的要求将 log_datas 中的CPU信息部分去除掉，剩余的日志以字符串形式存放在real_logs中
real_logs = log_datas.split("syslog:")[1]

# -------------------作业区域结束------------------------

if __name__ == "__main__":
    print("总共检测到{}行日志".format(real_logs.count("%")))
    unitTest.check_02_real_logs(real_logs)
    unitTest.output_error()
