dict_ip = {}
with open("log.txt", "r") as f:
    line = f.readline()
    while line:
        ip = line.split(" ")[0]
        if ip in dict_ip.keys():
            count_request = dict_ip[ip]
            count_request += 1
            dict_ip[ip] = count_request
        else:
            dict_ip[ip] = 1
        line = f.readline()
dict_ip_sorted = dict(sorted(dict_ip.items(), key = lambda x: x[1], reverse = True))
print(f'Spammer: {list(dict_ip_sorted.keys())[0]} , Sent: {list(dict_ip_sorted.values())[0]}')
