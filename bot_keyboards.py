from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# Модуль для создания кнопок и клавиатур

#<editor-fold Меню>
menu_btn_weather = InlineKeyboardButton('Погода', callback_data='weather')
menu_btn_valute = InlineKeyboardButton('Курсы валют', callback_data='menu_btn_valute_c')
menu_btn_number = InlineKeyboardButton('Факты о датах', callback_data='menu_btn_number_c')

keyboard_general_menu = InlineKeyboardMarkup(row_width=1).add(menu_btn_weather,
                                                              menu_btn_valute,
                                                              menu_btn_number)
#</editor-fold>
#<editor-fold Погода>
weather_btn_moscow = InlineKeyboardButton('Москва', callback_data='Москва')
weather_btn_piter = InlineKeyboardButton('Санкт-Петербург', callback_data='Санкт-Петербург')
weather_btn_novosib = InlineKeyboardButton('Новосибирск', callback_data='Новосибирск')
weather_btn_ekat = InlineKeyboardButton('Екатеринубруг', callback_data='Екатеринбург')
weather_btn_kazan = InlineKeyboardButton('Казань', callback_data='Казань')
weather_btn_nijnov = InlineKeyboardButton('Нижний Новгород', callback_data='Нижний Новгород')
weather_btn_another = InlineKeyboardButton('Выбрать другой город', callback_data='another_city')

keyboard_weather_menu = InlineKeyboardMarkup(row_width=2).add(weather_btn_moscow,
                                                            weather_btn_piter,
                                                            weather_btn_novosib,
                                                            weather_btn_ekat,
                                                            weather_btn_kazan,
                                                            weather_btn_nijnov,
                                                            weather_btn_another)
#</editor-fold>

#<editor-fold Дата>
fact_btn_today = InlineKeyboardButton('Сегодня', callback_data='today')
fact_btn_another_day = InlineKeyboardButton('Выбрать другой день', callback_data='another_day')

keyboard_fact_menu = InlineKeyboardMarkup(row_width=2).add(fact_btn_today,
                                                             fact_btn_another_day)

#</editor-fold>

#<editor-fold Валюта>
valute_btn_today = InlineKeyboardButton('Актуальный курс', callback_data='exc_rates_today')
valute_btn_converter = InlineKeyboardButton('Конвертер', callback_data='converter')


keyboard_valute_menu = InlineKeyboardMarkup(row_width=1).add(valute_btn_today,
                                                               valute_btn_converter)

btn_rub = InlineKeyboardButton('Российский рубль', callback_data='RUB')
btn_usd = InlineKeyboardButton('Доллар США', callback_data='USD')
btn_eur = InlineKeyboardButton('Евро', callback_data='EUR')
btn_cny = InlineKeyboardButton('Китайский Юань', callback_data='CNY')
btn_gbp = InlineKeyboardButton('Фунт стерлингов', callback_data='GBP')
btn_byn = InlineKeyboardButton('Белорусский рубль', callback_data='BYN')
btn_dkk = InlineKeyboardButton('Датская крона', callback_data='DKK')
btn_kzt = InlineKeyboardButton('Казахстанский тенге', callback_data='KZT')
btn_try = InlineKeyboardButton('Турецкая лира', callback_data='TRY')
btn_uah = InlineKeyboardButton('Украинская гривна', callback_data='UAH')
btn_jpy = InlineKeyboardButton('Японска йена', callback_data='JPY')
btn_chf = InlineKeyboardButton('Швейцарский франк', callback_data='CHF')
btn_hkd = InlineKeyboardButton('Гонконгский доллар', callback_data='HKD')
btn_inr = InlineKeyboardButton('Индийская рупия', callback_data='INR')
btn_pln = InlineKeyboardButton('Польский злотый', callback_data='PLN')
btn_krw = InlineKeyboardButton('Вон Республики Корея', callback_data='KRW')
btn_brl = InlineKeyboardButton('Бразильский реал', callback_data='BRL')
btn_czk = InlineKeyboardButton('Чешская крона', callback_data='CZK')

keyboard_valute = InlineKeyboardMarkup(row_width=2).add(btn_rub, btn_usd,
                                                        btn_eur, btn_cny,
                                                        btn_gbp, btn_byn,
                                                        btn_dkk, btn_kzt,
                                                        btn_try, btn_uah,
                                                        btn_jpy, btn_chf,
                                                        btn_hkd, btn_inr,
                                                        btn_pln, btn_krw,
                                                        btn_brl, btn_czk)

#</editor-fold>



