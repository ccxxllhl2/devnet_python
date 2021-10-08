with open("data/log.txt", "r") as file:
    logs = file.read()
datas = logs.split('\n')

data1 = datas[0][19:]
data2 = datas[1][19:]
data3 = datas[2][19:]
data4 = datas[3][19:]
data5 = datas[4][19:]

full_5_logs = "\n".join([data1, data2, data3, data4, data5])

with open("data/full_5_log.txt", "w") as file:
    file.write(full_5_logs)