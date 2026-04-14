# # WAP to calculate perimeter of triangle in Python?

# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

num1= int(input('Enter first value here...'))
num2= int(input('Enter second value here...'))
num3= int(input('Enter third value here..'))

if num1+num2 >= num3 and num2+num3>= num1 and num1+num3>=num2:
    

    if num1==num2==num3 :
    
        print('This is an equilateral triangle.')
    elif num1 != num2 != num3 :
        print('This is a scalene triangle.')
    elif num1 == num2 or num1==num3 or num2==num3 or num3:
        print('This is an isosceles triangle.')
    else: 
        print('This is invalid. Please try again.')
    
else:
    print('This is not a triangle!')

 
print('The answer for this question is :', num1+num2+num3)

