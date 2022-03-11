from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import sqlite3

conn = sqlite3.connect('bookings.db')
cur = conn.cursor()


def get_all():
    cur.execute(f"SELECT docfio, cabinet, patfio, palata, time FROM bookings;")
    return list(cur.fetchall())


class MainApp(MDApp):
   def build(self):
       # Определить экран
       screen = Screen()
       # Определить таблицу
       table = MDDataTable(
           pos_hint={'center_x': 0.5, 'center_y': 0.5},
           size_hint=(0.9, 0.9),
           check=True,
           use_pagination=True,
           rows_num=6,
           pagination_menu_height='240dp',
           pagination_menu_pos="auto",
           background_color=[1, 0, 0, 5],

           column_data=[  # Название колонок
               ("Врач", dp(30)),
               ("Кабинет", dp(20)),
               ("Пациент", dp(30)),
               ("Палата", dp(30)),
               ("Время", dp(30))
           ],
           row_data=get_all()
       )
       # Привязать таблицу
       table.bind(on_check_press=self.checked)
       table.bind(on_row_press=self.row_checked)

       self.theme_cls.theme_style = "Light"
       self.theme_cls.primary_palette = "BlueGray"
       # вернуть Builder.load_file('table.kv')
       # Добавить виджет таблицы на экран
       screen.add_widget(table)
       return screen

   # Функция проверки прессов
   def checked(self, instance_table, current_row):
       print(instance_table, current_row)

   # Функция для рядных прессов
   def row_checked(self, instance_table, instance_row):
       print(instance_table, instance_row)

MainApp().run()
