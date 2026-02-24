def is_disarium(num):
    
    num_str = str(num)
    length = len(num_str)
    total = 0

    
    for i in range(length):
        digit = int(num_str[i])
        total += digit ** (i + 1)  

    return total == num  


try:
    
    user_input = int(input("Enter a number:): "))

    
    if is_disarium(user_input):
        print(f"{user_input} Great Job! This is a Disarium number ")
    else:
        print(f"{user_input} OOPSS This NOT a Disarium number")

except ValueError:
    print("Invalid input enter a NUMBER!.")