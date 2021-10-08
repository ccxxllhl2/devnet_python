# 数据部分
ip_list = ["192.168.1.1",
           "192.168.1.2",
           "192.168.1.3",
           "192.168.1.4",
           "192.168.1.5"]


# 函数定义部分
def output_ip():
    for ip in ip_list:
        print(ip)
    print("所有的IP都处理完了！")

# 函数使用部分
output_ip()