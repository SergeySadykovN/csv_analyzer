import os
import json
import csv


class PriceMachine:

    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

    def load_prices(self, directory):
        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт

            Допустимые названия для столбца с ценой:
                розница
                цена

            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''

        self.data = []
        for filename in os.listdir(directory):
            if filename.endswith('.csv') and 'price' in filename.lower():
                with open(os.path.join(directory, filename), 'r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    print(str(reader))

    def _search_product_price_weight(self, headers):
        '''
            Возвращает номера столбцов
        '''

    def export_to_html(self, fname='output.html'):
        ''' result =
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''

    def find_text(self, text):
        pass

    def user_input(self, directory):
        self.load_prices(directory)

        while True:
            find_text_value = input('Что найти (или "exit") ?: ')
            if find_text_value.lower() == 'exit':
                print('Поиск завершен')
                break
            self.find_text(find_text_value)




if __name__ == '__main__':
    pm = PriceMachine()
    local_directory = os.path.dirname(os.path.abspath(__file__))
    pm.user_input(local_directory)



