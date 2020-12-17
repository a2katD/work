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

import random
