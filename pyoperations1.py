# # There are five trees in Jack's front yard. He checks each tree to find out how tall it is in inches and writes the height on a sheet of paper. Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?

# h_1=98
# h_2=94
# h_3=41
# h_4=96
# h_5=11

# sum= h_1+h_2+h_3+h_4+h_5
# avg= sum/5
# print('The average height of the trees are ...' , avg)

# Write a program to calculate the number of notes in the given amount?
amt= int(input('ENter the amount:'))
note100 = amt // 100
amt= amt %100
note50 = amt // 50
amt= amt %50
note20 = amt // 20
amt= amt %20
note10 = amt // 10
amt= amt %10
note5 = amt // 5
amt= amt %5
note1 = amt // 1

print('Notes of 100:  ', note100)
print('Notes of 50:  ', note50)
print('Notes of 20:  ', note20)
print('Notes of 10:  ', note10)
print('Notes of 5:  ', note5)
print('Notes of 1:  ', note1)




