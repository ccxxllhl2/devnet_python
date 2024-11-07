import os

ERRORS = []


def output_error():
    if not ERRORS:
        print("恭喜！程序未发现已知错误")
        return False
    else:
        print("程序共包含 {} 个已知错误：".format(len(ERRORS)))
        for error in ERRORS:
            print("  - " + error)
        return True


def is_dir_exist(file_path):
    if not os.path.exists(file_path):
        ERRORS.append("路径{}存在问题，请检查沿途文件夹".format(file_path))


def check_file_name(file_name):
    if not file_name.endswith(".xlsx"):
        ERRORS.append("文件名不正确，后缀应该是.xlsx")


def check_data(data1, data2, data3, data4):
    if not (len(data1) == len(data2) == len(data3) == len(data4)):
        ERRORS.append("请保持各个数据列表元素个数相同")


def check_02_result(result):
    if result[0] != {'GigabitEthernet1': 'DOWN'}:
        ERRORS.append("第一行日志处理仍然有问题")
    if result[1] != {'GigabitEthernet2': 'UP'}:
        ERRORS.append("第二行日志处理仍然有问题")
    if result[2] != {'admin': '192.148.120.4'}:
        ERRORS.append("第三行日志处理仍然有问题")
    if result[3] != {'admin': ['192.148.120.4', 'display acl all']}:
        ERRORS.append("第四行日志处理仍然有问题")


def check_02_real_logs(real_logs):
    if type(real_logs) is not str:
        ERRORS.append("real_logs格式不是字符串")
    if real_logs.count("%") != 512:
        ERRORS.append("发现日志丢失了，请检查代码")


def ssh_check(router, username, password):
    if router.username != username:
        ERRORS.append("{}用户名错误".format(router.hostname))
    elif router.password != password:
        ERRORS.append("{}密码错误".format(router.hostname))
    else:
        router.ssh_reply()


def check_03_info(info):
    if type(info) != dict:
        ERRORS.append("switch_ports包含非字典数据")


def check_software_info(softwareInfo):
    if len(softwareInfo) != 3:
        ERRORS.append("某个正则表达式没有匹配到内容")
    elif softwareInfo[0] != 'H3C Comware Platform Software':
        ERRORS.append("系统型号不正确")
    elif softwareInfo[1] != 'Version 5.20.99':
        ERRORS.append("版本号不正确")
    elif softwareInfo[2] != 'Release 1105':
        ERRORS.append("发行号不正确")


def check_if_info(if_info):
    if len(if_info) != 28:
        ERRORS.append("发现有UP的接口没有统计进来")


def check_socket_msg_type(msg):
    if type(msg) != str:
        ERRORS.append("消息数据不是字符串，检查消息的encoding与decode相关代码")


def check_list_type(my_list):
    if type(my_list) != list:
        ERRORS.append("列表表达式创建类型错误")


def check_list_length(my_list, length):
    if len(my_list) != length:
        ERRORS.append("列表表达式中设备数量不正确")


def check_webex_rooms(rooms):
    if len(rooms) != 5:
        ERRORS.append("房间数量不正确")

def check_class_pri(my_class):
    try:
        my_class.hostname
        ERRORS.append("此实例不建议使用类属性，全部使用实例属性即可，请删去类属性的定义")
    except:
        pass
