list_cube = []
sum_all = 0
sum_all_17 = 0
for element in range(1,1001):
    if element%2 != 0:
        element_cube = element**3
        list_cube.append(element_cube)
        sum_figures = 0
        for figure in range(len(str(element_cube))):
            sum_figures += int(str(element_cube)[figure])
        if sum_figures % 7 == 0:
            sum_all += element_cube
        sum_figures = 0
        element_cube = element_cube + 17
        for figure in range(len(str(element_cube))):
            sum_figures += int(str(element_cube)[figure])
        if sum_figures % 7 == 0:
            sum_all_17 += element_cube
print(sum_all)
print(sum_all_17)