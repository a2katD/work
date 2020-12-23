import os
import sys


# os.name  # имя операционной системы
# os.chdir  # смена текущей директории
# os.getcwd()  # возвращает текущую директорию
# os.mkdir()  # создание дипректории
# os.path  # вложенный модуль для работы с путями
# os.listdir(path=".") # возвращает содержимое директории

# примеры использования
# new_path = os.path.join(os.getcwd(), "new")  # соединяет имя с учетом особенностей ОС
# os.mkdir(new_path)  # создает новую директорию
#os.chdir(new_path)  # переходим в новую директорию
# print(os.getcwd())  # печатаем текущую директорию


# sys.executable - путь к интерпретатору пайтон
# sys.exit() - выход из пайтон
# sys.platform информация об ОС
# sys.path - список путей поиска модулей
# sys.argv список аргументов командной строки
# for i in range(len(sys.path)):
#	print(sys.path[i])

f = open("lol.txt", "r") #открытие файла
#f.write("hello\n") # запись в файл
#f.writelines(['new1\n', 'new2\n']) # запись по строка, принимает список
#print(f.read()) # возвращает прочитанный файл
print(f.readlines()) # возвращает список из строк прочитанного
f.close() # закрывает файл

with open("lol.txt", "r") as f: #альтернативное откртие файлы, который сам закроется
	for line in f:
		print(line.replace('\n', ''))
strokabyt = "Hello МИР".encode('utf-8') # кодировка строки
print(strokabyt)
stroka = strokabyt.decode('utf-8')
print(stroka)