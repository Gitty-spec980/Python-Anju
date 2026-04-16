# import keyword


# print('Python keywords are....\n')
# print(keyword.kwlist)

#Given a list of integers, count how many numbers are positive, how many are negative, and how many are zero.
#nums = [-1, 2, 3, -4, 0, 5, -6, 7]
nums = [-1, 2, 3, -4, 0, 5, -6, 7]
num_p= 0 
num_n= 0
num_zero= 0

for i in nums:
    if i >0:
        num_p = num_p+1
    elif i <0:
        num_n = num_n+1
    else:
       num_zero = num_zero+1
print("The total amount of positive numbers is " , num_p)
print('The total amount of negetive numbers is ', num_n)
print('The total amount of the number(s) zero is ' , num_zero)


