# x=6
# if (type(x) is int):
#     print('True')

# else:
#     print('False')


# x=6.7
# if (type(x) is not float):
#     print('True')

# else:
#     print('False')


# x=70
# y=70

# if (x is y):
#     print('x and y SAME identity!')

# y=67
# if (x is not y):
#     print('x and y have DIFFERENT identity')

# a=7
# b=-7

# print('a >> 1 =', a >> 1)
# print('b >> 1 =', b >> 1)

# a=6
# a=-7

# print('a << 1 =', a<<1)
# print('b << 1 =', b<<1)

print('Enter marks obtained in 5 subjects')

markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive
avg = int(tot / 5)

validRange = range(0,101)

if avg not in validRange:
    print('Invalid Input!!')

elif avg in range(91,101):
    print('Your grade is A1')
elif avg in range(81,91):
    print('Your grade is A2')  
elif avg in range(71,81):
    print('Your grade is B1') 
elif avg in range(61,71):
    print('Your grade is B2')
elif avg in range(51,61):
    print('Your grade is C1') 
elif avg in range(41,51):
    print('Your grade is C2')
elif avg in range(31,41):
    print('Your grade is D1')
elif avg in range(21,31):
    print('Your grade is D2')
elif avg in range(11,21):
    print('Your grade is E')
elif avg in range(1,11):
    print('Your grade is F')