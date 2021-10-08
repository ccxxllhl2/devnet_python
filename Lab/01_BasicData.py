# 整数
net_speed = 1000

# 浮点数
rssi = 55.6

# 字符串
hostname = "R1"
speed_str = "1000"

# 类型强制转换
result = net_speed + float(speed_str)
result2 = str(net_speed) + speed_str
print(result2)

# 布尔值
one_bool = True
print(5 * one_bool)

# 列表
ip_list = ["192.168.1.1",
           "192.168.2.100",
           "1.1.1.1",
           "100.100.100.100"]
print(ip_list)

# 元组
passwords = ("dsf323f32",
             "sdf32f23f2f2",
             "123456",
             "password")
print(passwords)

# 字典
users = {"admin": "admin123",
         "cisco": "cisco!234",
         "huawei": "hahaha123",
         "Yeslab": "xinwanggong"}
print(users)

# 集合
problem_list = ["星期一", "星期二", "星期三", "星期三", "星期三", "星期四", "星期五"]
uni_list = list(set(problem_list))
print(uni_list)