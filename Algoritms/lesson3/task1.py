import random
import time
# а)
list_one = []
time_list_fill_one = round(time.perf_counter()*1000)
for i in range(0, 100000):
    list_one.append(i)
time_list_fill_two = round(time.perf_counter()*1000)
print(f'Время заполнения списка на 10млн элементов: {time_list_fill_two - time_list_fill_one}')

dict_one = {}
time_dict_fill_one = round(time.perf_counter()*1000)
for i in range(0, 100000):
    dict_one[i] = i
time_dict_fill_two = round(time.perf_counter()*1000)
print(f'Время заполнения словаря на 10млн элементов: {time_dict_fill_two - time_dict_fill_one}')

# б)

time_list_get_one = round(time.perf_counter()*1000)
for i in range(0, 100000):
    list_one[i]
time_list_get_two = round(time.perf_counter()*1000)
print(f'Время получения 10млн элементов из списка: {time_list_get_two - time_list_get_one}')

time_dict_get_one = round(time.perf_counter()*1000)
for i in range(0, 100000):
    dict_one[i]
time_dict_get_two = round(time.perf_counter()*1000)
print(f'Время получения 10млн элементов из словаря: {time_dict_get_two - time_dict_get_one}')
# Время заполнения словаря
# в)

time_list_get_one = round(time.perf_counter()*1000)
for i in range(0, 100000):
    list_one.remove(i)
time_list_get_two = round(time.perf_counter()*1000)
print(f'Время удаления 100 тысяч элементов из списка: {time_list_get_two - time_list_get_one}')

time_dict_get_one = round(time.perf_counter()*1000)
for i in range(0, 100000):
    dict_one.pop(i)
time_dict_get_two = round(time.perf_counter()*1000)
print(f'Время удаления 100тысяч элементов из словаря: {time_dict_get_two - time_dict_get_one}')

