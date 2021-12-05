import datetime # библиотека для работы с датой и временем

import requests
from datetime import date
import bot_date_fact_result

def today_fact():
    day = date.today().day # получаем сегодняшний день
    month = date.today().month # месяц
    # отправляем запрос
    get_fact_today = requests.get('http://numbersapi.com/' + str(month) + '/'
                                  + str(day) + '/date?json')
    result = bot_date_fact_result.fact_rsult(get_fact_today) # отправляем полученные данные на перевод
    return result

def another_day_fact(month, day):
    try:
        # если пользователь сам ввел месяц и день, то проверяем дату на существование
        # в каждом году одинаковое кол-во дней в меясцах, кроме высокосного - берем любой такой за основу
        # проверяем только меясц и день
        datetime.datetime(year=2012, month=int(month), day=int(day)) #если ок, то делаем запрос
        get_fact_today = requests.get('http://numbersapi.com/' + str(month) + '/'
                                      + str(day) + '/date?json')
        result = bot_date_fact_result.fact_rsult(get_fact_today)
        return result
    # еслии нет, то пишем ошибку.
    # значение ValueError - нужен для того, чтобы программа не вылетала и можно было сделать свои действия
    except ValueError:
        error_text = 'Неверная дата. Попробуйте снова'
        return error_text
