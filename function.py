# nonlocal  # позволяет использовать переменную из объемлящей функции
# global  # позволяет использовать глобальную переменную вместо создания локальной

listed = [12, 21, 30, 46, 55]


# help() # пишем внутри имя функции и получаем манул по ней
def fun(x):
	return x % 10, x // 10 % 10  # возвращает картеж!


sorted(listed, key=fun, reverse=False)  # принимает итерируемую последовательность
# возвращает отсортированную копию listed (всегда список)
# key - применяет функцию к итеру, и сортирует по этой функции
# 1)встроенные фунеции
# 2)собственные функции
# 3)встроенные методы
# 4)анонимные фунеции типо lambda
sorted(listed, key=abs)  # сортирует по модулю
sorted('fkfjshdfHFKJDKF', key=str.lower)  # можно применять методы, надо вызвать тип.метод

ord('A')  # принимает чар, возвращает код аски
chr(65)  # принимает код аски, возвращает чар

abs(-7)  # принимает число, возвращает его модуль
max(1, 2)  # принимает значения, возвращает максимальное
min(1, 2)  # принимает значения, возвращает минимальное
sum([1,2]) # Поигимаеь коллекцию и возвращает сумму всех элементов
all([1,2,3]) # принимает коллекцию, возвращает True если все булевы Тру
any([0,1,3]) # принимает коллекцию, возвращает True если хотябы 1 булево тру

enumerate(listed, 10)  # принимает коллекцию,
# возвращает картеж из номера+значение, можно задать старт после запятой

callable([]) # Принимает любой объект и проверяет является ли он вызываемым,возвращает True

d = iter(listed)  # создает итерируемы объект, который можно проитерировать 1 раз
c = (i for i in range(10))  # создает объект типа генератор, итерируемая последовательность
# итераторы не занимают много памяти и очень быстро обрабатываются
# к генератору нельзя применить функцию len, нельзя взять по индексу
next(d)  # вызывает следующую итерацию итерируемого объекта


def gen_fun():  # функция генератор которая возвращает по 1 значению и замораживает остальные
	for i in [10, 12, 15]:
		yield i  # на подобии ретерна, возвращает значение и запоминает на чем остановился


# следующий вызов фунеции начнётся после строки yield


# помогает экономить память

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
# class map(object)
# |	map(func, iterable) --> map object # принимает функцию и итерабельную последовательность
# на каждый итер, применяет фунецию и возвращает результат

a = [-1, 2, -3, 4, -5, -10]
b = map(abs, a)  # принял функцию абс(модуль числа) и список
# b - будет итерируемая последовательность, можно обернуть в list и получится список
c = [abs(i) for i in a]  # тоже самое
# d = list(map(int, input().split()))
# принимает инпут, преобразовывает в инт, разбиваю по пробелу, преобразует в список


# class filter(object)
# | filter(func, iterable) --> filter object #  принимает функцию и итерабельную последовательность
# применяет функцию на каждый итер, и возвращает ответ если он True
p = list(filter(abs, [1, -1, 0, 3]))
d = {
	'moscow': 800,
	'boston': 200,
	'LA': 500,
	"SF": 400,
}
u = list(filter(lambda x: d[x] > 400, d))
# обходит словарь по значению, и фильтрует все больше 400, возвращая ключи
print(u)
a = [5, 6, 7, 8, 9]
b = [100, 200, 300, 400]
c = 'abcdfgh'
# zip (iter1 [iter2 [...]]) --> zip object
# создает картежи из итерируемых последовательностей
# сама определяет наименьшую длинну последовательности
rez = list(zip(a, b, c))
print(rez)
# for t1,t2,t3 in zip(a, b, c): # можно обойти в цикле
# 	print(t1,t2,t3)
