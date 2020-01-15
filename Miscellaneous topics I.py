#Counting

# count = 0
# for i in range(10):
# 	num = int(input("Enter a number:  "))
# 	if num > 10:
# 		count = count + 1
# print('There are', count, 'numbers greater than 10.')

# count1 = 0
# count2 = 0
# for i in range(10):
# 	num = int(input("Enter a number:  "))
# 	if num > 10:
# 		count1 += 1
# 	if num == 0:
# 		count2 += 1
# print("You entered", count1, "numbers greater than 10.")
# print("You entered", count2, "zeros.")

# count = 0
# for i in range(1, 101):
# 	if i % 10 == 4:
# 		count += 1
# 		print(i)
# print("There are", count, "numbers.")

# Program counts how many of the squares from 1^2 and 101^2 end in a 4
# L = []														#creates an empty list
# count = 0
# for i in range(1, 101):
# 	if (i**2) % 10 == 4:  # if the number leaves a remainder of 4 when divided by 10.
# 		count += 1
# 		L.append(i)                 
# print("There are",count, "numbers.")
# print(L)                              



# #Summing
# s = 0
# for i in range(1, 101):
# 	s = s + i
# print("The sum is", s)

# s = 0
# for i in range(10):
# 	num = int(input("Enter a number.  "))
# 	s = s + i
# print("The average is", s/10)

# #swapping

# x,y = y,x

# #flag variables

# num = int(input("Enter a number.  "))

# flag = 0
# for in in range(num):
# 	if num % i == 0:
# 		flag = 1

# if flag == 1:
# 	print("Not prime")
# else:
# 	print("Prime")   # a number is prime if it has no divisors other than 1 and itself.

# #Maxes and Mins
# largest = int(input("Enter a positive number to compare:  "))
# for i in range(9):
# 	num = int(input("Enter a positive number:  "))
# 	if num > largest:
# 		largest = num
# print("Largest number:", largest)

# smallest = int(input("Enter a positive number to compare:  "))
# for i in range(4):
# 	num = int(input("Enter a positive number: "))
# 	if num < smallest:
# 		smallest = num
# print("Smallest number: ", smallest)

#comments.
"""Program name: Hello World
   Author: Hamilton Agwulonu
   Date: 4/19/2019 """

# from random import randint
# count = 0
# for i in range(10000):
# 	num = randint(1, 100)
# 	if num % 12 == 0:
# 		count += 1
# print("The number of multiples of 12:", count)

#ex(1)
# count = 0
# squares = []
# for i in range(1,101):
# 	if i * i % 10 == 1:
# 		count += 1
# 		squares.append(i)
# print("The number of squares that end in a 1 are:", count)
# print(squares)


#ex(2)
# count1 = 0
# count2 = 0
# for i in range(1, 101):
# 	if i * i % 10 == 4:
# 		count1 = count1 + 1
# 	elif i * i % 10 == 9:
# 		count2 = count2 + 1
# print("The number of squares that end in a 4 are: ", count1)
# print("The number of squares that end in a 9 are: ", count2)

#ex(3)
# import math
# s = 1
# n = int(input("Enter a number: "))
# for i in range(1, n):
# 	print(i)
# 	s = s + 1/(i+1)
# 	t = s - math.log(n)
# print(s)
# print("The value of the computation is: ", t)

#ex(4)
# total = 0
# for num in range(1, 2001):
# 	if num % 2 != 0:
# 		total = total + num
# 		print(num, end=' ')

# # print(total)


#ex(5)
# s = 0
# n = int(input("Enter a number. "))
# for i in range(1, n):
# 	if n % i == 0:
# 		s = s + i
# print(s)


#ex(6)Perfect number = the sum of all its divisors excluding itself.
# this version of solution requires repeated user inputs.
# perfect_numbers = []
# while True:
# 	s = 0
# 	t = []
# 	n = int(input("Enter a number: "))
# 	for i in range(1, n):
# 		if n % i == 0:
# 			s = s + i
# 			t.append(i)
# 			print(t)
# 	print(s)

# 	if n == s:
# 		perfect_numbers.append(n)
# 		if len(perfect_numbers) == 1:
# 			print("This is a perfect number", perfect_numbers)
# 		else:
# 			if len(perfect_numbers) >1:
# 				print("These are the perfect numbers", perfect_numbers)



# # this version of solution requires one time user input
# while True:
# 	perfect_numbers = []
# 	u = int(input("Please enter upper limit, enter '0' to quit: "))
# 	if u == 0:
# 		break

# 	for n in range(1, u+1):
# 		s = 0
# 		for j in range(1, n):
# 			if (n % j) == 0:
# 				s = s + j

# 		if n == s:
# 			perfect_numbers.append(n)
# 			if len(perfect_numbers) > 1:
# 				print("These are the perfect numbers", perfect_numbers)
# 			else:
# 				if len(perfect_numbers) == 1:
# 					print("This is a perfect number", perfect_numbers)


#ex(7)
# while True:
# 	t = []
# 	n = int(input("Enter a positive number, enter '0' to quit: "))
# 	if n == 0:
# 		print("Stopped early")
# 		break
# 	for i in range(1, n+1):
# 		if n % (i**2) == 0 and i != 1:
# 			t.append(i**2)
# 			print(t)
# 			print(n, "is not squarefree")
# 			break	
# 	else:
# 		print(n, "is squarefree")

	
#ex(8)
# x = 5
# y = 8
# z = 11
# x, y , z = y, z, x
# print(x, y, z)

#ex(9) counting program
# S = []
# T = []
# U = []
# count = 0
# count2 = 0
# count3 = 0
# count4 = 0
# count5 = 0
# count6 = 0
# for i in range(1, 1001):
# 	s = i**2
# 	t = i**3
# 	u = i**5
# 	if s < 1001:
# 		S.append(s)
# 		count += 1
# 	if i not in S:
# 		count2 += 1
	
# 	if t < 1001:
# 		T.append(t)
# 		count3 += 1
# 	if i not in T:
# 		count4 += 1

# 	if u < 1001:
# 		U.append(u)
# 		count5 += 1
# 	if i not in U:
# 		count6 += 1


# print(S)
# print(count, "are perfect squares and", count2, "are not")
# print(T)
# print(count3, "are perfect cubes and", count4, "are not")
# print(U)
# print(count5, "are perfect_fifth_powers", count6, "are not")

#ex(10)
# L = []
# L.sort()
# for i in range(10):
# 	score = int(input("Please enter scores: "))
# 	L.append(score)
# 	largest = max(L)
# 	lowest = min(L)
# 	average = sum(L)/len(L)
# 	if score > largest:
# 		largest = score
# 	if score < lowest:
# 		lowest = score

# print("The largest score is", largest, "and the lowest is", lowest)
# print("The average is", average)
# second_largest = L.pop(-2)
# print("The second largest is", second_largest)
# for score in L:
# 	if score > 100:
# 		print("Warning!, value over 100 was entered")

# #dropping the two lowest scores
# del L[:2]
# new_average = sum(L)/len(L)
# print("The new average is", new_average) 



#ex(11)compute the factorial of any number
# factorial = 1
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
# 	factorial = factorial * i

# print(n,"factorial is", factorial)

#ex(12)
#Program random number guess.
# from random import randint
# score = 0
# for i in range(5):
# 	num = randint(1, 10)
# 	guess = int(input("Enter your guess: "))
# 	if guess == num:
# 		score += 10
# 	else:
# 		score -= 1

# if score < 0:
# 	print("You loose!, your score is", score)
# else:
# 	print("Nice try, your score is", score)

# ex(13)
# from random import randint
# question_number = 1  # initialize the question variable which begins from 1
# right = 0            # initialize the correct answer variable, starts from 0 since we have 0 answers at the beginning
# wrong = 0
# for i in range(10):
# 	num_1 = randint(1,10) # generate a random number within the range and store the value in the variable
# 	num_2 = randint(1,10)
# 	answer = num_1 * num_2   # stores the multiplication value of the numbers generated
# 	print("Question", question_number,":", num_1, "*", num_2, "= ", end='') # end; used to place the user-response on the same print line
# 	response = int(input())
# 	question_number += 1      # increments question_number after each question
# 	if response == answer:    # checks to see if response matches answer
# 		print("right!")
# 		right += 1            #increments Right each time a correct answer is given
# 	else:
# 		print("Wrong! The answer is", answer)
# 		wrong += 1

# if right == 10:                                  # the following if statement should be outside the for loop so as to compute
# 	print("Amazing!, you answered all correctly")  # and return the answer at the end of the session
# elif right <= 4:
# 	print("You have to improve! you got", wrong, "answers wrong" )
# else:
# 	print("Nice try, you got only", right, "questions correctly" )