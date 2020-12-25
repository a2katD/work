# nonlocal  # позволяет использовать переменную из объемлящей функции
# global  # позволяет использовать глобальную переменную вместо создания локальной

listed = [12, 21, 30, 46, 55]

# help() # пишем внутри имя функции и получаем манул по ней

sorted(listed, reverse=False)  # возвращает отсортированную копию listed

ord('A')  # принимает чар, возвращает код аски
chr(65)  # принимает код аски, возвращает чар

abs(-7)  # принимает число, возвращает его модуль
max(1, 2)  # принимает значения, возвращает максимальное
min(1, 2)  # принимает значения, возвращает минимальное

enumerate(listed, 10)  # принимает коллекцию,
# возвращает картеж из номера+значение, можно задать старт после запятой

lam = lambda x, y: x + y  # лямбда - функция в 1 строку
lam2 = lambda x: True if x > 0 else False  # может быть 1 оператор иф
sorted(listed, key=lambda x: x % 10)  # пример сортировки по последней цифре

# генераторы списков - быстрый и компактный код
# _выражение_ for _переменная_ in _коллекция_
# что будет возвращено, for(пока) переменна in откуда брать значение переменной
listed = [i for i in "hello"]  # превращает строку в список по чарам
listed = [[i, j] for i in [1, 2] for j in [4, 5]]  # пример создания 2 мерного массива
listed = [i + j for i in [1, 2] for j in [4, 5] if i + j >= 6]  # можно добавлять условие
numbers = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
result = [i for i in numbers if i > 0]  # фильтрует список, только положительные
li = [(1, 'a'), (2, 'b'), (3, 'c')]  # список из картежей
result = {per[0]: per[1] for per in li}  # превращаем его в словарь
print(result)
###########################################################
list(map(int, input().split()))
# принимает инпут, преобразовывает в инт, разбиваю по пробелу
