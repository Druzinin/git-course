from random import randint, choice
from datetime import date

d2 = date.today()
f = '-%m-%d'

info_form = [
    (
        i,
        'Имя ' + str(i),
        'Фамилия ' + str(i),
        (d1 := date(*map(lambda x: randint(*x), ((1950, 1999), (1, 12), (1, 28))))).strftime('19%y-%m-%d'),
        randint(1, 2),
        f"{(d2 := date(*map(lambda x: randint(*x), ((d1.year + 18, 2023), (1, 12), (1, 28))))).year}" + d2.strftime(f),
        'post ' + str(randint(1, 10)),
        choice(('IT', 'frontend', 'backend')),
        randint(50_000, 120_000)
    ) for i in range(1, 51)
]

info_list = [
    (
        i,
        (st := date(*map(lambda x: randint(*x), ((d2.year, 2023), (1, 12), (1, 28))))).strftime('20%y-%m-%d'),
        str((en := date(*map(lambda x: randint(*x), ((st.year, st.year + 1), (1, 12), (1, 28))))).year) + en.strftime(f),
        'причина ' + str(i),
        'диагноз ' + str(i),
        choice(('NO', 'YES', 'NO')),
        randint(1, 50)
    ) for i in range(1, 100)
]
