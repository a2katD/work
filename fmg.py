import os
import shutil
import datetime


def create_file(name, text=None):  # создает новый файл
	with open(name, "w", encoding='utf-8') as f:
		if text:
			f.write(text)


def create_folder(name):  # создает новую папку
	try:
		new_path = os.path.join(os.getcwd(), name)
		os.mkdir(new_path)
	except FileExistsError:
		print("folder already exists")


def get_list(folders_only=False, string=False):  # печатает список файлов и папок
	result = os.listdir(path=".")
	if folders_only:
		result = [f for f in result if os.path.isdir(f)]
	if string:
		print(result)
	else:
		for i in result:
			print(i)


def delete_file(name, sure=False):  # удаляет файл
	if os.path.isdir(name):
		if sure:
			new_path = os.path.join(os.getcwd(), name)
			shutil.rmtree(new_path)
		else:
			try:
				os.rmdir(name)
			except:
				print("folder is not empty")
	else:
		os.remove(name)


def copy_file(name, new_name):  # копирует файл или папку
	if os.path.isdir(name):
		try:
			shutil.copytree(name, new_name)
		except FileExistsError:
			print("Папка уже существует")
	else:
		shutil.copy(name, new_name)


def save_info(message='No message'):  # сохраняет логи
	current_time = datetime.datetime.now()
	result = f'{current_time} - {message}'
	with open('log.txt', "a", encoding='utf-8') as f:
		f.write(result + '\n')


if __name__ == '__main__':
	create_file('text.dat', "say my name")
	create_folder('new_f')
	get_list(folders_only=True)
	delete_file('text.dat')
	copy_file('new_f', 'new_d')
	copy_file('text.dat', 'new_file.dat')
	save_info('txt')
