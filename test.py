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
