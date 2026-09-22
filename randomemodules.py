# # Write a program to generate a random integer and match it with the input given by the user?

# import random
# playing=True
# num=str(random.randint(0,9))
# print("Hello Player! Today you will be playing random number game. Basically, You guess the number the computer is thinking about. Good luckkk!")

# while playing:
#     guess=input("Please enter a number from 0,9 (your guess) " )
#     if guess==num:
#         print("Great Job You guessed the number!") 
#         break
#     else:
#         print("Aww Try again buddy!")

# #   Create a program to play rock, paper, and scissors. Use a random module to select from the given options Check whether the random guess matches the user’s answer  

# import random

# while True:
#     user=input("Enter a choice (rock, paper, scissors): ")
#     possible= ["rock", "paper" , "scissors ", ]
#     computer=random.choice(possible)
#     print(f"\nYou chose {user}, computer chose {computer}. \n")

#     if user==computer:
#         print(f"Both players have tied!")
#     elif user== "rock":
#         if computer== "scissors":
#             print("Rock smashes scissors! You winnn")
#         else:
#             print("Paper covers rock! You lose :(")
#     elif user == "paper":
#         if computer== "rock":
#             print("Paper covers rock! you winnn")
#         else:
#             print("Scissors cuts paper! You lose :(")
#     elif user=="scissors":
#         if computer == "paper":
#             print("Scissors cuts paper! You winnn")
#         else:
#             print("Rock smashes scissors! You lose :(")
#     play_again= input("Play again? (y/n): ")
#     if play_again != "y":
#             break

import math
print(math.ceil(45.26))
print(math.floor(45.26))
print(math.sqrt(16))
print(math.cbrt(8))
print(math.pow(3,4))
print(math.fabs(-85))
print(math.gcd(12,8))
print(math.factorial(5))



