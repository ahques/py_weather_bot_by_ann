from aiogram.dispatcher.filters.state import State, StatesGroup

# Машины состояний

class WeatherLocation(StatesGroup):
    waiting_for_city = State()


class ChoseDate(StatesGroup):
    wating_for_month = State()
    wating_for_day = State()

class ConverterState(StatesGroup):
    wating_first_valute = State()
    wating_amount = State()
    wating_second_valute = State()