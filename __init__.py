import sqlite3 as sq

with sq.connect('tourist.db') as con:
    con.execute("PRAGMA foreign_keys = ON;")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS bookings;")
    cur.execute("DROP TABLE IF EXISTS tourists;")
    cur.execute("DROP TABLE IF EXISTS tours;")

    cur.execute("""CREATE TABLE IF NOT EXISTS tourists (
    id_tourist INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    gender TEXT,
    date_burn TEXT,
    number TEXT,
    email TEXT);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS tours (
    id_tour INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    country TEXT,
    city TEXT,
    start_date TEXT,
    end_date TEXT,
    price REAL);""")

    cur.execute("""CREATE TABLE IF NOT EXISTS bookings (
    id_booking INTEGER PRIMARY KEY AUTOINCREMENT,
    booking_date TEXT,
    count INTEGER,
    id_tourist INTEGER
    REFERENCES tourists ON DELETE CASCADE ON UPDATE CASCADE,
    id_tour INTEGER
    REFERENCES tours ON DELETE CASCADE ON UPDATE CASCADE);""")


tourists_data = [
    ('Ivan', 'Ivanov', 'M', '1990-05-23', '+7 (912) 345-6789', 'ivan.ivanov@example.com'),
    ('Maria', 'Petrova', 'F', '1987-12-01', '+7 (923) 456-7890', 'maria.petrova@example.com'),
    ('Sergei', 'Sidorov', 'M', '1985-06-12', '+7 (934) 567-8901', 'sergei.sidorov@example.com'),
    ('Elena', 'Kuznetsova', 'F', '1993-02-25', '+7 (945) 678-9012', 'elena.kuznetsova@example.com'),
    ('Maxim', 'Smirnov', 'M', '1988-09-18', '+7 (956) 789-0123', 'maxim.smirnov@example.com'),
    ('Olga', 'Novikova', 'F', '1991-11-06', '+7 (967) 890-1234', 'olga.novikova@example.com'),
    ('Dmitry', 'Morozov', 'M', '1983-08-29', '+7 (978) 901-2345', 'dmitry.morozov@example.com'),
    ('Natalia', 'Belyaeva', 'F', '1989-04-15', '+7 (989) 012-3456', 'natalia.belyaeva@example.com'),
    ('Alexei', 'Fedorov', 'M', '1986-03-07', '+7 (990) 123-4567', 'alexei.fedorov@example.com'),
    ('Anastasia', 'Kuzmina', 'F', '1994-07-21', '+7 (901) 234-5678', 'anastasia.kuzmina@example.com')
]

tours_data = [
    ('Tour 1', 'USA', 'New York', '2023-05-01', '2023-05-07', 1000.0),
    ('Испания-путешествие по городам', 'Spain', 'Barcelona', '2023-06-15', '2023-06-25', 1500.0),
    ('Tour 3', 'Italy', 'Rome', '2023-07-10', '2023-07-20', 7000.0),
    ('Tour 4', 'France', 'Paris', '2023-08-01', '2023-08-10', 2500.0),
    ('Tour 5', 'Australia', 'Sydney', '2023-09-05', '2023-09-15', 3000.0),
    ('Tour 6', 'Japan', 'Tokyo', '2023-10-01', '2023-10-07', 1200.0),
    ('Tour 7', 'Canada', 'Toronto', '2023-11-15', '2023-11-25', 10800.0),
    ('Tour 8', 'Thailand', 'Bangkok', '2023-12-10', '2023-12-20', 2200.0),
    ('Tour 9', 'Brazil', 'Rio de Janeiro', '2024-01-01', '2024-01-10', 2700.0),
    ('Tour 10', 'Russia', 'Moscow', '2024-02-05', '2024-02-15', 3200.0)
]

bookings_data = [
    ('2023-04-08', 2, 1, 3),
    ('2023-04-09', 1, 2, 4),
    ('2023-04-10', 3, 3, 2),
    ('2023-04-11', 2, 4, 1),
    ('2023-04-12', 1, 5, 5),
    ('2023-04-13', 4, 6, 7),
    ('2023-04-14', 2, 7, 8),
    ('2023-04-15', 1, 8, 6),
    ('2023-04-16', 3, 9, 10),
    ('2023-04-17', 2, 10, 9)
]


with sq.connect('tourist.db') as con:
    cur = con.cursor()

    cur.executemany("INSERT INTO tourists (name, surname, gender, date_burn, number, email) VALUES (?, ?, ?, ?, ?, ?)",
                    tourists_data)
    cur.executemany("INSERT INTO tours (name, country, city, start_date, end_date, price) VALUES (?, ?, ?, ?, ?, ?)",
                    tours_data)
    cur.executemany("INSERT INTO bookings (booking_date, count, id_tourist, id_tour) VALUES (?, ?, ?, ?)",
                    bookings_data)


# SELECTS
with sq.connect('tourist.db') as con:
    cur = con.cursor()

    # 1. Вывести список всех туристов
    cur.execute("SELECT * FROM tourists;")
    print("Список всех туристов:")
    print(cur.fetchall())

    # 2. Вывести список всех туров, отсортированных по цене в порядке убывания
    cur.execute("SELECT * FROM tours ORDER BY price DESC;")
    print("Список всех туров, отсортированных по цене в порядке убывания:")
    print(cur.fetchall())

    # 3. Вывести список всех бронирований, сделанных в заданном городе
    city = "Paris"
    cur.execute("SELECT * FROM bookings JOIN tours ON bookings.id_tour=tours.id_tour WHERE tours.city=?;", (city,))
    print(f"Список всех бронирований, сделанных в городе {city}:")
    print(cur.fetchall())

    # 4. Вывести список всех туристов, сделавших бронирование в определенный период времени
    start_date = "2023-06-01"
    end_date = "2023-08-31"
    cur.execute("""SELECT tourists.* FROM tourists JOIN bookings ON tourists.id_tourist=bookings.id_tourist JOIN
    tours ON bookings.id_tour=tours.id_tour WHERE tours.start_date >= ? AND tours.end_date <= ?;""",
                (start_date, end_date))
    print(f"Список всех туристов, сделавших бронирование в период с {start_date} по {end_date}:")
    print(cur.fetchall())

    # 5. Вывести список всех туров с указанием названия страны и города
    cur.execute("SELECT name, country, city FROM tours;")
    print("Список всех туров с указанием названия страны и города:")
    print(cur.fetchall())

    # 6. Вывести список всех туристов, женщин, у которых дата рождения позже 01.01.1990
    cur.execute("SELECT * FROM tourists WHERE gender='F' AND date_burn > '1990-01-01';")
    print("Список всех женщин-туристов, родившихся после 01.01.1990:")
    print(cur.fetchall())

    # 7. Вывести список всех туров, цена которых больше 5000
    cur.execute("SELECT * FROM tours WHERE price > 5000;")
    print("Список всех туров, цена которых больше 5000:")
    print(cur.fetchall())

    # 8. Вывести список всех туристов, которые сделали бронирование на конкретный тур
    cur.execute("""SELECT tourists.name, tourists.surname, tours.name FROM tourists JOIN
    bookings b ON tourists.id_tourist = b.id_tourist JOIN tours ON tours.id_tour = b.id_tour WHERE tours.name = ?""",
                ('Tour 2',))
    print('Список туристов, которые забронировали тур "Tour 2":')
    print(cur.fetchall())

    # 9. Вывести список всех туристов, которые сделали бронирование на тур в указанную дату
    cur.execute("""SELECT tourists.name, tourists.surname, tours.name, tours.start_date FROM tourists JOIN
    bookings b ON tourists.id_tourist = b.id_tourist JOIN
    tours ON tours.id_tour = b.id_tour WHERE tours.start_date = ?""", ('2023-06-15',))
    print('Список туристов, которые забронировали тур на 15 июня 2023 года:')
    print(cur.fetchall())

    # 10. Вывести список всех туристов, у которых номер телефона начинается на "+7"
    cur.execute("SELECT name, surname, number FROM tourists WHERE number LIKE '+7%'")
    print('Список туристов, у которых номер телефона начинается на "+7":')
    print(cur.fetchall())


# UPDATES
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#
#     # 1. Изменить дату начала тура с id=1 на '2023-05-01'
#     cur.execute("UPDATE tours SET start_date='2023-05-01' WHERE id_tour=1;")
#
#     # 2. Обновить цену тура с id=7 на 1500
#     cur.execute("UPDATE tours SET price=1500 WHERE id_tour=7;")
#
#     # 3. Изменить номер телефона туриста с id=5 на '+1 (555) 123-4567'
#     cur.execute("UPDATE tourists SET number='+1 (555) 123-4567' WHERE id_tourist=5;")
#
#     # 4. Изменить дату бронирования с id=3 на '2023-04-05'
#     cur.execute("UPDATE bookings SET booking_date='2023-04-05' WHERE id_booking=3;")
#
#     # 5. Обновить количество туристов в бронировании с id=8 на 3
#     cur.execute("UPDATE bookings SET count=3 WHERE id_booking=8;")
#
#     # 6. Изменить дату окончания тура с id=2 на '2023-08-31'
#     cur.execute("UPDATE tours SET end_date='2023-08-31' WHERE id_tour=2;")
#
#     # 7. Обновить электронную почту туриста с id=1 на 'new_email@example.com'
#     cur.execute("UPDATE tourists SET email='new_email@example.com' WHERE id_tourist=1;")
#
#     # 8. Изменить дату начала тура с id=4 на '2023-06-15'
#     cur.execute("UPDATE tours SET start_date='2023-06-15' WHERE id_tour=4;")
#
#     # 9. Обновить дату начала тура на 2023-05-01 для всех туров, где страна = 'Испания':
#     cur.execute("UPDATE tours SET start_date = '2023-05-01' WHERE country = 'Spain';")
#
#     # 10. Обновление цены на тур "Греция-отдых на море" на 1500 у.е.
#     cur.execute("UPDATE tours SET price = 1500 WHERE name = 'Греция-отдых на море';")
#
#     # 11. Обновление даты начала тура "Испания-путешествие по городам" на 2023-06-01.
#     cur.execute("UPDATE tours SET start_date = '2023-06-01' WHERE name = 'Испания-путешествие по городам';")
#
#     # 12. Обновление количества туристов в бронировании с id 1002 на 3 человека.
#     cur.execute("UPDATE bookings SET count = 3 WHERE id_booking = 2;")
#
#     # 13. Обновление номера телефона у туриста с id 2001 на +1 (123) 456-7890.
#     cur.execute("UPDATE tourists SET number = '+1 (123) 456-7890' WHERE id_tourist = 1;")
#
#     # 14. Обновление даты начала тура на 2024-07-01 для всех туров, цена которых меньше 2000 у.е.
#     cur.execute("UPDATE tours SET start_date = '2024-07-01' WHERE price < 2000;")
#
#     # 15. Обновление электронной почты у всех туристов из России на new_email@example.com.
#     cur.execute("""UPDATE tourists SET email = 'new_email@example.com' WHERE id_tourist IN
#     (SELECT bookings.id_tourist FROM bookings JOIN
#     tours ON bookings.id_tour = tours.id_tour WHERE country = 'Russia');""")
#
#     # 16. Обновление даты начала тура на 2023-08-15 для всех бронирований с количеством туристов больше 2.
#     cur.execute("UPDATE bookings SET id_tour = 3 WHERE count > 2;")
#
#     # 17. Обновление названия тура на "Египет-отдых на курорте" для всех бронирований с id_тура равным 1003.
#     cur.execute("UPDATE tours SET name = 'Египет-отдых на курорте' WHERE id_tour = 3;")


# DELETES
# with sq.connect('tourist.db') as con:
#     cur = con.cursor()
#
#     # 1. Удалить все бронирования, связанные с туристом с id=1
#     cur.execute("DELETE FROM bookings WHERE id_tourist=1")
#
#     # 2. Удалить все бронирования, связанные с туром с id=2
#     cur.execute("DELETE FROM bookings WHERE id_tour=2")
#
#     # 3. Удалить все бронирования, сделанные в определенную дату
#     cur.execute("DELETE FROM bookings WHERE booking_date='2023-04-12'")
#
#     # 4. Удалить всех туристов, которые сделали бронирование на тур с id=3
#     cur.execute("DELETE FROM tourists WHERE id_tourist IN (SELECT id_tourist FROM bookings WHERE id_tour=3)")
#
#     # 5. Удалить все бронирования, сделанные туристом с определенным номером телефона
#     cur.execute("DELETE FROM bookings WHERE id_tourist IN (SELECT id_tourist FROM tourists WHERE number=?)",
#                 ('+7 (923) 456-7890',))
#
#     # 6. Удалить все бронирования, сделанные туристом с определенной электронной почтой
#     cur.execute("""DELETE FROM bookings WHERE id_tourist IN (SELECT id_tourist FROM tourists WHERE email = ?)""",
#                 ('natalia.belyaeva@example.com',))
#
#     # 7. Удалить все бронирования на туры, начинающиеся после определенной даты
#     cur.execute("""DELETE FROM bookings WHERE id_tour IN (SELECT id_tour FROM tours WHERE start_date > ?)""",
#                 ('2023-04-15',))
#
#     # 8. Удалить всех туристов, которые забронировали тур в определенную страну
#     cur.execute("""DELETE FROM tourists WHERE id_tourist IN (SELECT id_tourist FROM bookings JOIN
#     tours ON bookings.id_tour = tours.id_tour WHERE tours.country = ?)""", ('Spain',))
#
#     # 9. Удалить все бронирования на туры, заканчивающиеся до определенной даты
#     cur.execute("""DELETE FROM bookings WHERE id_tour IN (SELECT id_tour FROM tours WHERE end_date < ?)""",
#                 ('2023-04-10',))
#
#     # 10. Удалить все бронирования, сделанные на тур с определенной ценой
#     cur.execute("""DELETE FROM bookings WHERE id_tour IN (SELECT id_tour FROM tours WHERE price = ?)""", (1500.0,))
