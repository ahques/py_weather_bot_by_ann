import json # импорт библиотеки для работы с форматов json


def weather_info(weather):
    current_weather = json.loads(weather.text) # полученные данные переводим в json формат
    if current_weather['cod'] == '404': # Если в ответе нет города, то это значит ошибку
        result = 'Город не найден. Попробуйте еще раз.' # Отдаем ошибку в bot_weather_api
    else: # перебор файла и извлечениие нужных значений
        description = current_weather['weather'][0]['description']
        temp = round(current_weather['main']['temp'] - 273.15)
        feels_like = round(current_weather['main']['feels_like'] - 273.15)
        clouds = current_weather['clouds']['all']
        wind_speed = current_weather['wind']['speed']
        # записываем значение в красивый ответ
        result = ('Погода: ' + str(description) + '\n' 
                  'Температура: ' + str(temp) + ' °C \n'
                  'Ощущается как: ' + str(feels_like) + ' °C \n'
                  'Облачность: ' + str(clouds) + '%\n'
                  'Скорость ветра: ' + str(wind_speed) + 'м/с\n')
    return result # Отдаем ответ в bot_weather_api

