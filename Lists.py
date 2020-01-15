# L = eval(input("Enter a list: "))
# print("The first element is ", L[0])

#Program generates a list of 50 random numbers btwn 1 and 100.and

#Example 1
# from random import randint
# L = []
# for i in range(50):
# 	L.append(randint(1, 100))

# print(L)

#Example 2: Replace each element in a list with its square
# new_list = []
# for i in range(len(L)):
# 	L[i] = L[i]**2
# 	new_list.append(L[i])
# print(new_list)

#Example 3: Count how many items in a list are greater than 50. put them in a new list
# new_list1 = []
# count = 0
# for i in L:
# 	if i > 50:
# 		count += 1
# 		new_list1.append(i)
# print(count)
# print(new_list1)

#ex(4)
# Given a list with nums btwn 1 and 100 create a new list whose first element is how many one are in L, whose second element is how many twos are in L.
# from random import randint
# frequencies = []
# L = []
# count = 0
# for i in range(101):
# 	c = randint(1, 101)
# 	L.append(c)

# for i in range(len(L)):
#     if i == 1:
#     	count += 1
#     	frequencies.append(L.count(i))

# print(frequencies)

# #ex(5)
#Program prints out the two largest and smallest scores in a list
# scores = []
# for i in range(5):
# 	print("Enter a score: ", end='')
# 	score = int(input())
# 	scores.append(score)
# 	scores.sort()

# print(scores)
# print('Two smallest: ', scores[0], scores[1])
# print('Two Largest: ', scores[-1], scores[-2])

# #ex(6)
# Program to play a game.
# questions = ['What is the capital of France?: ',
# 			 'Which state has only one neighbor?: ']
# answers = ['Paris', 'Maine']

# num_right = 0
# for i in range(len(questions)):
# 	guess = input(questions[i])
# 	if guess.lower() == answers[i].lower():
# 		print('Correct')
# 		num_right += 5
# 	else:
# 		print('Wrong. The answer is', answers[i])
# 		num_right -= 1

# print('You have', num_right, 'out of', i+1, 'right.')


# #(1)
# count = 0
# count2 = 0
# L = eval(input('Enter a list of integers: '))
# print('The total number of elements is ', len(L))
# print('The last item in the list is ', L[-1])
# L.reverse()
# print('The list in reverse order is ', L)
# if 5 in L:
# 	print('Yes')
# else:
# 	print('No')

# for i in range(len(L)):
# 	if L[i] == 5:
# 		count += 1
# print(count)
# del L[1:-1]
# L.sort()
# print(L)

# for i in range(len(L)):
# 	if L[i] < 5:
# 		count2 += 1
# print(count2)

# #(2)
# from random import randint
# L = []
# count3 = 0 #counts even numbers
# count4 = 0 #counts odd numbers
# for i in range(20):
# 	L.append(randint(1, 100))
# print(L)
# print("The average is ", sum(L)/len(L))
# print('The largest value is', L[-1], 'The smallest is', L[0])
# print('The second largest and smallest entries are', L[1], 'and', L[-2])
# for i in range(len(L)):
# 	if L[i] % 2 == 0:
# 		count3 += 1
# 	else:
# 		if L[i] % 2 != 0:
# 			count4 += 1
# print(count3)
# print(count4)

# #(3)
# L = [8, 9, 10]
# L[1] = 17
# L.append(4)
# L.append(5)
# L.append(6)
# del L[0]
# L.sort()
# L[3] = 25
# print(L * 2 )

# #(4)
# L = eval(input(('Enter a list of numbers between 1 and 12: ')))
# for i in range(len(L)):
# 	if L[i] > 10:
# 		L[i] = 10
	
# print(L)

# #(5)
# new_L = []
# L = eval(input("Enter a list of strings: "))
# for item in L:
# 	item = item[1:]
# 	new_L.append(item)

# print(new_L)

#(6)
#(a)
# L = []
# L2 = []
# for i in range(50):
# 	L.append(i)
#(b)
# for i in range(1, 51):
# 	i = i**2
# 	L2.append(i)
# print(L)
# print(L2)

#(c)
#alpha = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
# 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# new_alpha = []
# for i in range(len(alpha)):
# 	rpt_chr = alpha[i] * (i+1)  #alpha[i] returns the string in the lists index
# 	new_alpha.append(rpt_chr)
# print(new_alpha)

# #(7)
# L = [3, 1, 4]
# M = [1, 5, 9]
# N = []
# for i in range(len(L)):
# 	if len(L) == len(M):
# 		n = L[i] + M[i]
# 		N.append(n)
#	else:
#		print('Lists are not of the same length')
# print(N)

#(8)
# L = []
# print('Enter an integer: ')
# integer = int(input())
# for i in range(1, integer):
# 	if integer % i == 0:
# 		L.append(i)
# print(L) 

#(9)
# from math import *
# from random import randint
# L = []
# M = []
# count_2 = 0
# count_3 = 0
# count_4 = 0
# count_5 = 0
# count_6 = 0
# count_7 = 0
# count_8 = 0
# count_9 = 0
# count_10 = 0
# count_11 = 0
# count_12 = 0
# for i in range(10000):
# 	L.append(randint(1,7))
# 	M.append(randint(1,7))
# for i in range(len(L)):
# 	N = L[i] + M[i]
# 	if N == 2:
# 		count_2 += 1
# 		perc_2 = round(((count_2/10000) * 100))
# 	elif N == 3:
# 		count_3 += 1
# 		perc_3 = round(((count_3/10000) * 100))
# 	elif N == 4:
# 		count_4 += 1
# 		perc_4 = round(((count_4/10000) * 100))
# 	elif N == 5:
# 		count_5 += 1
# 		perc_5 = round(((count_5/10000) * 100))
# 	elif N == 6:
# 		count_6 += 1
# 		perc_6 = round(((count_6/10000) * 100))
# 	elif N == 7:
# 		count_7 += 1
# 		perc_7 = round(((count_7/10000) * 100))
# 	elif N == 8:
# 		count_8 += 1
# 		perc_8 = round(((count_8/10000) * 100))
# 	elif N == 9:
# 		count_9 += 1
# 		perc_9 = round(((count_9/10000) * 100))
# 	elif N == 10:
# 		count_10 += 1
# 		perc_10 = round(((count_10/10000) * 100))
# 	elif N == 11:
# 		count_11 += 1
# 		perc_11 = round(((count_11/10000) * 100))
# 	elif N == 12:
# 		count_12 += 1
# 		perc_12 = round(((count_12/10000) * 100))
# print(count_2, count_3, count_4, count_5, count_6, count_7, count_8, count_9, count_10, count_11, count_12)

# print('Percentage 2 is', perc_2, '%')
# print('Percentage 3 is', perc_3, '%')
# print('Percentage 4 is', perc_4, '%')
# print('Percentage 5 is', perc_5, '%')
# print('Percentage 6 is', perc_6, '%')
# print('Percentage 7 is', perc_7, '%')
# print('Percentage 8 is', perc_8, '%')
# print('Percentage 9 is', perc_9, '%')
# print('Percentage 10 is', perc_10, '%')
# print('Percentage 11 is', perc_11, '%')
# print('Percentage 12 is', perc_12, '%')

#(10)
# L = ['a', 'b', 'c']
# for i in range(1):
# 	L = L[-1:] + L[:-1]
# 	print(L)

# #(11) not exactly
# L = []
# for i in range(1, 11):
# 	if i == 1:
# 		L.append(1)
# 	else:
# 		if i > 1:
# 			L.append([1])
# 			L.append([0]*i)
# print(L) 


#(12)
# from random import randint
# data = []
# for i in range(10):
# 	data.append(randint(0,1))

# longest = 0
# current = 0
# for num in data:
# 	if num == 1:
# 		current += 1
# 		print(current)
# 	else:
# 		longest = max(longest, current)
# 		current = 0

# print(data)
# print("The longest run of 1\'s is", longest)

# from random import randint   # solving the above problem using function call.
# data = []
# for i in range(100):
# 	data.append(randint(0,1))
# def consecutive_one(data):
# 	longest = 0
# 	current = 0
# 	for num in data:
# 		if num == 1:
# 			current += 1
# 		else:
# 			longest = max(longest, current)
# 			current = 0
# 	return max(longest, current)
# print(data)
# print(consecutive_one(data))
	

#(13)
# L = [1, 1, 2, 3, 4, 3, 0, 0]
# for num in L:
# 	b = L.count(num)
# 	if b > 1:
# 		L.remove(num)
# print(L)

# #(14) Program to convert from feet to listed values of measurement
# L = ['inches', 'yards', 'miles', 'millimeters', 'centimeters', 'meters', 'kilometers']
# measure = [12, 0.3333, 0.000189394, 304.8, 30.48, 0.3048, 0.003048]
# print("Enter a length in feet: ", end='')
# length = float(input())
# print('Choose a measure to convert btwn 0 and 6: ', end='')
# answer = int(input())
# for i in range(len(L)):
# 	i = answer
# 	a = length * measure[i]
# print('Conversion to', L[i])
# print(length, 'feet is ', a, L[i])

#(15)
# from random import randint
# print("Enter a message: ", end='')
# message = input()
# new_message = ' '
# shifts = []
# new_index = []
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
# 'v', 'w', 'x', 'y', 'z'] 
# alpha_long = alpha * 2
# print(alpha_long)
# for a in message:
# 	shifts.append(randint(1, 26))
# print(shifts)

# for i in range(len(message)):
# 	a = alpha_long.index(message[i])
# 	for j in range(len(shifts)):
# 		b = shifts[j]
# new_pos = a + b
# new_index.append(new_pos)
# print(a)
# print(b)
# print(new_index)

	


# message = "secret"
# for i in range(len(message)):
# 	print(message[i])










