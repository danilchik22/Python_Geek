list_prices = [57.8, 46.51, 97, 34.5, 105.7, 104.45, 10.1, 5.45, 45.90, 3.1, 23.45]
for price in list_prices:
    rub = str(price).split('.')[0]
    kop = "00"
    if isinstance(price, float):
        kop = str(price).split('.')[1]
    if len(kop) == 1:
        kop = kop + "0"
    print(f'{rub} руб {kop} коп')
print('\n')
print(id(list_prices))
list_prices.sort()
print('ID отсортированного списка такой же: ')
print(id(list_prices))
for price in list_prices:
    print(f'{price} ', end=' ')
new_list_prices = list_prices[:]
new_list_prices.sort(reverse=True)
for most_expensive in new_list_prices[0:5]:
    print(most_expensive)