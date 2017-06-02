name = input("Please input name: ")
if name == 'master':
	print('Hello Master')
	password = input('Please input password: ')
	if password == 'abc123':
		print('Access granted.')
	else:
		print('Wrong password!')
else:
	print('Invalid user!')