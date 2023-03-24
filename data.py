from random import randint, choice, random

info_form = [
    (
        i,
        'name ' + str(i),
        'surname ' + str(i),
        i + 10,
        randint(1, 2),
        randint(1, 31),
        'post ' + str(randint(1, 10)),
        choice(('IT', 'not IT')),
        random() * 10
    ) for i in range(1, 51)]

info_list = [
    (
        i,
        (start_date := randint(1, 31)),
        randint(start_date + 1, 32),
        'cause ' + str(i),
        'diagnosis ' + str(i),
        randint(0, 1),
        randint(1, 51)
    ) for i in range(1, 100)
]
