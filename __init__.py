import sqlite3 as sq

with sq.connect('tourist.db') as con:
    con.execute("PRAGMA foreign_keys = ON;")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS tourists;")
    cur.execute("DROP TABLE IF EXISTS tours;")
    cur.execute("DROP TABLE IF EXISTS bookings;")

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
    star_date TEXT,
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
    tours ON bookings.id_tour=tours.id_tour WHERE tours.star_date >= ? AND tours.end_date <= ?;""",
                (start_date, end_date))
    print(f"Список всех туристов, сделавших бронирование в период с {start_date} по {end_date}:")
    print(cur.fetchall())

    # 5. Вывести список всех туров с указанием названия страны и города
    cur.execute("SELECT name, country, city FROM tours;")
    print("Список всех туров с указанием названия страны и города:")
    print(cur.fetchall())

    # 6. Вывести список всех туристов, женщин, у которых дата рождения позже 01.01.1990
    cur.execute("SELECT * FROM tourists WHERE gender='Female' AND date_burn > '1990-01-01';")
    print("Список всех женщин-туристов, родившихся после 01.01.1990:")
    print(cur.fetchall())

    # 7. Вывести список всех туров, цена которых больше 5000
    cur.execute("SELECT * FROM tours WHERE price > 5000;")
    print("Список всех туров, цена которых больше 5000:")
    print(cur.fetchall())

    # 8. Вывести список всех туристов, которые сделали бронирование на конкретный тур
    cur.execute("""SELECT tourists.name, tourists.surname, tours.name FROM tourists JOIN
    bookings b ON tourists.id_tourist = b.id_tourist JOIN tours ON tours.id_tour = b.id_tour WHERE tours.name = ?""",
                ('Tour A',))
    print('Список туристов, которые забронировали тур "Tour A":')
    print(cur.fetchall())

    # 9. Вывести список всех туристов, которые сделали бронирование на тур в указанную дату
    cur.execute("""SELECT tourists.name, tourists.surname, tours.name, tours.star_date FROM tourists JOIN
    bookings b ON tourists.id_tourist = b.id_tourist JOIN
    tours ON tours.id_tour = b.id_tour WHERE tours.star_date = ?""", ('2023-06-15',))
    print('Список туристов, которые забронировали тур на 15 июня 2023 года:')
    print(cur.fetchall())

    # 10. Вывести список всех туристов, у которых номер телефона начинается на "+7"
    cur.execute("SELECT name, surname, number FROM tourists WHERE number LIKE '+7%'")
    print('Список туристов, у которых номер телефона начинается на "+7":')
    print(cur.fetchall())
