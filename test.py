# def zero(s, E=2.7182818284590452353602875):
# 	if s == 0:
# 		print(int(round(E, s)))
# 	else:
# 		print(round(E, s))
#
#
# s = int(input())
# zero(s)

# A, B, C = map(int, input().split())
# return ''.join(s_list)
# s_list = s.split('')
#
# a = []
# n = int(input())
# for i in range(n):
# 	a.append([0] * n)

# def prost(num):
# 	flag = True
# 	if num == 2:
# 		return True
# 	for i in range(num):
# 		if i == 0 or i == 1:
# 			continue
# 		if i != 0 and i != 1 and (num % i) == 0:
# 			flag = False
# 	return flag
#
# M, N = map(int, input().split())
# count = 0
# for i in range(M, N + 1):
# 	if prost(i):
# 		print(i)
# 		count +=1
# 	if count == 0:
# 		print('Absent', end='')

# if prost(A):
# 	s += A
# if prost(B):
# 	s += B
# if prost(C):
# 	s += C
# print(s)
# if prost(s) == True:
# 	print('Yes')
# else:
# 	print('No')

# def update(mass, l, r, x):
# 	for i in range(l, r + 1):
# 		mass[i - 1] = x
#
#
# def add(mass, l, r, x):
# 	for i in range(l, r + 1):
# 		mass[i - 1] = mass[i - 1] + x
#
#
# def rsq(mass, l, r):
# 	s = 0
# 	for i in range(l, r + 1):
# 		s += mass[i - 1]
# 	return s
#
#
# def rmq(mass, l, r):
# 	m = mass[l - 1]
# 	for i in range(l, r + 1):
# 		if mass[i - 1] < m:
# 			m = mass[i - 1]
# 	return m
#
#
# n = int(input())
# mass = list(map(int, input().split()))
# m = int(input())
# get = lambda mass, i: mass[i - 1]
# for y in range(m):
# 	params = list(input().split())
# 	if params[0] == 'rsq':
# 		print(rsq(mass, int(params[1]), int(params[2])))
# 	if params[0] == 'update':
# 		update(mass, int(params[1]), int(params[2]), int(params[3]))
# 	if params[0] == 'rmq':
# 		print(rmq(mass, int(params[1]), int(params[2])))
# 	if params[0] == 'add':
# 		add(mass, int(params[1]), int(params[2]), int(params[3]))
# 	if params[0] == 'get':
# 		print(get(mass, int(params[1])))

# kolvo = int(input())
# mass = list(map(int, input().split()))
# for i in mass:
# 	if i == 0:
# 		continue
# 	if mass[i] < mass[i - 1]:
# 		mass.pop(i - 1)
# print(mass)
# # 2 5 3 4 6 1

import os


def create_dir(num):
    for i in range(1, num + 1):
        new_dir = os.path.join(os.getcwd(), ("dir_" + str(i)))
        os.mkdir(new_dir)


def delete_dir(num):
    for i in range(1, num + 1):
        new_dir = os.path.join(os.getcwd(), ("dir_" + str(i)))
        os.rmdir(new_dir)


# os.name  # имя операционной системы
# os.chdir  # смена текущей директории
# os.getcwd()  # возвращает текущую директорию
# os.mkdir()  # создание дипректории
# os.path  # вложенный модуль для работы с путями
# os.listdir(path=".") # возвращает содержимое директории
# s = "123sss"
# bs = b"123sss"
# print(bs[1])
#
# import random
#
# print([random.randint(1, 101) for i in range(10)])
# print([i ** 2 for i in list(map(int, input().split()))])

# basket = ['apple', 'orange', 'salt', 'salat']
# chest = ['orange', 'juice', 'butter', 'apple', 'suggar']
# a = [i for i in basket if i in chest]
# print(a)
# rand = [1, 7, 55, 4, 99, 3, 11, 6, 7, 99, 1, 65, 4, 6, 7, 5, 69, 19, 79, -1, 4, -12, -48, -24, -5]
# b = [i for i in rand if i % 3 == 0 and i % 4 != 0 and i > 0]
# print(b)
# import  math
# def sqrt(listed):
# 	new_list = [math.sqrt(num) if num > 0 else num for num in listed]
#
#
# print(sqrt(a))
# print(a)
#
# def er(a):
# 	if a == 13:
# 		raise ValueError("число 13 плохое")
# 	return a**2
# print(er(13))
# listed = [1,2,3,4,5,7,11,15,19]
# d = iter(listed) # создает итерируемы объект, который можно проитерировать 1 раз
# # for i in d:
# 	# print(i)
# print("123\r456")

# f = open("numbers.txt.")
# num = f.readlines()
# print(num)
# for i in range(len(num)):
#     num[i] = int(num[i].replace("\n", ""))
# print(num)
# c = 0
# s = 0
# for i in num:
#     if i > 99 and i < 1000:
#         c += 1
#     if i > 9 and i < 100:
#         s += i
# print(c)
# print(s)

# <<<<<<< HEAD
# class Error:
#     def __init__(self, *args):
#         self.my_list = []
#
#     def my_input(self):
#         while True:
#             try:
#                 val = int(input('Введите значения и нажимайте Enter - '))
#                 self.my_list.append(val)
#                 print(f'Текущий список - {self.my_list} \n ')
#             except:
#                 print(f"Недопустимое значение - строка и булево")
#                 y_or_n = input(f'Попробовать еще раз? Y/N ')
#
#                 if y_or_n == 'Y' or y_or_n == 'y':
#                     print(try_except.my_input())
#                 elif y_or_n == 'N' or y_or_n == 'n':
#                     return f'Вы вышли'
#                 else:
#                     return f'Вы вышли'
#
# try_except = Error(1)
# print(try_except.my_input())
# =======
# a = [1,12,2,1,1,1,1,1,1,31,321,3,13,132,1,321]
# a = sorted(list(set(a)))
# print(a)
#
#
# >>>>>>> ef7bbbf100c4d15e637efa0c1e6049eebd8a6457

# n, m = map(int, input().split())
n = int(input())
string = input()
i = k = 0
while k != -1 and i != -1:
    while i != -1:
        i = string.find('01')
        if i != -1:
            string = string[:i] + string[i+2:]
            k = 0
    while k != -1:
        k = string.find('10')
        if k != -1:
            string = string[:k] + string[k+2:]
            i = 0
print(len(string))