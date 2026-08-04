# # Write a program to demonstrate a right angle triangle pattern?
# print("RIght Angle Triangle Pattern!")

# rows= int(input("Please Enter the number of rows: "))
# for i in range(rows):
#     for j in range( i+1):
#         print("&", end=" ")
#     print()
# # Write a program to demonstrate a Floyd triangle pattern?

# rows= int(input("Please Enter the number of rows: "))
# num = 1
# for i in range(0,rows +1):
#     for j in range( i+1):
#         print(num, end=" ")
#         num += 1
#     print()
# Write a program to demonstrate the numbers in a diamond pattern?
rowSize= int(input("Enter the number of rows: "))
if rowSize%2==0:
    halfDiamRow=int(rowSize/2)
else:
    halfDiamRow=int(rowSize/2)
space = halfDiamRow-1

for i in range(1, halfDiamRow+1):
    for j in range(1, space+1):
        print(end=" ")
    space= space-1
    num=1
    for j in range(2*i-1):
        print(end= str(num))
        num=num+1
    print()
space=1
for i in range(1, halfDiamRow):
    for j in range(1, space+1):
        print(end=" ")
    space = space+1
    num=1
    for j in range(1,2*(halfDiamRow-i)):
        print(end=str(num))
        num=num+1
    print()
