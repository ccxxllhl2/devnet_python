userdict = {"admin": "admin123",
            "root": "123456",
            "yeslab": "ciscoHUAWEI"}

# 直接for循环
for one in userdict:
    print(one)

# 指定对键进行循环
for one in userdict.keys():
    print(one)

# 指定对值进行循环
for one in userdict.values():
    print(one)

# 指定对item进行循环
for one in userdict.items():
    print(one)

# 提取键
print(list(userdict.keys()))

# 提取值
print(list(userdict.values()))