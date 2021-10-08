# 字符串的索引
one_str = "HCIE and CCIE"
hcie_str = one_str[0:4]
print(hcie_str)
ccie_str = one_str[-4:]
print(ccie_str)

# 列表的索引
one_list = ["HCIA", "HCIP", "HCIE", "YESLAB", "CCNA", "CCNP", "CCIE"]
huawei_list = one_list[0:3]
print(huawei_list)
cisco_list = one_list[-3:]
print(cisco_list)

# 字符串转列表
str_to_list = one_str.split(" ")
print(str_to_list)

# 列表转字符串
list_to_str = " ".join(str_to_list)
print(list_to_str)

# 字符串格式化输出
device_name = "ISR6500"
interface_name = "GE1/0/24"
net_speed = 120.0102030405
print("{}设备的{}接口的当前网速为：{:.2f}mb/s".format(device_name, interface_name, net_speed))

# 列表内容添加
one_list = ["HCIA", "HCIP", "HCIE", "YESLAB", "CCNA", "CCNP"]
print("append前：{}".format(one_list))
one_list.append("CCIE")
print("append后：{}".format(one_list))

one_list = ["HCIA", "HCIP", "HCIE", "YESLAB", "CCNA", "CCNP"]
print("extend前：{}".format(one_list))
one_list.extend(["CCIE"])
print("extend后：{}".format(one_list))

# 列表元素排序
test_list = [2, 1, 5, 3, 4, 7, 6]
test_list.sort()
test_list.reverse()
print(test_list)

# 列表的深拷贝与浅拷贝
listA = [1, 2, 3]
listB = listA.copy()
listA[1] = 99
print("listA:{}".format(listA))
print("listB:{}".format(listB))