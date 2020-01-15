# s = 'Hello'
# t = "Hello"
# m = """This is a long string that is
# spread across two lines"""


# s = " "     # telling that variable s is an empty string
# for i in range(10):
# 	t = input("Enter a letter: ")
# 	if t == "a" or t == "e" or t == "i" or t == "o" or t == "u":
# 		s = s + t
# print(s)
# print(len(s))

# #if t in "aeiou":

# f = "abcdefghij"

# d = f[2:5]
# d = f[ :5]
# d = f[5: ]
# d = f[-2: ]
# d = f[ : ]
# d = f[1:7:2]  # characters from 1 to 7, by twos
# d = f[ : :-1] # negative step string reversal
# print(d)

#strings are immutable to change a character at index 4 do this.

# s = '234567'
# s = s[:4] + 'X' + s[5:]
# print(s)

# for i in range(len(s)):
# 	print(s[i])               #to keep track of the location of the character.

# for c in s:
# 	print(c)

#ex(1)
# s = input("Enter some text: ")
# doubled_s = ''
# for c in s:
# 	doubled_s = doubled_s + c*2
# print(doubled_s)

#ex(2)
# name = input("Enter your name: ")
# for i in range(len(name)):
# 	print(name[:i+1], end=' ')


#ex(3)
#Program that removes all captitalization and punctuation from a string
# s = s.lower()
# for c in ',.;:-?!()\'"':
# 	s = s.replace(c, ' ')

#ex(4)
# #Program that prints the decimal part of a number
# s = input("Enter your decimal number: ")
# print(s[s.index('.')+ 1:])               # find the index where the . is and add 1 to print the decimal number from there.


#ex(4) Alternative solution
# from math import floor
# num = eval(input("Enter your decimal number: "))
# print(num - floor(num))

#ex(7)
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# key = alphabet[::-1]
# new_message = " "
# secret_message = input("Enter your message: ")
# secret_message = secret_message.lower()
# encrypted_message = " "

# for c in secret_message:
# 	if c.isalpha():
# 		print(key[alphabet.index(c)], end='')
# 	else:
# 		print(c, end='') 

#(1)
# s = input("Enter a string: ")
# print(len(s))
# print(s * 10)
# print(s[0])
# print(s[ :3])
# print(s[-4: ])
# print(s[ : :-1])
# if len(s) > 7:
# 	print(s[7])
# else:
# 	print("Index out of range")
# print(s[1:-1])
# s_allcaps = s.upper()
# print(s_allcaps)
# chr_replaced = s.replace('a', 'e')
# print(chr_replaced)

# for c in s:
# 	s = s.replace(c, " ")
# print(s)


# count = 0
# s = input("Enter your string: ")
# for i in range(len(s)):
# 		if  s[i] == ' ':
# 			count += 1
# print("There are", count+1, "words in the sentence")

# def count():    ## this is how to define a function that counts words in a sentence
# 	count = 0
# 	s = input("Enter your string: ")
# 	for i in range(len(s)):
# 			if  s[i] == ' ':
# 				count += 1

# 	print("There are", count, "words in the sentence") # returns an extimate of the number of words in the sentence
# 	                   #count +1                       # returns the exact number of words in the sentence.

# count() # calling the function

#(3)
# s = input("Enter a formula: ")
# count1 = 0
# count2 = 0
# for i in s:
# 	if i == '(':
# 		count1 += 1
# 	elif i == ')':
# 		count2 += 1

# if count1 == count2:
# 	print("Equal number of opening and closing parenthesis")
# else:
# 	print("Unequal number of opening and closing parenthesis")


#(4)
# count = 0
# s = input("Enter a word: ")
# for i in 'a,e,i,o,u':
# 	for c in s:
# 		if c == i:
# 			count += 1

# print("Word contains", count, "vowels")


#(5)
# string = input("Enter a word: ")
# new_string = s[:1] + '*' + s[2:] + '!!!'   # take all the characters up to index 1 add *, then all the characters from index 2 and add !!!
# print(new_string)

#(6) converts string to lowercase and removes puntuation
# s = input("Enter a string: ")
# s = s.lower()
# for c in ',.!':
# 	s = s.replace(c,' ')

# print(s)

#(7) Determines if a a word is a palindrome(reads the same backword and forwords)
# s = input('Enter a word: ')
# t = s[ : :-1] 
# if  t == s:
# 	print(s, "is a palindrome")
# else:
# 	print(s, "is not a palidrome") 

#(8)
# count1 = 0
# count2 = 0
# n = int(input("Number of email addresses?: "))

# for i in range(n):
# 	print("Enter address", ":", end='')
# 	address = input()
# for i in "@st":
# 	for c in 'address':
# 		if c == i:
# 			count1 += 1

# for item in "@pro":
# 	for t in 'address':
# 		if t == item:
# 			count2 += 1

# if count1 == n:
# 	print("All are student addresses")
# elif count1 == n and count2 == 1:
# 	print(count1, "are student addresses and", count2, "is a professor address")
# else:
# 	print(count1, "are student addresses and", count2, "are professor addresses")

# #(9)
# n = int(input("Enter a number: "))
# for i in range(1, n+1):
# 	print('\n',' '*(i-1), i)

# #(10)
# n = input("Enter a string: ")
# for c in n:
# 	print('\n', i*2)

#(11)
# s = input("Enter a word: ")
# for c in s:
# 	if c.isalpha():
# 		location = s.index("a")
# print(s[:location + 1],'\n', s[location + 1:])

#(12)	
# new_word = ''
# s = input("Enter a word: ")
# for index, value in enumerate(s):  # the enumerate function returns the index and value of a string 
# 	if index % 2 == 1:
# 		new_word += value.upper()
# 	else:
# 		new_word += value

# print(new_word)


#(13)
# new_string = ''
# print("Enter two strings of the same length")
# for i in range(1):
# 	print("s", ':', end='')
# 	s = input()
# 	print("t", ':', end='')
# 	t = input()
# 	if len(s) != len(t):
# 		print("String lengths are unequal")
# 	for i in range(len(s)):
# 		new_string += t[i] + s[i]
# print(new_string)

# s = 'abcde'    #hard coded the manual way
# new_new = ''
# t = 'ABCDE'
# if len(s) != len(t):
#	  print("String lengths are unequal")	
# for i in range(len(s)):
# 		new_new += t[i] + s[i]
# print(new_new)

#(14) program capitalizes the first letter of each word in the name
# print("Enter your name in lower case letters: ", end='')
# name = input()
# #f = name.index(' ')
# #name = name[0].upper() + name[1:f] + name[f+1].upper() + name[f+2:]
# name = name[0].upper() + name[1:name.index(' ')] + " " +  name[name.index(' ')+1].upper() + name[name.index(' ')+2:]
# print(name)


#(15)
# print("Enter a college_class: ", end='')
# c_class = input()
# print("Enter an adjective: ", end='')
# adjec = input()
# print("Enter an activity: ", end='')
# activ = input()
# s = "class was really today. We learned how to in school. I can't wait for tomorrow's lecture!"
# f = s.index('class')
# g = s.index('today')
# h = s.index('in')
# new_story = s[:f] + c_class + ' ' + s[f:g] + adjec + ' ' + s[g:h] + activ + ' ' + s[h:]
# print(new_story)

# print("Enter a string: ", end='')
# newstr = input()
# line = 'Kung Panda'
# index = line.index('Panda')
# output_line = line[ :index] + newstr + ' ' +  line[index: ]
# print(output_line)

# #(16)
# print("Enter firstname: ", end='')
# first_name = input()
# print("Enter lastname: ", end='')
# last_name = input()
# msg = """Dear , 
# I am pleased to offer you our new Platinum Plus Rewards card 
# at a special intoductory APR of 47.99%. , an offer 
# like this does not come along every day, so i urge you to call 
# now toll-free at 1-800-314-1592. We cannot offer such a low 
# rate for long, , so call right away."""

# a = msg.index(',')
# b = msg.index('I')
# c = msg.index(', an')
# d = msg.index(' , so')
# e = msg.index('so call')

# new_message = msg[:a] + ' ' + first_name + ' ' + last_name + '\n\n' + msg[b:c] + first_name + msg[c:d] + ' ' + first_name + ' ' + msg[e:]
# print(new_message)


# #(17)
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# for i in range(len(alphabet)):
# 	if alphabet[i] == 0:
# 		print(alphabet[:])
# 	else:
# 		if alphabet[i] != 0:
# 			print(alphabet[i::] + alphabet[:i])

#(18)
#(a)
# print("Enter a string: ", end='')
# name = input()
# print("Enter a letter: ", end='')
# letter = input()
# s = 0
# if letter == name[:s]:
# 	print("Letter appears in the string", name)
# 	s = s + 1
# else:
# 	print("Letter does'nt appear in the string", name)

# #(b)
# s = ''
# print("Enter a string: ", end='')
# name = input()
# print("Enter a letter: ", end='')
# letter = input()
# for c in name:
# 	if c == letter: 
# 		s = s + c
# if len(s) == 1:
# 	print("The letter occurs once") # we subtract by 1 to get the number of occurences of the letter in the string. String of Length 5 runs from 0 to 4
# else:
# 	pass
# 	print("The letter occurs", (len(s) - 1), "times")

# (c)
# print("Enter a string: ", end='')
# name = input()
# print("Enter a letter: ", end='')
# letter = input()
# for i in range(len(name)):
# 	if name[i] != letter:
# 		print("Letter not in string")
# 	else:
# 		print("Letter in string")	# the trick here is to compare the name index which returns 0 - end of string with the input letter

# #(19)
# print("Enter a large integer: ", end='')
# integer = int(input())
# new_integer = format(integer, ",")   #using the format function
# print(new_integer)


#(20)
# time = input("Time: ")
# hour = int((time[:2]))
# zones = ["Pacific", "Eastern", "Central", "Mountain"]
# print("Enter any of the following zones", zones)
# start = input("Starting zone: ")
# end = input("Ending zone: ")
# if start == 'Pacific':
# 	new_hour = (hour + 3) % 12
# 	hour_time= str(new_hour)
# 	new_time = hour_time + time[2:]

# elif start == 'Eastern':
# 	new_hour = (hour + 5) % 12
# 	hour_time = str(new_hour)
# 	new_time = hour_time + time[2:]

# elif start == 'Central':
# 	new_hour = (hour + 8) % 12
# 	hour_time = str(new_hour)
# 	new_time = hour_time + time[2:]


# elif start == 'Mountain':
# 	new_hour = (hour + 9) % 12
# 	hour_time = str(new_hour)
# 	new_time = hour_time + time[2:]

# print(new_time)


#(21)
# print("Enter a word: ", end='')
# word = input()
# new_word = word[2:] + word[:2]
# print(new_word)

#(22) Method of encryption
#(a)
# even = ' '
# odd = ' '
# new_word = ""
# print("Enter a string: ", end='')
# word = input()
# for i in range(len(word)):
# 	if i % 2 == 0:
# 		even += word[i]
# 	else:
# 		if i == 1 or i % 2 != 0:
# 			odd += word[i]
# new_word = even.strip() + odd.strip()
# print(new_word)

#(b)
#decrypt solution incomplete.
# new_words = ""
# for i in range(len(even)):
# 	new_words = new_words + even[i].strip()
# 	for j in range(len(odd)):
# 		new_words = new_words + odd[i].strip()
# print(new_words)

#(23)
# #(a)
# grp_1 = ""
# grp_2 = ""
# grp_3 = ""
# print("Enter a string: ", end=' ')
# word = input()
# for i in range(0, len(word), 3):
# 	grp_1 = grp_1 + word[i]
# for i in range(1, len(word), 3):
#  	grp_2 = grp_2 + word[i]
# for i in range(2, len(word), 3):
#  	grp_3 = grp_3 + word[i]

# encrypted_message = grp_1 + grp_2.strip() + grp_3.strip()
# print(encrypted_message)

# #(b)
# #decrypt
# grp_4 = ""
# grp_5 = ""
# grp_6 = ""
# grp_7 = ""
# grp_8 = ""
# for i in range(0, len(encrypted_message), 5):
# 	grp_4 = grp_4 + encrypted_message[i]
# for i in range(1, len(encrypted_message), 5):
# 	grp_5 = grp_5 + encrypted_message[i]
# for i in range(2, len(encrypted_message), 5):
# 	grp_6 = grp_6 + encrypted_message[i]
# for i in range(3, len(encrypted_message), 5):
# 	grp_7 = grp_7 + encrypted_message[i]
# for i in range(4, len(encrypted_message), 5):
# 	grp_8 = grp_8 + encrypted_message[i]
# decrypted_message = grp_4.strip() + grp_5.strip() + grp_6 + grp_7.strip() + grp_8.strip()

# print(decrypted_message)

#(24)
# print("Enter an equation: ", end=' ')
# equation = input()
# num1 = int(equation[-1:])
# num2 = num1 - 1
# num3 = str(num2)
# new_equation = equation[-1:] + equation[:1] + equation[1:2] + num3
# print(new_equation)

#(25)
