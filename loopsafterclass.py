n = int(input("Enter number!:  "))

for i in range(1, n + 1):
    exponent = i ** i
    if i < n:
        print(exponent, end=", ")
    else:
        print(exponent)