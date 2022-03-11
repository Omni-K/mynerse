from __future__ import print_function #v verx koda
from decimal import Decimal #v verx koda
from datetime import datetime, date, timedelta #v verx koda
import mysql.connector #v verx koda

user = 'cipherqu_du'
passw = '123456Qwerty'
host = 'venera.lite-host.in'
db = 'cipherqu_du'

# Подключиться к серверу MySQL
cnx = mysql.connector.connect(user=user, database=db, host=host, password=passw)

# Получить два буферизованных курсора
curA = cnx.cursor(buffered=True)

# Запрос для получения сотрудников, присоединившихся в период, определяемый двумя датами
query = ( "SELECT * FROM `patients`")


# Выберите сотрудников, получающих повышение
curA.execute(query)

# Перебираем результат
for entry in curA:
  print(entry)

 # Зафиксировать изменения
  cnx.commit()

cnx.close()
