#ex(1)
# temp = 0
# while temp != -1000:
# 	temp = eval(input("Enter a temperature (-1000 to quit): "))
# 	if temp != -1000:
# 		print("In Fahrenheit that is", 9/5*temp+32)
# 	else:
# 		print("Bye")

#ex(2)
# from random import randint 
# secret_num = randint(1, 10)
# guess = 0
# while guess != secret_num:
# 	guess = eval(input("Guess the secret number: "))
# print("You finally got it!")

#ex(3)
#mimicing a for loop
# for i in range(10):
# 	print(i)

# i = 0
# while i < 10:
# 	print(i)
# 	i = i + 1

#ex(4)
# temp = eval(input("Enter a temperature in Celsius: "))
# if temp <- 273.15:
# 	print("That temperature is not possible.")
# else:
# 	print("In Fahrenheit, that is", 9/5*temp+32)

#ex(4) Improvement
# temp = eval(input("Enter a temperature in Celsius: "))
# while temp <-273.15:
# 	temp = eval(input("Impossible. Enter a valid temperature: "))
# print("In Fahrenheit, that is", 9/5*temp+32)



#ex(6)
# i = 0
# while i<50:
# 	print(i)
# 	i = i + 2
# print("Bye")


#Infinite Loops and the break statement.
# for i in range(10):
# 	num = eval(input("Enter number: "))
# 	if num < 0:
# 		break

# i = 0
# num = 1
# while i<10 and num>0:
# 	num = eval(input("Enter a number: "))

# while True:
# 	temp = eval(input(": "))
# 	if temp == -1000:
# 		print("Bye")
# 		break
# 	print(9/5*temp+32)


#The else statement
# for i in range(10):
# 	num = eval(input("Enter number: "))
# 	if num < 0:
# 		print("Stopped early")
# 		break
# else:
# 	print("User entered all ten values")


#ex(7)
#check if an integar number is prime
# while True:
# 	num = eval(input("Enter a number: "))
# 	if num <= 0:
# 		print("Bye")
# 		break
# 	for i in range(2, num):
# 		if num % i == 0:
# 			print("Not a prime")
# 			break
# 	else:
# 		print("Is a prime")

#ex(8)
# from random import randint

# secret_num = randint(1, 100)
# num_guesses = 0
# guess = 0

# while guess != secret_num and num_guesses < 4:
# 	guess = eval(input("Enter your guess(1 - 100): "))
# 	num_guesses += 1
# 	if guess < secret_num:
# 		print("HIGHER", 5 - num_guesses, "guesses left.\n")
# 	elif guess > secret_num:
# 		print('LOWER', 5 - num_guesses, "guesses left.\n")
# 	else:
# 		print("You got it!")
	
# if num_guesses == 5 and guess != secret_num:
# 	print("You loose. The correct number is", secret_num)

#alternatively:
# from random import randint 

# secret_num = randint(1, 100)

# for num_guesses in range(5):
# 	guess = eval(input("Enter your guess (1-100): "))
# 	if guess < secret_num:
# 		print("HIGHER", 5 - num_guesses, "guesses left.\n")
# 	elif guess > secret_num:
# 		print("LOWER", 5 - num_guesses, "guesses left.\n")
# 	else:
# 		print("You got it!")
# 		break
# else:
# 	print("You loose. The correct number is", secret_num, "\n")
# 	new_game = input("Would you like to play again? y or n: ")
# 	if new_game == "y":
# 		print("play again")

#ex(1)
# for loop style.
# for i in range(51):
# 	print(i)
#
# while loop style	
# i = 0
# while i < 51:
# 	print(i)
# 	i+= 1          # or i = i + 1 

#ex(2a)
#Program prints strings characters one by one.
# word = input("Enter a string: ")
# for i in range(len(word)):
# 	print(word[i], "\n")          # we do this is we want to keep count.

# word = input("Enter a string: ")
# for c in word:
# 	print(c)

#ex(2b)
# 2a modified to print second character in the string
# word = input("Enter a string: ")
# for i in range(len(word)):
# 	second_char = word[1::2]

# print(second_char, "\n")

#ex(3)
# program to convert weight from kilo-grams to pounds
# weight = eval(input("Enter the weight in kilograms please: "))
# pounds = 2
# conversion = weight*pounds
# while weight < 0:
# 	weight = eval(input("Invalid, please enter a valid weight: "))
# print("The weight in pounds is", conversion, "pounds.")

#ex(4)
# name = "Hamilton"
# password = "indigo+04"
# num_of_tries = 0
# while num_of_tries < 5:
# 	user_pass = input("Enter your password: ")
# 	user_name = input("Enter your username: ")
# 	if user_pass == password and user_name == name:
# 		num_of_tries += 1
# 		print("You have been logged on")
# 		break
# 	else:
# 		print("Password invalid, you have", 4 - num_of_tries, "attempts left.")
# 		num_of_tries += 1
# if num_of_tries == 5:
# 	print("You have been kicked out of the system")
	

#ex(5)
# scores = []
# grades = []
# scores_A = 0
# scores_B = 0
# no_of_entries = 0
# while no_of_entries < 5:
# 	test_scores = eval(input("Enter a test score: "))
# 	if test_scores < 0:
# 			break
# 			print("Done")
# 	scores.append(test_scores)
# 	no_of_entries +=1
	
# for score in scores:
# 	if score >= 90:
# 		grades.append("A")
# 		scores_A += 1
# 	else:
# 		if score < 90:
# 			grades.append("B")
# 			scores_B += 1

# if scores_B > 1 and scores_A > 1:
# 	print("There are", scores_A, "A scores and", scores_B, "B scores.")
# elif scores_B < 1 and scores_A > 1:
# 	print("There are ", scores_A, "A scores")
# else:
# 	print("There are ", scores_B, "B scores")



#ex(6)
# from random import randint 
# secret_num = randint(1, 100)
# num_guesses = 4
# for num_guesses in range(5, 0, -1):
# 	guess = eval(input("Enter your guess (1-100): "))
# 	if num_guesses <= 2 and guess < secret_num:
# 		num_guesses -= 1
# 		print("HIGHER, you have", num_guesses, "guess left.\n" )
# 	elif num_guesses <= 2 and guess > secret_num:
# 		num_guesses -= 1
# 		print("LOWER, you have", num_guesses, "guess left.\n" )
# 	elif num_guesses == 0:
# 		num_guesses -= 1
# 		print("You have nothing left.\n" )
# 	elif guess < secret_num:
# 		num_guesses -= 1
# 		print("HIGHER", num_guesses, "guesses left.\n")
# 	elif guess > secret_num:
# 		num_guesses -= 1
# 		print("LOWER", num_guesses, "guesses left.\n")
	
# 	else:
# 		print("You got it!")
# 		break
# else:
# 	print("You loose. The correct number is", secret_num, "\n")

#ex(7a)
#Program to find the location of a letter in a string
# word = str(input("Please, enter a word: "))
# alpha = str(input("Please enter a letter: "))
# i = 0
# location = 0
# while i < len(word):
# 	if alpha not in word:
# 			print("Letter missing from string.")
# 			break
# 	else:
# 		location = word.index(alpha)

# 	i = i+1
# print(location)

#ex(7b)
# word = input("Please enter a word: ")
# alpha = input("Please enter a letter: ")
# location = 0
# for i in range(len(word)):
# 	if alpha not in word:
# 		print("Letter missing from string.")
# 		break
# 	else:
# 		location = word.index(alpha)

# print(location)

#ex(8)
#Program to compute the greatest common divisor
# a = eval(input("Please enter first value a: "))
# b = eval(input("Please enter second value b: "))
# i = 1
# while(i <= a and i <= b):
# 	if(a % i == 0 and b % i == 0):
# 		gcd = i
# 	i += 1
# print("\n GCD of {0} and {1} = {2}".format(a, b, gcd)) 


#ex(8)
#Program to compute gcd my own solution
# a = eval(input("Enter first value a: "))
# b = eval(input("Enter second value b: "))
# if a > b:
# 	numerator = a
# 	denominator = b
# else:
# 	numerator = b
# 	denominator = a

# while True:
# 	if denominator == 0:
# 		print("The gcd is",numerator)
# 		break	
# 	else:
# 		remainder = numerator % denominator
# 		numerator = denominator
# 		denominator = remainder 

#ex(9)















