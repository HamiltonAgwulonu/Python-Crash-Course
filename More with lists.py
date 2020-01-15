#ex(1)
# from random import choice
# names = ['Joe', 'Bob', 'Sue', 'Sally']
# current_player = choice(names)
# print(current_player)

#ex(2)
# from random import sample
# names = ['Joe', 'Bob', 'Sue', 'Sally']
# team = sample(names, 2)
# print(team)

#ex(3)
# from random import choice
# s = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
# for i in range(10000):
# 	print(choice(s), end='')

#ex(4)
# from random import shuffle
# names = ['Joe', 'Bob', 'Sue', 'Sally']
# shuffle(names)
# teams = []
# for i in range(0, len(names), 2):
# 	teams.append([names[i], names[i+1]])

# print(teams)

# s = 'Hi! this is a test.'
# # print(s.split())

# from string import punctuation
# for c in punctuation:
# 	s = s.replace(c, '')
# print(s)



# #List comprehensions
# L = [i for i in range(5)]
# print(L)


# M = [0 for i in range(10)] 
# print(M)

# S = [i**2 for i in  range(1, 8)]
# print(S)


# string = 'Hello'
# L = [1, 12, 5, 9, 12]
# M = ['one', 'two', 'three', 'four', 'five', 'six']

# A = [c*2 for c in string]
# print(A)

# D = [m[0] for m in M]
# print(D)

# E = [i for i in L if i < 10]
# print(E)

# F = [m[0] for m in M if len(m)==3]
# print(F)


# G = [[i, j] for i in range(2) for j in range(2)]
# print(G)

#conversely can be written as
# L = []
# for i in range(2):
# 	for j in range(2):
# 		L.append([i,j])
# print(L)


#Using list comprehensions
# from random import randint
# L = [randint(1,100) for i in range(50)]
# print(L)

# L = [1, 2, 4, 6]
# L = [i**2 for i in L]
# print(L)

# H = len([i for i in L if i>50])
# print(H)
# L = [i for i in range(1,100)]
# print(L)
# frequencies = [L.count(i) for i in range(1, 100)]
# print(frequencies)



# #(1)
# count = 0
# print("Enter some text: ", end=' ')
# text = input()
# text = text.split()
# articles = ['a', 'an', 'the']
# for item in text:
# 	for i in articles:
# 		if item == i:
# 			count += 1
# print(count)

#(2)  # this creates a list
# s = []
# for i in range(5):
# 	print("Enter a number: ", end='')
# 	number = input()
# 	s.append(number)
# s = '+'.join(s)
# print(s)

# s = ' '
# for i in range(5):
# 	print("Enter a number: ", end='')
# 	number = input()
# 	s = s + number
# list('s')
# s = '+'.join(s)
# print(s)
#(In the problem above first we created a string of numbers, next we converted the string into a list and lastly we applied the join method on the list of stings)

#(3)
# print("Please enter a sentence: ", end='')
# sentence = input()
# sentence = sentence.split()
# print(sentence[2])

# for word in range(2, len(sentence), 2):
# 	print(sentence[word])


# L = [1, 2, 4, 5, 6, 7, 8]

# for i in range(2, len(L), 2):
# 	print(L[i])

#(4)
# from random import shuffle
# print("Please enter a sentence: ", end='')
# sentence = input()
# original_sentence = sentence
# sentence = sentence.split()
# shuffle(sentence)
# print(sentence)
# print(original_sentence)

#5
# from random import choice
# quotes = ['I think, therefore i am.', 'We are what we repeatedly do', 'What goes around comes around!']
# current_quote = choice(quotes)
# print(current_quote)


#(6)
# L = []
# from random import sample
# for i in range(1,49):
# 	L.append(i)
# lottery_numbers = sample(L, 6)
# print(lottery_numbers)


#(7)
# import random
# users_numbers = [2, 6, 4, 8, 1, 5]
# count = 0
# count2 = 0
# for i in range(1000):
# 	drawings = random.sample(range(1, 10), 6)
# 	print(drawings)
# 	if drawings != users_numbers:
# 		count += 1
# 	elif drawings == users_numbers:
# 		count2 += 1
		
# average = count2/1000
# print(count)
# print(count2)
# print(average)


# #(8)
# from random import sample
# hat_names = []
# no_of_entries = []
# for i in range(5):
# 	print('Enter a list of names: ', end='')
# 	names = input()
# 	hat_names.append(names)
# print(hat_names)

# for i in range(3):
# 	print("Enter the no of entries each player has: ", end='')
# 	entries = int(input())
# 	no_of_entries.append(entries)

# drawings = sample(hat_names, 3)
# print(drawings)
# #for player_A
# for i in range(no_of_entries[0]):
# 	player_A_drawings = sample(hat_names, 3)
# 	print(player_A_drawings)
# 	if player_A_drawings == drawings:
# 		print('Player A wins')
# 	else:
# 		print('Player A losses')
# #for player_B
# for i in range(no_of_entries[1]):
# 	player_B_drawings = sample(hat_names, 3)
# 	print(player_B_drawings)
# 	if player_B_drawings == drawings:
# 		print('Player B wins')
# 	else:
# 		print('Player B losses')
# #for player_C
# for i in range(no_of_entries[2]):
# 	player_C_drawings = sample(hat_names, 3)
# 	print(player_C_drawings)
# 	if player_C_drawings == drawings:
# 		print('Player C wins')
# 	else:
# 		print('Player C losses')


#(9)
# from random import sample
# count = 0
# L = []
# questions = ['What is the best programming language?: ',
#             'Who won the premier league in 2019?: ',
#             'Who is the president of America?: ',
#             'Which is the biggest ocean in the world?: ',
#             'Who is the Largest Aircraft maker?: ',
#             'Where does love start?: ',
#             'Why do we grow old and die?: ',
#             'What is the simplest subject to learn?: ',
#             'What is the capital of France?: ',
#             'What is the capital of Germany?: ']
# answers = ['Python', 'Man-City', 'Donald Trump', 'The Pacific', 'Air-Bus', 'The Heart', 'Sin', 'Mathematics', 'Paris', 'Berlin']
# questions_to_answer = sample(questions, 4)
# for i in range(len(questions_to_answer)):

# 	print(questions_to_answer[i], end='')
# 	user_answer = input()
# 	if user_answer == answers:
# 		print('Correct!')
# 		count += 1
# print('You got', count, 'out of 4 right!')

# L = [1, 2, 4]
# M = ['Mary', 'James', 'John']


# for i in range(len(L)):
# 	print('Enter your answer',L[i], ': ', end='')
# 	answer = input()
# 	if M[i] == answer:
# 		print('Yes')
# 	else:


#10 
# sentence = str(input("Enter some text: "))
# curse_words = ["darn", "dang", "freakin", "heck", "shoot"]
# for item in len(curse_words):
# 	if wrd in curse_words:
# 	sentence = sentence.replace(M[i], N[i]) 
# print(sentence)

# L = ['James', 'Peter', 'John']
# M = ['Martha', 'John', 'Mary']
# for i in range(len(L)):
# 	for i in range(len(M)):
# 		if L[i] in M:
# 			print(L[i])
