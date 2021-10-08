import random

scan_num = 10
while scan_num > 0:
    mem_scan = random.randint(0, 1024)
    print("内存剩余量：", mem_scan)
    if mem_scan < 100:
        print("内存不足，请进行运维操作!")
    elif (mem_scan >= 100) and (mem_scan < 500):
        print("内存用量较大，邮件告警!")
    else:
        print("没事，接着喝茶！")
    scan_num -= 1