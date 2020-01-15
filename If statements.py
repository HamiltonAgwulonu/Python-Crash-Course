# Do something provided something else is true.

#Random number game guess
# from random import randint
# num = randint(1, 10)
# for guess in range(3):
# 	guess = int(input("Enter your guess: "))
# 	if guess == num:
# 		print("You got it!")
# 	else:
# 		print("Sorry. The number is ", num)
# print("Game over!")

# to construct more complicated conditions use and or and not

# if grade>= 80 and grade < 90:
# 	print('Your grade is a B.')

#Alternatively we can write so: 
# if 80<=grade<90:

# grade = int(input("Enter your score: "))
# if grade > 1 or grade < 100:  # this condition is wrong because every number stisfies it.
# 	print('You passed!')

# elif

# grade = int(input("Entr your score: "))
# if grade >= 90:
# 	print("A")
# elif grade >= 80:
# 	print("B")
# elif grade >= 70:
# 	print("C")
# elif grade >= 60:
# 	print("D")
# else:
# 	print("F")

#(1)
# length = float(input("Enter the length: "))
# centimeters = 2.54
# if length > 0:
# 	inches = length*centimeters
# 	print(length, "centimeters is equivalent to", inches, "inches.")
# else:
# 	print("Entry invalid!, entry should be greater than 0: ")

#(2)
# t = int(input("Enter the temperature: "))
# units = input("What unit is your temperature, celcius, 'c' or fahrenheit, 'f'?: ")
# if units == 'c':
# 	f = (9/5)*t + 32
# 	print(t, "degrees celsius is", f, "degrees fahrenheit!"  )
# elif units == 'f':
# 	c = (5/9)*(t - 32)	
# 	print(t, "degrees fahrenheit is", c, "degrees celsius!" )
# else:
# 	print("Invalid unit!, try again")

# #(3)
# Using elif's as soon as the condition is true, the rest of the conditions are 
# skipped until the end of the whole block 
# t = float(input("Enter a temperature: "))
# units = input("Enter the units of measure: celcius 'c' or fahrenheit, 'f'?: ")
# if t < -273.15:
# 	print("Invalid temperature!, temperature below absolute zero")
# elif t == -273.15:
# 	print("The temperature is absolute", 0)
# elif -273.15 > t < 0:
# 	print("The temperature is below freezing!")
# elif t == 0:
# 	print("The temperature is at the freezing point!")
# elif 0 <= t < 100:
# 	print("The temperature is in the normal range!")
# elif t == 100:
# 	print("The temperature is at the boiling point")
# else:
# 	print("The temperature is above the boiling point")


#(4)
# total_credits = int(input("How many credits have you taken?: "))
# if total_credits <= 23:
# 	print("You are a freshman!")
# elif 24 < total_credits < 53:
# 	print("You are a sophomore!")
# elif 54 < total_credits < 83:
# 	print("You are a junior!")
# else:
# 	print("You are a senior!")

#(5)
# from random import randint
# guess = int(input("Enter your guess: "))
# if guess == randint(1,10):
# 	print("You got it!")
# else:
# 	print("Wrong!")

# #(6)
# no_of_items = int(input("Please enter the no of items:"))
# if no_of_items < 10:
# 	cost = 12 * no_of_items
# 	print("Your total cost is", "$",cost)
# elif 10 < no_of_items < 99:
# 	cost = 10 * no_of_items
# 	print("Your totak cost is", "$",cost)
# elif no_of_items >= 100:
# 	cost = 7 * no_of_items
# 	print("Your total cost is", "$",cost)

# #(7)
# num_1 = float(input("Please enter first number: "))
# num_2 = float(input("Please enter second number: "))
# if (num_1 - num_2) == 0.001:
# 	print("Close!")
# else:
# 	print("Not Close!")


# #(8)
# year = int(input("Please enter year: "))
# if (year % 100 == 0) and (year % 400 == 0):
# 	print("Year is  a leap year!")
# elif year % 4 == 0:
# 	print("Year is a leap year!")
# else:
# 	print("Year is not a leap year")



#(9)
# number = int(input("Please enter a number: "))
# for i in range(1, number):
# 	if number % i == 0:
# 		print(i, end=' ')

# #(10)
# from random import randint
# question_number = 1  # initialize the question variable which begins from 1
# Right = 0            # initialize the correct answer variable, starts from 0 since we have 0 answers at the beginning
# for i in range(10):
# 	num_1 = randint(1,10) # generate a random number within the range and store the value in the variable
# 	num_2 = randint(1,10)
# 	answer = num_1 * num_2   # stores the multiplication value of the numbers generated
# 	print("Question", question_number,":", num_1, "*", num_2, "= ", end='') # end; used to place the user-response on the same print line
# 	response = int(input())
# 	question_number += 1      # increments question_number after each question
# 	if response == answer:    # checks to see if response matches answer
# #		print("Right!")
# 		Right += 1            #increments Right each time a correct answer is given
# 	else:
# 		print("Wrong! The answer is", answer)

# if Right == 10:                                  # the following if statement should be outside the for loop so as to compute
# 	print("Amazing!, you answered all correctly")  # and return the answer at the end of the session
# else:
# 	print("Nice try, You got only", Right, "questions correctly")


#(11)
# hour = int(input("Enter hour: "))
# print("Is it", "am:", (1), "or", "pm:", (2),"? ", end='')
# time_of_day = int(input())
# hours_ahead = int(input("How many hours ahead? "))
# New_hour = (hour + hours_ahead) % 12
# if hour + hours_ahead >= 12:
# 	print(New_hour, "pm.")
# else:
# 	print(New_hour, "am.")

# #(12)
# for no_of_candies in range(1, 200):
# 	if no_of_candies % 5 == 2 and no_of_candies % 6 == 3 and no_of_candies % 7 == 2:
# 		print(no_of_candies)

# #(13)
# from random import choice
# shapes = ["rock", "paper", "scissors"]
# computer = choice(shapes)
# rounds = 1
# user_wins = 0
# computer_wins = 0
# for games in range(5):
# 	print("Round", rounds, "Your turn: ", end='')
# 	user = input()
# 	rounds += 1
# 	if user == computer:
# 		print("Correct")
# 		user_wins += 1
# 	else:
# 		print("Wrong!")
# 		computer_wins += 1

# if user_wins > computer_wins:
# 	print("You won the game")
# elif user_wins == computer_wins:
# 	print("We have a tie")
# else:
# 	print("Computer won the game")