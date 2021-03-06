# Сериализация
# Это процесс преобразования объекта в поток байтов для
# сохранения или передачи в память, базу данных или файл
# Обратный процесс - десериализация
#
# Применяется при
# сохранении объекта в файл
# сохранении объекта в базу данных
# передача объекта по сети
#
# Модуль Pickle
# dump - сохранине объекта в файл
# dumps - преобразование объекта в байты
# load - загрузка объекта их файла
# loads - загрузка объекта из набора байт
import pickle

person = {'name': 'Maxim', 'phone': "[123,345]"}
with open('preson.dat', 'wb') as f:  # открываем файл и сохраняем в переменную
	pickle.dump(person, f)  # передаем объект который сохраняем
# затем передаем файл куда сохраняем
f.close()
with open('preson.dat', 'rb') as f:
	person = pickle.load(f)  # записываем в переменную данные из файла
print(person)

# Формат json - (JavaScript Object NOtation)
# текстовый формат обмена данными, основаннный на JavaScript
# Аналогичен набору словарей, списков, простых типо данных в Питоне
# Но является просто текстом(строкой)
#
# Применяется для хранения и передачи данных, чаще всего используется в WEB разработке
# а так же для передачи данных по протоколу http
#
# dump - сохранине объекта в файл
# dumps - преобразование объекта в json
# load - загрузка объекта их файла
# loads - загрузка объекта из формата  в json

import json

friends = [
	{'name': 'Max', 'age': '23', 'phone': [123, '456']},
	{'name': 'Leo', 'age': '42'}
]
json_friends = json.dumps(friends) # Преобразовывает list in str
friends2 = json.loads() # преобразовывает str in list
