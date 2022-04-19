import os
import json


dict_result = {}
folder_name = os.getcwd()
for root, dirs, files in os.walk(folder_name):
    for file in files:
        full_path_file = os.path.join(root, file)
        size = os.stat(full_path_file).st_size
        count = 1
        while True:
            if size <= 10*count:
                if 10*count in dict_result:
                    list = dict_result[10*count][1]
                    if not full_path_file.split(".")[-1] in list:
                        list.append(full_path_file.split(".")[-1])
                    dict_result[10*count] = (dict_result[10*count][0]+1, list)
                else:
                    dict_result[10*count] = (1, [full_path_file.split(".")[-1]])
                break
            count = count*10
dict_result = dict(sorted(dict_result.items(), key = lambda x: x[0]))
for key, value in dict_result.items():
    print(f"{key}: {value}")
name = folder_name + "_summary.json"
with open(name, "w", encoding="utf-8") as f:
    json.dump(dict_result, f)