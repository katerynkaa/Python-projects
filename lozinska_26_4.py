import sys
from urllib.request import urlopen
import html.parser
import openpyxl
from openpyxl.styles import Font

class MeteoProgParser(html.parser.HTMLParser):
    AMOUNT_OF_DAYS_TO_LOAD = 5

    def __init__(self, *args):
        super().__init__(*args)
        self.entries = [{} for x in range(MeteoProgParser.AMOUNT_OF_DAYS_TO_LOAD)]
        self.current_entry_index = 0
        self.stop = False
        self.current_key = None
        self.move_next = False

    def handle_starttag(self, tag, attrs):
        if self.stop:
            return
        if self.has_class(attrs, 'dayoffMonth'):
            self.current_key = 'Day'
        if self.has_class(attrs, 'from'):
            self.current_key = 'Minimum temperature'
        if self.has_class(attrs, 'to'):
            self.current_key = 'Maximum temperature'
            self.move_next = True
        return super().handle_starttag(tag, attrs)

    def handle_data(self, data):
        if self.stop or self.current_key is None:
            return
        current_entry = self.get_current_entry()
        current_entry[self.current_key] = data.strip()
        self.current_key = None
        if self.move_next:
            self.move_next = False
            self.current_entry_index += 1
            if self.current_entry_index >= MeteoProgParser.AMOUNT_OF_DAYS_TO_LOAD:
                self.stop = True

        return super().handle_data(data)

    def get_current_entry(self):
        return self.entries[self.current_entry_index]

    def has_class(self, attrs, class_name):
        return class_name in next((attribute_value for (attribute_name, attribute_value) in attrs if attribute_name == 'class'), '').split(' ')

city_name = input('Enter city name (in English): ')

url = 'http://www.meteoprog.ua/ru/weather/{city_name}'.format(city_name=city_name)
request = urlopen(url)
response = str(request.read(), encoding='utf8', errors='ignore')

parser = MeteoProgParser()
import codecs

parser.feed(response)

workbook = openpyxl.Workbook()
sheet = workbook.active

sheet.append(['Погода', city_name])
l = list(parser.entries[0].keys())
sheet.append(l)

for row in sheet.iter_rows(min_row=1, max_row=2, max_col=3):
    for cell in row:
        cell.font = Font(bold=True)

for entry in parser.entries:
    sheet.append(list(entry.values()))
workbook.save(filename='MeteoProg.xlsx')