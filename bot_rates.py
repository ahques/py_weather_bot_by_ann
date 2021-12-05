import requests # импорт библиотеки для запросов к сайтам
import json # импорт библиотеки для работы с форматов json
from datetime import date # для работы с датой

url = 'https://www.cbr-xml-daily.ru/daily_json.js' # адрес сайта для запроса
# Получаем курсы валют. Можно добавить по желанию
def rates_today():
    get_valute = requests.get(url) # Отправляем запрос
    data = json.loads(get_valute.text) # данные из запроса в json
    # извлекаем нужные данные.
    # По аналогии добавить переменные, заменить за 'USD' на нужную валюту (из файла)
    usd = data['Valute']['USD']['Value']
    eur = data['Valute']['EUR']['Value']
    cny = data['Valute']['CNY']['Value']
    # Три строчки на получение сегодняшней даты для красивой запсии ответа
    # по умолчанию формат yyyy-mm-dd, поэтому берем по отдельности
    day = date.today().day
    month = date.today().month
    year = date.today().year
    result = ('Курс Цб РФ на ' + str(day) + '.' + str(month) + '.' + str(year) +
              '\n_________________________\n'
              'Доллар США = ' + str(usd) + ' ₽\n'
              'Евро = ' + str(eur) + ' ₽\n'
              'Китайский Юань = ' + str(cny) + ' ₽') # По аналогии добавить сюда
    return result # Отпралвяем ответ

