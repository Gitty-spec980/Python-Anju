# a=67
# b=-67
# c=0

# if a and b and c:
#     print('All the numbers have a boolean value as True')
# else:
    # print('all the numbers have the boolean value as False')

# a=41
# b=-41
# c=0

# if a > 0 or b > 0:
#     print('Either of the numbers are greater than 0')
# else:
#     print('No number is greater than 0')

# if b > 0 or c > 0:
#     print('Either of the numbers are greater than 0')
# else:
#     print('No number is geater than 0')

# a=10
# b=12
# c=12

# print(not(b==c))
# print(not(a==b))


# a= "python"
# b="coding"

# if not (a==b):
#     print(a, 'and',b, 'are DIFFERENT')

# a= 7
# b=7

# if not ((a==1)==(b==5)):
#     print('Hello')

# a=int(input('Enter a number'))

# if not (a % 2 == 0):
#     print(a, 'is an odd number')

# BMI calculator

height = float(input('Enter your height in cm: '))
weight=float(input('Enter your weight in kg:'))

BMI = weight / (height/100)**2

print( f"Your BMI is {BMI:.2f}")

if BMI <= 18.4:
    print('You are underweight.')
elif BMI <= 24.9:
    print('You are healthy.')
elif BMI <=29.9:
    print('You are overweight.')
elif BMI <=34.9:
    print('you are everly overweight.')
elif BMI <= 39.9:
    print('You are obese.')
else:
    print('You are severley obese.')