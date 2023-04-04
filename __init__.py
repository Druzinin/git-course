import sqlite3 as sq

with sq.connect('tourist.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Туристы;")
    cur.execute("DROP TABLE IF EXISTS Туры;")
    cur.execute("DROP TABLE IF EXISTS Бронирования;")
    cur.execute('''CREATE TABLE IF NOT EXISTS Туристы (
    id INTEGER PRIMARY KEY,
    имя TEXT NOT NULL,
    фамилия TEXT NOT NULL,
    пол TEXT NOT NULL,
    дата_рождения TEXT NOT NULL,
    номер_телефона TEXT,
    электронная_почта TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Туры (
    id INTEGER PRIMARY KEY,
    название TEXT NOT NULL,
    страна TEXT NOT NULL,
    город TEXT NOT NULL,
    дата_начала TEXT NOT NULL,
    дата_окончания TEXT NOT NULL,
    цена REAL NOT NULL
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS Бронирования (
    id INTEGER PRIMARY KEY,
    id_туриста INTEGER NOT NULL,
    id_тура INTEGER NOT NULL,
    дата_бронирования TEXT NOT NULL,
    кол_во_туристов INTEGER NOT NULL,
    FOREIGN KEY (id_туриста) REFERENCES Туристы,
    FOREIGN KEY (id_тура) REFERENCES Туры
    )''')

with sq.connect('tourist.db') as con:
    cur = con.cursor()

    cur.execute('''INSERT INTO Туристы VALUES
        (1, 'Иван', 'Иванов', 'мужской', '1990-05-12', '+7 (999) 123-45-67', 'ivanov@mail.com'),
        (2, 'Петр', 'Петров', 'мужской', '1985-11-20', '+7 (999) 765-43-21', 'petrov@mail.com'),
        (3, 'Елена', 'Сидорова', 'женский', '1992-07-03', '+7 (999) 111-22-33', 'sidorova@mail.com'),
        (4, 'Александр', 'Кузнецов', 'мужской', '1978-12-15', '+7 (999) 234-56-78', 'kuznetsov@mail.com'),
        (5, 'Ольга', 'Иванова', 'женский', '1995-04-27', '+7 (999) 876-54-32', 'ivanova@mail.com'),
        (6, 'Сергей', 'Смирнов', 'мужской', '1989-09-02', '+7 (999) 999-99-99', 'smirnov@mail.com'),
        (7, 'Анна', 'Ковалева', 'женский', '1998-02-18', '+7 (999) 222-33-44', 'kovalyova@mail.com'),
        (8, 'Артем', 'Морозов', 'мужской', '1987-06-30', '+7 (999) 111-11-11', 'morozov@mail.com'),
        (9, 'Наталья', 'Васильева', 'женский', '1991-11-09', '+7 (999) 444-55-66', 'vasilyeva@mail.com'),
        (10, 'Дмитрий', 'Соколов', 'мужской', '1984-03-24', '+7 (999) 777-88-99', 'sokolov@mail.com')''')

    cur.execute('''INSERT INTO Туры VALUES
    (1, 'Круиз по Средиземному морю', 'Италия', 'Рим', '2023-06-10', '2023-06-18', 80000),
    (2, 'Отдых на Бали', 'Индонезия', 'Денпасар', '2023-07-12', '2023-07-20', 100000),
    (3, 'Поход в горы Кавказ', 'Россия', 'Краснодар', '2023-08-15', '2023-08-23', 45000),
    (4, 'Горнолыжный курорт в Альпах', 'Франция', 'Шамони', '2024-01-15', '2024-01-22', 90000),
    (5, 'Сафари в Южной Африке', 'Южная Африка', 'Крюгер-Национальный парк', '2024-02-10', '2024-02-18', 120000),
    (6, 'Поход на Килиманджаро', 'Танзания', 'Аруша', '2024-03-15', '2024-03-26', 150000),
    (7, 'Экскурсия по Парижу', 'Франция', 'Париж', '2023-09-20', '2023-09-25', 60000),
    (8, 'Культурный тур по Риму', 'Италия', 'Рим', '2023-10-08', '2023-10-14', 75000),
    (9, 'Каникулы в Малибу', 'США', 'Малибу', '2023-11-12', '2023-11-22', 180000),
    (10, 'Сноубординг в Канаде', 'Канада', 'Банф', '2024-01-02', '2024-01-09', 110000)''')

    cur.execute('''INSERT INTO Бронирования VALUES
    (1, 3, 1, '2023-05-15', '2023-05-22'),
    (2, 1, 2, '2023-07-01', '2023-07-08'),
    (3, 4, 5, '2023-06-10', '2023-06-18'),
    (4, 2, 8, '2023-08-22', '2023-08-29'),
    (5, 7, 10, '2023-07-14', '2023-07-21'),
    (6, 9, 3, '2023-09-01', '2023-09-08'),
    (7, 6, 9, '2023-06-25', '2023-07-02'),
    (8, 2, 5, '2023-05-01', '2023-05-08'),
    (9, 8, 4, '2023-07-28', '2023-08-04'),
    (10, 10, 1, '2023-08-10', '2023-08-17')''')

with sq.connect('tourist.db') as con:
    cur = con.cursor()
    cur.execute("")
#   SELECT * FROM tourists;
#   SELECT * FROM tours ORDER BY price DESC;
#   SELECT * FROM bookings WHERE city = 'заданный город';
#   SELECT tourists.* FROM tourists INNER JOIN bookings ON tourists.tourist_id = bookings.tourist_id WHERE booking_date BETWEEN 'начало периода' AND 'конец периода';
#   SELECT tours.*, countries.country_name, cities.city_name FROM tours INNER JOIN cities ON tours.city_id = cities.city_id INNER JOIN countries ON cities.country_id = countries.country_id;
#   SELECT * FROM tourists WHERE gender = 'женский' AND birth_date > '1990-01-01';
#   SELECT * FROM tours WHERE price > 5000;
#   SELECT tourists.* FROM tourists INNER JOIN bookings ON tourists.tourist_id = bookings.tourist_id WHERE bookings.tour_id = 'конкретный тур';
#   SELECT tourists.* FROM tourists INNER JOIN bookings ON tourists.tourist_id = bookings.tourist_id INNER JOIN tours ON bookings.tour_id = tours.tour_id WHERE tours.date = 'указанная дата';
#   SELECT * FROM tourists WHERE phone_number LIKE '+7%';

with sq.connect('tourist.db') as con:
    cur = con.cursor()
    cur.execute("")
#   UPDATE Tour SET start_date = '2023-05-01' WHERE id = 1;
#   UPDATE Tour SET price = 1500 WHERE id = 7;
#   UPDATE Tourist SET phone_number = '+1 (555) 123-4567' WHERE id = 5;
#   UPDATE Booking SET booking_date = '2023-04-05' WHERE id = 3;
#   UPDATE Booking SET number_of_tourists = 3 WHERE id = 8;
#   UPDATE Tour SET end_date = '2023-08-31' WHERE id = 2;
#   UPDATE Tourist SET email = 'new_email@example.com' WHERE id = 1;
#   UPDATE Tour SET start_date = '2023-06-15' WHERE id = 4;
#   UPDATE Tour SET start_date = '2023-05-01' WHERE country = 'Испания';
#   UPDATE Tour SET price = 1500 WHERE name = 'Греция-отдых на море';
#   UPDATE Tour SET start_date = '2023-06-01' WHERE name = 'Испания-путешествие по городам';
#   UPDATE Booking SET number_of_tourists = 3 WHERE id = 1002;
#   UPDATE Tourist SET phone_number = '+1 (123) 456-7890' WHERE id = 2001;
#   UPDATE Tour SET start_date = '2024-07-01' WHERE price < 2000;
#   UPDATE Tourist SET email = 'new_email@example.com' WHERE country = 'Россия';
#   UPDATE Booking SET start_date = '2023-08-15' WHERE number_of_tourists > 2;
#   UPDATE Booking SET tour_name = 'Египет-отдых на курорте' WHERE tour_id = 1003.

with sq.connect('tourist.db') as con:
    cur = con.cursor()
    cur.execute("")
#   DELETE FROM bookings WHERE tourist_id=1;
#   DELETE FROM bookings WHERE tour_id=2;
#   DELETE FROM bookings WHERE booking_date='YYYY-MM-DD';
#   DELETE FROM tourists WHERE id IN (SELECT tourist_id FROM bookings WHERE tour_id=3);
#   DELETE FROM bookings WHERE tourist_phone='phone_number';
#   DELETE FROM bookings WHERE tourist_email='email_address';
#   DELETE FROM bookings WHERE tour_start_date>'YYYY-MM-DD';
#   DELETE FROM tourists WHERE id IN (SELECT tourist_id FROM bookings WHERE tour_country='country_name');
#   DELETE FROM bookings WHERE tour_end_date<'YYYY-MM-DD';
#   DELETE FROM bookings WHERE tour_price='price_value';
