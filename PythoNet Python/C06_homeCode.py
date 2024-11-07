########################
### YESLAB 网工Python ###
########################
import unitTest


device_info = ["cisco_beijing01",
               "cisco_beijing02",
               "cisco_shanghai01",
               "cisco_shanghai02",
               "cisco_hangzhou02",
               "cisco_hangzhou02",
               "cisco_guangzhou02",
               "cisco_guangzhou02",]

# 此脚本需要完成以下任务：
# 公司所有的思科设备都换成华为了，设备的hostname前缀也需要从cisco改为huawei，用列表表达式完成这项任务
# -------------------作业区域开始------------------------
# TODO: 编写列表表达式new_device_info，将device_info里面的cisco前缀都更新为huawei


# -------------------作业区域结束------------------------


if __name__ == "__main__":
    unitTest.check_list_type(new_device_info)
    unitTest.check_list_length(new_device_info, len(device_info))
    unitTest.output_error()
    for info in new_device_info:
        print(info)
