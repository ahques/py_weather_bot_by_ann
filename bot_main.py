# ГЛАВНЫЙ ФАЙЛ, точка входа в программу
# Импортируем необходимые для работы библиотеки
from aiogram import Bot, types # импортируем из aiograma переменную, храняшюю переменную с токеном(Bot)
from aiogram.dispatcher import Dispatcher # импортируем диспатчер(отправщик наших сообщений пользователю)
from aiogram.utils import executor # импортируем executor, отправитель запросов на сервер телеграмма
from aiogram.dispatcher import FSMContext # импортируем машину состояний
from aiogram.contrib.fsm_storage.memory import MemoryStorage # бекенд для хранения инфы
# MemoryStorage - использует оперативную память, подойдет для небольших пороектов

# Ниже импортируем наши модули, чтобы иметь к ним доступ
import bot_converter # Конвертер валют
import bot_rates # Курсы валют
import bot_keyboards # Клавиатуры
import bot_date_fact # Факт о дате
import bot_weather_api # Погода
from bot_states import WeatherLocation as w_state # Импорт отдельной функции состояния (для удобства)
from bot_states import ChoseDate as n_state # аналогично
from bot_states import ConverterState as c_state # аналогично

token = '2100852287:AAFuEPQpSY0i6WpcPP8N-7dtu25pOwjIqVA' # Токен бота
# Передаем в бота токен, а также устанавливаем ParseMod.HTML для всех сообщений от бота (см. ниже пример)
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage()) # передаем в диспатчер бота и бекенд


async def set_commands(dp): # Функция для показа комманд в выпадающем меню
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Начальное меню'),
        types.BotCommand('weather', 'Погода'),
        types.BotCommand('valute', 'Валюта'),
        types.BotCommand('fact', 'Факт о дате'),
        types.BotCommand('help', 'Описание')
    ])
# Функция хелп, вызывается командой /help.
# В нее передается значение msg (message) - то есть '/help' - и машина состояний
async def help_func(msg: types.Message, state: FSMContext):
    # сбрасывает машину состояний (аналогично далее в коде)
    # Нужно, чтобы выйти из машины состояний при вводе комманды
    await state.finish()
    await msg.answer('Информационный бот info_bot_by_Ann ver 1.00\n'
                     'Список доступных комманд:\n'
                     '/start - Вызвать начальное меню\n'
                     '/weather - Узнать погоду\n'
                     '/valute - Актуальные курсы валют\n'
                     '/fact - События, которые произошли в этот день\n'
                     '/help - Вызвать это меню')
#types.Message - ожидаемый тип переменной для более подробного вывода ошибок, не влияет на работу
async def start_func(msg: types.Message, state: FSMContext): # Стартовая функция - главное меню
    await state.finish()
    # <b></b> - html код, делает текстжирным. За обработку отвечает ParseMod.HTML
    await msg.answer('<b>Привет!</b>',
                     reply_markup=bot_keyboards.keyboard_general_menu) # вывод клаиватуры

# Вызывается не коммандой в чат, срабатывает на определенный вызов (упрошенно)
# Это отслеживает call - в него передается значение вызова
async def weather_menu(call: types.CallbackQuery, state: FSMContext): #срабатывание на кнопку (колбек)
    await state.finish()
    await call.message.answer('<b>Выберите город</b>',
                              reply_markup=bot_keyboards.keyboard_weather_menu) # Меню погоды
async def weather_menu_m(msg: types.Message, state: FSMContext): #срабатываение на комманду в чат
    await state.finish()
    await msg.answer('<b>Выберите город</b>',
                              reply_markup=bot_keyboards.keyboard_weather_menu)
async def weather_city(call: types.CallbackQuery):
    # Отправляем значение кнопки (келбека) в функцию. Значение ранво названию города
    response = bot_weather_api.weather_city(call.data)
    await call.message.answer(call.data) # Пишем город ( передает знанчение кнопки)
    await call.message.answer(response) # Выдаем ответ
async def weather_another_city(call: types.CallbackQuery):
    await call.message.answer('<b>Введите название города:</b>',)
    await w_state.waiting_for_city.set() # Переводим бот в состояние стейтмашины
async def city_chosen_func(msg: types.Message, state: FSMContext):
    response = bot_weather_api.weather_city(msg.text) # Отправляем текст в функцию
    await msg.answer(response)
    await state.finish()

async def fact_menu(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('<b>Выберите дату</b>',
                              reply_markup=bot_keyboards.keyboard_fact_menu)
async def fact_menu_m(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer('<b>Выберите дату</b>',
                              reply_markup=bot_keyboards.keyboard_fact_menu)
async def today_fact(call: types.CallbackQuery):
    response = bot_date_fact.today_fact()
    await call.message.answer(response)
async def another_day_fact(call: types.CallbackQuery):
    await call.message.answer('<b>Введите месяц</b>')
    await n_state.wating_for_month.set()
async def chose_month(msg: types.Message, state:FSMContext):
    # сохраняем значение месяца под ключом chosen_month. Значение сохраняется по сути словаре
    await state.update_data(chosen_month=msg.text)
    await msg.answer('<b>Введите день</b>')
    await n_state.wating_for_day.set()
async def chose_day(msg: types.Message, state:FSMContext):
    data = await state.get_data() # вытаскимваем словарь из памяти
    month = data['chosen_month'] # извлекаем значение
    response = bot_date_fact.another_day_fact(month, msg.text)
    await msg.answer(response)
    await state.finish()

async def valute_menu(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer('<b>Операции с валютой</b>',
                              reply_markup=bot_keyboards.keyboard_valute_menu)
async def valute_menu_m(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer('<b>Операции с валютой</b>',
                              reply_markup=bot_keyboards.keyboard_valute_menu)
async def valute_today(call: types.CallbackQuery):
    response = bot_rates.rates_today()
    await call.message.answer(response)
async def converter_fv(call: types.CallbackQuery):
    await call.message.answer('<b>Выберите валюту</b>',
                              reply_markup=bot_keyboards.keyboard_valute)
    await c_state.wating_first_valute.set()
async def amount(msg: types.Message, state:FSMContext):
    await state.update_data(first_valute=msg)
    await msg.message.answer('<b>Введите сумму</b>')
    await c_state.wating_amount.set()
async def converter_sv(msg: types.Message, state:FSMContext):
    await state.update_data(amount=msg.text)
    await msg.answer('<b>Выберите валюту для конвертации</b>',
                     reply_markup=bot_keyboards.keyboard_valute)
    await c_state.wating_second_valute.set()
async def converter_result(msg: types.Message, state:FSMContext):
    second_val = msg['data']
    data = await state.get_data()
    first_val = data['first_valute']['data']
    amount = data['amount']
    response = bot_converter.valute_converter(first_val, amount, second_val)
    await msg.message.answer(response)
    await state.finish()

# Регистрируем все комманды, на которые срегирует бот
# register_message_handler - реагирование на команду в чате
# register_callback_query_handler - реагирование на колбек (колбек тут илет от нажатия кнопки)

# Если в чат пришла команда /start, то выполняется функция start_func,
# state='*' нужен для прерывания стейтамашины
dp.register_message_handler(start_func, commands='start', state='*')
dp.register_message_handler(weather_menu_m, commands='weather', state='*')
dp.register_message_handler(fact_menu_m, commands='fact', state='*')
dp.register_message_handler(valute_menu_m, commands='valute', state='*')
dp.register_message_handler(help_func, commands='help', state='*')

# если бот отловил текст weather, то выполянется функция weather_menu
dp.register_callback_query_handler(weather_menu, text='weather')
dp.register_callback_query_handler(weather_city, text='Москва')
dp.register_callback_query_handler(weather_city, text='Санкт-Петербург')
dp.register_callback_query_handler(weather_city, text='Новосибирск')
dp.register_callback_query_handler(weather_city, text='Екатеринбург')
dp.register_callback_query_handler(weather_city, text='Казань')
dp.register_callback_query_handler(weather_city, text='Нижний Новгород')
dp.register_callback_query_handler(weather_another_city, text='another_city')
#Если состояние стейтмашины перешло в w_state.waiting_for_city, то выполняется функция city_chosen_func
dp.register_message_handler(city_chosen_func, state=w_state.waiting_for_city)

dp.register_callback_query_handler(fact_menu, text='menu_btn_number_c')
dp.register_callback_query_handler(today_fact, text='today')
dp.register_callback_query_handler(another_day_fact, text='another_day', state='*')
dp.register_message_handler(chose_month, state=n_state.wating_for_month)
dp.register_message_handler(chose_day, state=n_state.wating_for_day)

dp.register_callback_query_handler(valute_menu, text='menu_btn_valute_c')
dp.register_callback_query_handler(valute_today, text='exc_rates_today')
dp.register_callback_query_handler(converter_fv, text='converter')
dp.register_callback_query_handler(amount, state=c_state.wating_first_valute)
dp.register_message_handler(converter_sv, state=c_state.wating_amount)
dp.register_callback_query_handler(converter_result, state=c_state.wating_second_valute)





async def on_startup(dp): # запускатея на старте, прописывается ниже
    await set_commands(dp) # а старте запускаем работу выпадающего меню

if __name__ == '__main__':
    # skip_updates=True - для того, чтобы бот не среагировал на команды,
    # которые были отпралвены в чат во время ег простоя (срегагирует только на последнюю)
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)


