# #(1)
# for i in range(100):
# 	print('Hamilton')

#(2)
# for i in range(100):
# 	print('Hamilton', end='')

#(3)
# for i in range(1, 101):
# 	print(i, 'Hamilton')

# #(4) 
# for k in range(1, 21):
# 	print( k, k*k, sep='---')

# #(5)
# for k in range(8, 92, 3):
# 	print(k, '', end='')

# # (6)
# for k in range(100, 0, -2):
# 	print(k, ' ', sep=',', end='')

# # (7)
# for i in range(10):
# 	print('A', end='')
# for i in range(6):
# 	print('B', end='')
# for i in range(3):
# 	print('C', end='')
# 	print('D', end='')
# print('E', end='')
# for i in range(6):
# 	print('F', end='')
# print('G')

# #(8)
# name = str(input('What is your name? '))
# repeat = int(input('Please enter the number of times to repeat: '))
# for i in range(repeat):
# 	print(name)
	
# #(9)
#Program to display fibonacci numbers up to n-th term
# nterms = int(input('Enter number of digits you want in series (minimum 2): '))
# first = 0
# second = 1
# print('\nfibonnaci series is: ')
# print(first, second, end=',')
# for i in range(2, nterms):
# 	next_n = first + second 
# 	print(next_n, end=',')

# 	first = second
# 	second = next_n  


# #(10)
# how_high = int(input('Please enter how high: '))
# how_wide = int(input('Please enter how wide: '))
# display_character = str(input('Please enter the character: '))
# for i in range(how_high):
# 	print(display_character*how_wide)

#(11)

# how_high = int(input('Please enter how high: '))
# how_wide = int(input('Please enter how wide: '))
# display_character = str(input('Please enter the character: '))
# print(display_character*how_wide)
# for i in range(1, how_high - 2):
# 	print(display_character, ' ' *(how_wide - 2), display_character, sep='')
# print(display_character*how_wide)


#(12)
# height = int(input('Enter triangle height: '))
# for i in range(height):
# 	print('*'*(i+1))

#(13)
# height = int(input('Enter triangle height: '))
# for i in range(height):
# 	print('*'*(i-1))

# (14)
# h = int(input('Please enter diamonds height: '))
# for i in range(1, h, 2):
# 	print(" "*(h//2 - i//2), "*"*i)
# for i in range(h, 0, -2):
# 	print(" "*(h//2 - i//2), "*"*i)


# #(15)
h = int(input('Please enter letters height: ')) 
for i in range(1, h, 2): 
	print(" "*(h//2 - i//2), "*"*(i)) # 4, 3, 2, 1, 0 spaces
# 									# 1, 3, 5, 7, 9 stars

# h= int(input('Enter height of the letter: '))
# for i in range(0, h, 1):
# 	print(' '*(h//2 - i//2), '*'*((i**2)+1))


# limit= int(input('Enter height of the letter: '))	
# for i in range(limit+1):
# 	print((limit-1)*" "+ ' #'*i)

# def pattern(limit):

#     for i in range(1, limit+1, 1):
#         print((limit-i)*" "+ ' #'*((i*2)+1))    

# pattern(4)


#h = int(input('Enter the height: '))
#for i in range(0, h, 1):
#	print("  "*(h//2 - i//2), ' *'*((i*2)+1))
	# if h < 5:
	# 	print('*', " "*(h-1), '*')
	# else:
	# 	print('*', " "*(h-2), '*')