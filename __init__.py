import sqlite3 as sq
from data import *

with sq.connect('ЗАРПЛАТА.sqlite') as con:
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS анкета")
    cur.execute("DROP TABLE IF EXISTS 'Больничные листы'")
    cur.execute("""CREATE TABLE IF NOT EXISTS анкета (
    id INTEGER PRIMARY KEY,
    имя TEXT,
    фамилия TEXT,
    дата_рождения INTEGER,
    пол INTEGER,
    дата_найма INTEGER,
    должность TEXT,
    отдел TEXT,
    базовая_ставка REAL
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS "Больничные листы" (
    id INTEGER PRIMARY KEY,
    дата_начала INTEGER,
    дата_окончания INTEGER,
    причина TEXT,
    диагноз TEXT,
    оплачен INTEGER,
    id_сотрудника INTEGER,
    FOREIGN KEY (id_сотрудника) REFERENCES анкета(id) ON DELETE CASCADE ON UPDATE CASCADE
    )""")

with sq.connect('ЗАРПЛАТА.sqlite') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO анкета VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", info_form)
    cur.executemany("INSERT INTO 'Больничные листы' VALUES (?, ?, ?, ?, ?, ?, ?)", info_list)

with sq.connect('ЗАРПЛАТА.sqlite') as con:
    cur = con.cursor()
    print(1, *cur.execute("SELECT имя, должность FROM анкета").fetchall(), sep='\n')
    print()
    print(2, *cur.execute("SELECT имя, базовая_ставка FROM анкета").fetchall(), sep='\n')
    print()
    print(3, *cur.execute("SELECT имя FROM анкета WHERE отдел = 'IT'").fetchall(), sep='\n')
    print()
    print(4, *cur.execute("SELECT имя FROM анкета WHERE дата_найма > 22").fetchall(), sep='\n')
    print()
    print(5, *cur.execute("SELECT id FROM 'Больничные листы' WHERE id_сотрудника = 42").fetchall(), sep='\n')
    print()
    print(6, *cur.execute("SELECT id FROM 'Больничные листы' WHERE оплачен").fetchall(), sep='\n')
    print()
    # print(7, *cur.execute("SELECT * FROM ").fetchall(), sep='\n')
    # print()
    # print(8, *cur.execute("SELECT * FROM ").fetchall(), sep='\n')
    # print()
    # print(9, *cur.execute("SELECT * FROM ").fetchall(), sep='\n')
    # print()
    # print(10, *cur.execute("SELECT * FROM ").fetchall(), sep='\n')
    # print()
    # print(11, *cur.execute("SELECT * FROM ").fetchall(), sep='\n')
    # print()
    # print(12, *cur.execute("SELECT * FROM ").fetchall(), sep='\n')
    # print()
    # print(13, *cur.execute("SELECT * FROM ").fetchall(), sep='\n')
    # print()
    # print(14, *cur.execute("SELECT * FROM ").fetchall(), sep='\n')
    # print()
    # print(15, *cur.execute("SELECT * FROM ").fetchall(), sep='\n')
    # print()
