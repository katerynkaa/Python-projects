import re
from urllib.request import Request, urlopen
import datetime

def day_of_week(date):
    c = date.split(".")
    r = datetime.datetime(int(c[2]), int(c[1]), int(c[0])).weekday()
    return r

def date_span(date_given, start, end):
    TODAY_CHECK = datetime.datetime.strptime(str(date_given), "%d.%m.%Y")
    start = datetime.datetime.strptime(str(start), "%d.%m.%Y")
    end = datetime.datetime.strptime(str(end), "%d.%m.%Y")
    if start <= TODAY_CHECK <= end:
        return True
    else:
        return False


url = "https://www.flyuia.com/ua/ua/information/time-table-special-october-march"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
http_file = urlopen(req)

city1 = 'ТЕЛЬ-АВІВ'
city2 = 'КИЇВ'
date = '19.03.2022'

cities = r'<td>({c1}\s\-\s{c2}\s)</td>'.format(c1 = city1, c2 = city2)
flight = r'<td>(\w{2}\d{3})</td>'
days = r'<td>(\s(\d\,)+\d\s)</td>'
dates = r'<td>(\d{2}\/\d{2}\/\d{4}\s\-\s\d{2}\/\d{2}\/\d{4}\s)</td>'
time = r'<td>(\d{2}\:\d{2}\s\-\s\d{2}\:\d{2})</td>'
INFO = r'\n'.join([cities, flight, days, dates, time])

s = ''
for line in http_file:
    s += str(line, encoding='utf-8')

data = re.findall(INFO, s)

all_flights = []
data_needed = []
min_len = 10
for k in range(len(data)):
    for i in range(len(data[k])):
        if i == 0 or i == 1 or i == 2 or i == len(data[k])-1 or len(data[k]):
            if '\t' in data[k][i]:
                data_conv = ''
                for j in range(len(data[k][i])-1):
                    if data[k][i][j] != ',' and data[k][i][j] != '/':
                        data_conv+=data[k][i][j]
                    if data[k][i][j] == '/':
                        data_conv += '.'
                data_needed.append(data_conv)
                data_conv = ''
            else:
                data_needed.append(data[k][i])
    all_flights.append(data_needed)
    data_needed = []
#print(all_flights)

for i in range(len(all_flights)):
    start = all_flights[i][-2][0:10]
    end = all_flights[i][-2][-10:]
    if date_span(date, start, end) == True:
        ch = day_of_week(date)
        for k in all_flights[i][2]:
            if str(ch) == k:
                print('Є квитки на рейс {r} із {c1} до {c2} на {d} виліт та прибуття: {t}'.format(r = all_flights[i][1], c1 = city1, c2 = city2, d = date, t = all_flights[i][-1]))

