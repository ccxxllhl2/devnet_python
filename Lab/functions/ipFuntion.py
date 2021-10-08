def output_ip(list_ip, list_count, is_count=True):
    if is_count:
        ip_access_count = {}
        for i in range(len(list_ip)):
            ip_access_count[list_ip[i]] = list_count[i]
        return ip_access_count
    else:
        return list_ip