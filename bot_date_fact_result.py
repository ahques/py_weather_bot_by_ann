import json
from googletrans import Translator # библиотека для перевода

translator = Translator()
# переводим полученный текст
def fact_rsult(info):
    fact = json.loads(info.text)
    result = translator.translate(str(fact['text']), dest='ru')
    print(result.text)
    return result.text