# try:
#     num=int(input("Please enter a number "))
#     print (num)
# except ValueError as ex:
#     print(ex)

# try:
#     num1=int(input("Please enter the first number "))
#     num2=int(input("Please enter the second number "))
#     answer=num1/num2
#     print(answer)
# except ZeroDivisionError as ze:
#     print("Division By zero is an error")
# except ValueError as ve:
#     print("Please input a valid whole number")
# except:
#     print("Wrong input")
# else:
#     print("No exceptions")
# finally:
#     print("This code will execute no matter what")

valid=False
while not valid:
    try:
        num=int(input("Please enter a number "))
        while num%2==0:
            print("BYE!!")
        valid = True
    except ValueError:
        print("Invalid")
    
    
    


