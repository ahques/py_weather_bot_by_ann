import requests # библиотека для отправки запросов к сайтам
import bot_weather_result # отправка результата на обработку в другой модуль

apikey = 'db84cd3f41c31455eaf61c8be6d95a60' # API ключ для openweathermap.org

def weather_city(city):
    get_weather = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid='
        + apikey + '&lang=ru') # Отправляем запрос на погоду в  нужном городе
    result = bot_weather_result.weather_info(get_weather) # полученные данные в модуль на обработку
    return result # отдаем результат в bot_main
#для теста
#weather_city('Moscow')



