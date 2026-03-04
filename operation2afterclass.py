# with open('Afterclass.txt','w') as file :
#     file.write('Hewo! This is my after class project fro operations 2!')
# file.close()

# #  Split file into words
# with open('Afterclass.txt','r') as file :
#     data=file.readlines()
#     print(' This is the content in the file :')
#     for line in data :
#         word=line.split()
#         print(word)
# file.close()

# Create a new file
# new_file = open('My_File.txt','x')
# new_file.close()
# Check if a file exists
# import os
# print('Checking if My_file exists or not.......')
# if os.path.exists('mM_file.txt'):
#     os.remove('My_file.txt')
# else:
#     print('This file does not exist')

# # # create a new if it doesn't
 # My_file = open('My_file.txt','w')
# My_file.write('Hewo again! This is my after class prject!')
# My_file.close()

# # # delete file named New_File
# # import os
# # os.remove('My_File.txt')

# # Program to eliminate repeated lines from a file.

# #  creating the output file
# outputFile = open('UpdatedFile.txt','w')

# # Reading the input file
# inputFile = open('Afterclass.txt','r')

# # Holds lines already seen
# lines_seen_so_far = set()
# print('Eliminating duplicate lines.......')

# # itering each line in the file
# for line in inputFile:
#     # checking if line is unique
#     if line  not in lines_seen_so_far:

#         # Write unique ines in output file
#         outputFile.write(line)

#         #  adds unique lines to lines_seen_so_far

#         lines_seen_so_far.add(line)

# # closing the file
# inputFile.close()
# outputFile.close()

