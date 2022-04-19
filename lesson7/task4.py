import os
dict_result = {}
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        count = 1
        while True:
            if size <= 10*count:
                if 10*count in dict_result:
                    dict_result[10*count] = dict_result[10*count]+1
                else:
                    dict_result[10*count] = 1
                break
            count = count*10
dict_result = dict(sorted(dict_result.items(), key = lambda x: x[0]))
print(dict_result)