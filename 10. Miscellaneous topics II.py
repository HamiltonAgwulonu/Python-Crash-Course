#ex(1)
# Program to print palindromic numbers 1 and 10000
# for i in range(1, 10001):
# 	s = str(i)
# 	if s == s[::-1]:
# 		print(s)

#ex(2)
#Program that tells how old a person is.
# birthday = 'January 1, 1991'
# year = int(birthday[-4:])
# print('You are', 2010-year, 'years old.')


#ex(3)
# #Program that takes a number and adds its digits.
# digit = str(input("Enter a number: "))
# answer = 0
# for i in range(len(digit)):
# 	answer = answer + int(digit[i])
# print(answer)

#Using list comprehension we can achieve the above.

# answer = sum([int(c) for c in str(input("enter a number: "))])
# print(answer)

#Break a decimal number
# num = float(input("Enter a number: "))
# ipart = int(num)
# dpart = num - ipart
# print(ipart)
# print(dpart)

#Booleans

# game_over 

#Short circuiting

# for w in words:
# 	if w[4] == 'z':
# 		print(w)

#the above code will return an index out of range error. Instead we do the following

#if len(words) >= 5 and w[4] == 'z':  # this is shortcircuiting in action where the first part of the condition is checked.

#Continuation
#Sometimes to split a line of code across two lines

# if 'a' in string or 'b' in string or 'c' in string \
# or 'd' in string or 'e' in string:


#String Formatting: Using the format method of strings
# a = 23.60 * .25
# print("The tip is {:.2f}".format(a))


# bill = 23.60
# tip = 23.60 *.25
# print("Tip: ${:.2f}, Total: ${:.2f}".format(tip, bill+tip))


