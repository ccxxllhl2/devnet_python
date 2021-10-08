from data import ipData
from functions import ipFuntion

ip_count = ipFuntion.output_ip(ipData.IP_LIST, ipData.COUNT_LIST, is_count=True)
print(ip_count)