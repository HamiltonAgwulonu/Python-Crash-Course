#Password checker
count = 3
password = 'indigo+05'
for password in range(3):
	login = input("Enter your password: ")
	count = count -1
	if login == password:
		print("Access granted!")
	elif count > 1:
		print("Wrong password! You have", count, "more attempts")
	elif count == 0:
		print("Your account is locked!")
	else:
		print("Wrong password! You have", count, "more attempt")