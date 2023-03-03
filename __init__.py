import re
s = '''Стаж работы сотрудников в ООО "Регуляр"

Иванов И.И.	26 лет 8 месяцев
Петров П.П	14 лет 2 месяца
Базаров Г.К.	18 лет 5 месяцев
Лабутин С.Д.	1 год 11 месяцев
Лазухина Т.П.	2 года 6 месяцев
Паланова З.К.	15 лет 1 месяц
Таничева У.С.	15 лет 10 месяцев
Каверин Т.Д.	21 год 4 месяца
Зудина К.Ю.	3 года'''

print(*re.findall(r"(\d+ \w+)\s?(\d+ месяц.*$)?", s, re.M), sep='\n')
