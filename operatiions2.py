# with open('Codingal.txt','w') as file :
#     file.write('Hello, My name is Anjali!. I am 12 years old!')
# file.close()

# #  Split file into words
# with open('Codingal.txt','r') as file :
#     data=file.readlines()
#     print(' The Words in this file are.......')
#     for line in data :
#         word=line.split()
#         print(word)
# file.close()

# # Create a new file
# new_file = open('New_File.txt','x')
# new_file.close()

# Check if a file exists
# import os
# print('Checking if my_file exists or not.......')
# if os.path.exists('my_file.txt'):
#     os.remove('my_file.txt')
# else:
#     print('This file does not exist')

# # # create a new if it doesn't
 # my_file = open('my_file.txt','w')
# my_file.write('Hi! I am Anjali and I am 12 yars old!')
# my_file.close()

# # delete file named New_File
# import os
# os.remove('New_File.txt')

# Program to eliminate repeated lines from a file.

#  creating the output file
outputFile = open('UpdatedFile.txt','w')

# Reading the input file
inputFile = open('codingal.txt','r')

# Holds lines already seen
lines_seen_so_far = set()
print('Eliminating duplicate lines.......')

# itering each line in the file
for line in inputFile:
    # checking if line is unique
    if line  not in lines_seen_so_far:

        # Write unique ines in output file
        outputFile.write(line)

        #  adds unique lines to lines_seen_so_far

        lines_seen_so_far.add(line)

# closing the file
inputFile.close()
outputFile.close()

