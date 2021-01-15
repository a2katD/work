# Сортировка перебором - возвращает отсортированную последовательность
def brute_force_sort(iter, copy=False):
	if copy == True:
		copy = iter.copy()
	else:
		copy = iter
	for i in range(len(copy)):
		for j in range(len(copy)):
			if copy[i] < copy[j]:
				copy[i], copy[j] = copy[j], copy[i]
	return copy


# Сортировка пузырьком - возвращает отсортированную последовательность
def bubble_sort(iter, copy=False):
	if copy == True:
		copy = iter.copy()
	else:
		copy = iter
	for i in range(len(copy) - 1):
		for j in range(len(copy) - i - 1):
			if copy[j] > copy[j + 1]:
				copy[j], copy[j + 1] = copy[j + 1], copy[j]
	return (copy)

# Линейный поиск - возвращает True или False, при ключе index=True возвращает индекс искомого числа или -1 если его нет
def linear_search(iter, key, index=False):
	for i in range(len(iter)):
		if iter[i] == key:
			if index == True:
				return i
			else:
				return True
	if index == True:
		return -1
	else:
		return False


# Бинарный поиск - возвращает True или False, при ключе index=True возвращает индекс искомого числа или -1 если его нет
def binary_search(iter, key, index=False):
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
		if index == True:
			return -1
		else:
			return False
	else:
		if index == True:
			return mid
		else:
			return True
