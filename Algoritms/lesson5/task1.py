from collections import namedtuple

Company = namedtuple('Company', 'Name Profit_quarter1 Profit_quarter2 Profit_quarter3 Profit_quarter4')
companies = []
number_companies = 0
try:
    number_companies = int(input('Введите число компаний: '))
except ValueError:
    print('Ввод некорректен')

for i in range(number_companies):
    name = input('Введите название компании: ')
    try:
        profit1 = int(input('Введите прибыль компании за 1 квартал: '))
        profit2 = int(input('Введите прибыль компании за 2 квартал: '))
        profit3 = int(input('Введите прибыль компании за 3 квартал: '))
        profit4 = int(input('Введите прибыль компании за 4 квартал: '))
        companies.append(Company(name, profit1, profit2, profit3, profit4))
    except ValueError:
        print('Прибыль должна быть число')
if len(companies) != 0:
    all_profit = 0
    for company in companies:
        year_profit_company = (company.Profit_quarter1 + company.Profit_quarter2 + company.Profit_quarter3 +
                                  company.Profit_quarter4)
        all_profit += year_profit_company
    companies_below = {company.Name for company in companies if company.Profit_quarter1 + company.Profit_quarter2 +
                       company.Profit_quarter3 + company.Profit_quarter4 < all_profit / len(companies)}
    companies_higher = {company.Name for company in companies if company.Profit_quarter1 + company.Profit_quarter2 +
                       company.Profit_quarter3 + company.Profit_quarter4 > all_profit / len(companies)}
    print(f'Среднегодовая прибыль всех предприятий: {all_profit / len(companies)}')
    print('Предприятия с прибылью ниже средней: ')
    for name_company in companies_below:
        print(name_company)

    print('Предприятия с прибылью выше средней: ')
    for name_company in companies_higher:
        print(name_company)
