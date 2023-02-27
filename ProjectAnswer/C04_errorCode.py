########################
### YESLAB 网工Python ###
########################

import re
import unitTest

# 此脚本需要完成以下任务：
# 使用正则表达式在版本信息日志中提取关键信息，具体信息参见实验手册
# -------------------作业区域开始------------------------
# TODO: 修正下面代码错误
with open("data/verLOG.log") as file:
    verData = file.readlines()

software_info = []
pattern1 = r"H3C \w{1,7} \w{1,8} Software"
pattern2 = r"Version [0-9]+\.[0-9]+\.[0-9]+"
pattern3 = r"Release [0-9]{1,4}"

for data in verData:
    for pattern in [pattern1, pattern2, pattern3]:
        result = re.search(pattern, data)
        if result is not None:
            software_info.append(result.group())

# -------------------作业区域结束------------------------

if __name__ == "__main__":
    unitTest.check_software_info(software_info)
    for info in software_info:
        print(info)
    unitTest.output_error()
