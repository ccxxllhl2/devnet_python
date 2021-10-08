# 数据
ping_list = [10, 50, 52, 3, 2, 1019, 2134, 513, 1126, 2652]
ops_data = [[40, 52, 13],
            [16, 19, 9],
            [87, 62, 94],
            [11, 17]]

# 基本的列表表达式
problem_list1 = [ping for ping in ping_list]
print(problem_list1)

# 加if的列表表达式
problem_list2 = [ping for ping in ping_list if ping > 1500]
print(problem_list2)

# 多重列表索引
mem_net_ops = [data[1]*0.01 for data in ops_data if len(data)==3]
print(mem_net_ops)