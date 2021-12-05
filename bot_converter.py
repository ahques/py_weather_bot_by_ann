import requests # импорт библиотеки для запросов к сайтам
import json # импорт библиотеки для работы с форматов json
# Конвертер валют
url = 'https://www.cbr-xml-daily.ru/daily_json.js' # адрес для запроса

def valute_converter(first_val, amount, second_val): # получаем валюуту 1, сумму и валюту 2
    get_currency = requests.get(url) # посылаем запрос и получаем в переменную данные
    data = json.loads(get_currency.text) # переводим данные в json
    # В данных нет рубля, так что задаем все значения для него вручную (если используется)
    if first_val == 'RUB':
        first_valute = 1
        name_fv = 'Российских рублей'
        f_nominal = 1
    else:
        # Вытаскиваем нужные данные из json
        first_valute = data['Valute'][first_val]['Value']
        name_fv = data['Valute'][first_val]['Name']
        f_nominal = data['Valute'][first_val]['Nominal']
    if second_val == 'RUB':
        second_valute = 1
        name_sv = 'Российских рублей'
        s_nominal = 1
    else:
        second_valute = data['Valute'][second_val]['Value']
        name_sv = data['Valute'][second_val]['Name']
        s_nominal = data['Valute'][second_val]['Nominal']
    # Формула для конвертации валюты
    convert = (float(first_valute) / float(f_nominal)) * float(amount) \
              / (float(second_valute) / float(s_nominal))
    # итоговое число, '{0:.4f}' - 4 занака после запятой
    f_con = '{0:.4f}'.format(convert)
    str_con = str(f_con)
    result = str(amount) + ' ' + name_fv + ' = ' + str_con + ' ' + name_sv # записываем ответ
    return result

# Использовал для теста
#valute_converter('USD', 100, 'KZT')