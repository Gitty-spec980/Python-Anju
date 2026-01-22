# Write a Python program that takes a name as an input from the user and then creates a function that accepts the same name as a parameter and greets the user.

# def greet(fname):
#     print("Hello",fname,",Good evening")
# n=input("Enter A Name:")
# greet(n)

# Write a Python program that takes any word as an input from the user and then creates a function that accepts the same word as a parameter and checks whether it is a palindrome or not. (Palindrome word is the same when read in both directions - forward or backward. Example - racecar)

def isPalindrome(str):
    lp=0
    rp=len(str)-1

    while rp>=lp:
        if not str[lp]==str[rp]:
            return False
        lp=lp+1
        rp-=1
    return True
enyphen=input("Enter a Word")
print("is this a Palindrome")
print(isPalindrome(enyphen))    

