# row=int(input("Enter the number of rows"))
# for i in range(1, row+1):
#     for j in range(1,i+1):
#         print("*", end="  ")
#     print("\n")

#Revresed version of right angle triangle:

# row=int(input("Enter the number of rows"))
# for i in range(row,0,-1):
#     for j in range(i,0,-1):
#         print("*", end="  ")
#     print("\n")

# # Outline:
# Write a program to find out the denominations of notes of 2000, 500, 200, 100, 50, 20, and 10 for the total amount of money entered by the user. 

d=[2000, 500, 200, 100, 50, 20,10]
amt=int(input("Enter the amount:"))
for note in d:
    count=amt//note
    amt=amt%note
    if count!=0:
       print("No of Notes in {}: {}".format(note,count))