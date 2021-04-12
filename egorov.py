################################################################
# 7.12 Замыкания
################################################################
# def main_func():
#     count = 0
#     def inner_funck():
#         nonlocal count
#         count += 1
#         return count
#     return inner_funck
# a = main_func()
# print(a())
# print(a())
##########
# def multiply(value):
#     def f(v):
#         return v * value
#     return f
#
# f_2 = multiply(2)
# print(f_2(5))
################################################################
# Функция таймер, может быть полезна например в игре майнкрафт #
################################################################
# from time import perf_counter, sleep
# def timer():
#     start = perf_counter()
#     def inner():
#         return (perf_counter() - start)
#     return inner
# timer = timer()
# timer()
# sleep(5)
# print(timer())

################################################################
# Декораторы
################################################################
from functools import wraps # Декоратор wraps сохраняет исходные значения имени и документации
# def decorator(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         print("Start decorator")
#         func(*args, **kwargs)
#         print("Stop decorator")
#     return inner
#
# @decorator # == (say = decorator(say))
# def say(*args, **kwargs):
#     """DOCUMENTATION"""
#     print("HW", *args, **kwargs)
# say(1,2,3)