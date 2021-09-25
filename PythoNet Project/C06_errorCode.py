########################
### YESLAB 网工Python ###
########################

import re
import unitTest

net_speed = ["500Kbps", "100Kbps", "3000Kbps", "12000Kbps"]
# 此脚本需要完成以下任务：
# 对net_speed里面的所有网速值进行单位统一，都换算成Mbps
# -------------------作业区域开始------------------------
# TODO: 修正下面代码中的错误
num_pattern = r"[0-9]*"
char_pattern = r"[a-zA-Z].*"
values = [int(re.search(num_pattern, data)) for data in net_speed]
new_net_speed = [str(value*0.001)+"Mbps" for value in value]
# -------------------作业区域结束------------------------


if __name__ == "__main__":
    unitTest.check_list_length(new_net_speed, len(net_speed))
    unitTest.output_error()
    print(new_net_speed)