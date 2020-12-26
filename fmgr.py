import sys
import fmg
fmg.save_info('start')
try:
	command = sys.argv[1]
except:
	command = None

if command == 'list':
	try:
		params = sys.argv[2]
	except:
		fmg.get_list()
	else:
		if params == '-f':
			fmg.get_list(folders_only=True)
		elif params == '-s':
			fmg.get_list(string=True)
		elif params == '-fs' or '-sf':
			fmg.get_list(folders_only=True, string=True)
		else:
			print('Bad options')
elif command == 'create_file':
	try:
		name = sys.argv[2]
	except:
		print('File not found')
	else:
		try:
			text = sys.argv[3]
		except:
			fmg.create_file(name)
		else:
			fmg.create_file(name, text)
elif command == 'create_folder':
	try:
		name = sys.argv[2]
	except:
		print('File not found')
	else:
		fmg.create_folder(name)
elif command == 'delete':
	try:
		name = sys.argv[2]
	except:
		print('File not found')
	else:
		try:
			params = sys.argv[3]
		except:
			fmg.delete_file(name)
		else:
			if params == '-y':
				fmg.delete_file(name, sure=True)
			else:
				print('Bad options')
elif command == 'copy':
	try:
		name = sys.argv[2]
	except:
		print('File not found')
	else:
		try:
			new_name = sys.argv[3]
		except:
			print('Not name new file')
		else:
			fmg.copy_file(name, new_name)
elif command == 'help':
	print('list - список файлов и папок')
	print('create_file - создать файл')
	print('create_folder - создать папку')
	print('delete - удалить файл или папку')
	print('copy - копировать файл или папку')
else:
	print("Bad options")
fmg.save_info('stop')