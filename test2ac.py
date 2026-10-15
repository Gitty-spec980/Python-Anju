
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("FUNCTION CALCULATOR")


try:
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
  
    operation = input("Choose an operation (add, subtract, multiply, divide): ").strip().lower()
    
   
    if operation == "add":
        result = add(num1, num2)
        print(f"Result!: {result}")
    elif operation == "subtract":
        result = subtract(num1, num2)
        print(f"Result: {result}")
    elif operation == "multiply":
        result = multiply(num1, num2)
        print(f"Result: {result}")
    elif operation == "divide":
        result = divide(num1, num2)
        print(f"Result: {result}")
    else:
      
        print("Unknown operation.")


except ValueError:
    print("Error: Please enter numbers only.")


except ZeroDivisionError:
    print("Error: Cannot divide by zero.")


finally:
    print("Thank you for using FUNCTION CALCULATOR!")
