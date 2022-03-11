import sqlite3

conn = sqlite3.connect('bookings.db')
cur = conn.cursor()


# sql = f'CREATE TABLE bookings(id INT PRIMARY KEY, docfio TEXT, cabinet TEXT, patfio TEXT, palata INT, time TEXT)'


def get_by_palata(n: str):
    cur.execute(f"SELECT * FROM bookings WHERE palata={n};")
    res = cur.fetchall()
    for result in res:
        print(result)


def get_doc_info():
    cur.execute(f"SELECT * FROM bookings;")
    res = cur.fetchall()
    for result in res:
        print(result)


cur.execute("SELECT * FROM doctors;")
one_result = cur.fetchall()
for result in one_result:
    print(result)

buks = [(1, "Максимцева Инна Юрьевна", "200", "Ланова Александра Ивановна", "305", "8:30"),
        (2, "Смирнов Павел Андреевич", "208", "Лакова Мария Максимовна", "305", "12:10"),
        (3, "Айболитов Иван Сергеевич", "208", "Лакова Мария Максимовна", "305", "10:00"),
        (4, "Симато Олег Павлович", "203", "Думенко Кирилл Николаевич", "305", "11:15"),
        (5, "Имаренко Алла Ивановна", "220", "Тюмима Инна Валерьевна", "305", "12:15"),
        (6, "Петров Иван Петрвич", "202", "Лакова Максим Алексеевич", "305", "9:15"),
        ]

#for b in buks:
    #sql = f'INSERT INTO bookings VALUES ({b[0]}, \"{b[1]}\", \"{b[2]}\", \"{b[3]}\",\"{b[4]}\",\"{b[5]}\");'
    #print(sql)
    #cur.execute(sql)
    #conn.commit()
# pass
#sql = f'DELETE FROM doctors WHERE id=398640724;'
#print(sql)
#cur.execute(sql)
#conn.commit()

print('-' * 20)
get_doc_info()