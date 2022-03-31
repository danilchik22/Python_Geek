По второй задаче есть второй вариант решения через остаток от деления и целые части от деления:

list_cube = []
sum_all = 0
sum_all_17 = 0
for element in range(1,1001):
    if element%2 != 0:
        element_cube = element**3
        list_cube.append(element_cube)
        sum_figures = element_cube%10 + element_cube%100//10 + element_cube%1000//100 + element_cube%10000//1000 + element_cube%100000//10000 + element_cube%1000000//100000 + element_cube%10000000//1000000 + element_cube%100000000//10000000 + element_cube%1000000000//100000000
        if sum_figures%7 == 0:
            sum_all += element_cube
        element_cube = element_cube + 17
        sum_figures = element_cube%10 + element_cube%100//10 + element_cube%1000//100 + element_cube%10000//1000 + element_cube%100000//10000 + element_cube%1000000//100000 + element_cube%10000000//1000000 + element_cube%100000000//10000000 + element_cube%1000000000//100000000
        if sum_figures%7 == 0:
            sum_all_17 += element_cube
print(sum_all)
print(sum_all_17)