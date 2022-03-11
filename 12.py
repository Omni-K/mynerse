from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import sqlite3

conn = sqlite3.connect('bookings.db')
cur = conn.cursor()


def get_by_palata(n: str):
    cur.execute(f"SELECT * FROM bookings WHERE palata={n};")
    return list(cur.fetchall())


rd = []
for r in get_by_palata("305"):
    rd.append((r[1], r[2], r[3], r[5]))


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
                ("Имя", dp(30)),
                ("Время", dp(30))
            ],
            row_data=rd
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
