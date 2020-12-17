# Сортировка перебором - возвращает отсортированную последовательность
def brute_force_sort(iter):
	for i in range(len(iter)):
		for j in range(len(iter)):
			if iter[i] < iter[j]:
				iter[i], iter[j] = iter[j], iter[i]
	return (iter)


# Сортировка выбором - возвращает отсортированную последовательность
# def selection_sort(iter):
# 	step = len(iter)
# 	while step >= 0:
# 		big = iter[0]
# 		for i in range(step):
# 			if iter[i] > big:
# 				num = i
# 				big = iter[i]
# 		iter[step - 1], iter[num] = iter[num], iter[step - 1]
# 		step -= 1
# 	return iter


# Сортировка пузырьком - возвращает отсортированную последовательность
def bubble_sort(iter):
	for i in range(len(iter) - 1):
		for j in range(len(iter) - i - 1):
			if iter[j] > iter[j + 1]:
				iter[j], iter[j + 1] = iter[j + 1], iter[j]
	return (iter)


# Линейный поиск - возвращает индекс искомого числа, -1 если нет
def linear_search(iter, key):
	for i in range(len(iter)):
		if iter[i] == key:
			return i
	return -1


# Бинарный поиск - возвращает индекс искомого числа, -1 если нет
def binary_search(iter, key):
	mid = len(iter) // 2
	left = 0
	right = len(iter) - 1
	while iter[mid] != key and left <= right:
		if key > iter[mid]:
			left = mid + 1
		else:
			right = mid - 1
		mid = (left + right) // 2
	if left > right:
		return -1
	else:
		return mid
