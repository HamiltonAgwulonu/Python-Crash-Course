
# from random import randint
# for x in range(50):
# 	x = randint(3, 6)
# 	print(x, " ", end='')


# from random import randint
# x = randint(1, 50)
# y = randint(2, 5)
# z = x**y
# print('x is: ', x, 'y is: ', y, 'x raised to power y is: ', z)


# from random import randint
# x = randint(1, 10)
# print(x)
# if x > 1:
# 	print('Hamilton'*x)

#from numpy import random # generate a random array of float numbers
# import random # imports everything
# x = random.uniform(1, 10)
# print(round(x, 2))

# #(5)
# from random import randint
# stop = 1
# for x in range(51): # determines how many times we will loop
# 	x = randint(1, stop + 1)
# 	stop += 1
# 	print(x, ' ', end='')

# #(6)
# x = int(input('Please enter the first number: '))
# y = int(input('Please enter the second number. '))
# z = (abs(x-y)/(x+y))
# print(z)

#(7)
#for x in range(3):
# x = int(input('Please enter an angle between -180 and 180 degrees: '))
# if -180 < and x < 180:
# 	y = (x + 180)%360
# 	print('x is equal to: ', y, 'degrees')	
# else:
# 	print('The value provided is out of bounds')

#(8)
#Seconds to minutes and seconds converter
# seconds = eval(input('Please enter a number in seconds: '))
# minutes = seconds//60  # returns the integer
# seconds_2 = seconds%60 # returns the remiander which is the seconds
# print(seconds,'seconds equals', minutes, 'minutes and', seconds_2, 'seconds')


#(9)
# calculate future hour
# user_hour = int(input('Enter Hour: '))
# future = int(input('How many hours ahead?: '))
# if user_hour >= 1 and user_hour <= 12:
# 	New_hour = (user_hour + future) % 12
# 	print(New_hour, "o\'clock")


#(10a)
# Find the last digit of a number
# power = int(input('Enter a power: '))
# last_digit = (2**power) % 10
# print(last_digit)

# (10b)
# Find the last two digits of a number
# power = int(input('Enter a power: '))
# last_digit = (2**power) % 100
# print(last_digit)

#(10c)
#Prompt user for power and number of last digits hey want
# power = int(input('Enter a power: '))
# digits = int(input('Enter the number of digits: '))
# last_digit = (2**power) % digits
# print(last_digit)

#(11)
# weight_kg = int(input('What is the weight?: '))
# weight_pnd = (weight_kg * 2205)
# print(round(weight_pnd, -1))

#(12)
#from math import *
# number = int(input('Enter a number?: '))
# print(factorial(number))


#(13)
# from math import *
# number = int(input('Enter a number: '))
# print('sin',(number),' = ', sin(number), 'cos',(number), ' = ', cos(number), 
# 	'tan',(number), ' = ', tan(number))

#(14)
# from math import *
# angle = int(input('Enter an angle: '))
# print('sin',(angle), ' = ', sin(angle))

#(15)
# from math import *
# for i in range(0, 360, 15):
# 	sine = sin(i)
# 	cose = cos(i)
# 	print(i, ' --- ', sin(i), ' ', cos(i))


#(16)
	# print()


#(17)
#Program to check for leap year
# start_year = 1600
# end_year = int(input("enter end year: "))
# count = 0
# for start_year in range(start_year, end_year):
# 	if start_year % 4 == 0:
# 		count += 1
# 		print(start_year)

# print('There have been' + ' ' + str(count) + ' ' + 'leap years since' + ' ' 
# 	+ str(start_year))



#(18)
#Program to convert currency
# amount = float(input("Enter the amount: "))
# quater = amount // 0.25
# penny = amount // 0.01
# dime = amount // 0.10
# nickel = amount// 0.05
# print(amount, 'cents is equivalanet to', str(quater) + ' ' 
# 	+ str("quaters,") + ' ' + str(penny) + ' ' + str("pennies,") + ' ' 
# 	+ str(dime) + ' ' + str("dimes,") + ' ' + 'and' + ' ' + str(nickel) + ' ' + str("nickels."))
