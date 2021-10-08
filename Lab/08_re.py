import re

with open("data/log.txt") as file:
    logs = file.read()

pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
ip_list = list(set(re.findall(pattern, logs)))
for ip in ip_list:
    print(ip)
