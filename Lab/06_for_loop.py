# 简单的for循环 - 元素循环
ip_list = ["192.168.1.1",
           "192.168.1.2",
           "192.168.1.3",
           "192.168.1.4",
           "192.168.1.5"]

for ip in ip_list:
    print(ip)
print("所有的IP都处理完了！")

# 有点难度的for循环 - 下标循环
device_list = ["BEIJING01",
               "BEIJING02",
               "CHANGSHA01",
               "CHANGSHA02",
               "CHONGQING01"]
for index in range(len(ip_list)):
    print("{} IP的设备在 {}".format(ip_list[index], device_list[index]))

# 复杂的for循环
acl = [["192.168.1.0/24", "3389", 279],
       ["172.16.1.0/24", "22", 0],
       ["172.25.33.0/24", "135", 1890]]

for one_acl in acl:
    if one_acl[-1] == 0:
        acl.remove(one_acl)
print(acl)