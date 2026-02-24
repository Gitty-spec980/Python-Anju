# #Open the file
# f=open('abc.txt','r')
# #modifying
# print(f.read())
# #close
# f.close()

# #Append
# f=open('abc.txt','a')
# f.write('nThe file is now opened in append mode.')
# f.write('\nThe old content will not be deleted')
# f.close()

# #Write
# f=open('abc.txt','w')
# f.write('\nThe file is opened in Write mode now')
# f.write('\nThe old content will be delted')
# f.close

# f=open('abc.txt','r')
# # #modifying
# print(f.read())
# # #close
# f.close()

#Print the total number of lines in the file
#Program to count number of lines in this file
#Opening a file
file = open("abc.txt","r")
counter = 0

#Reading from the file
content = file.read()
#splitting content into lines
#and storing them in a list
CoList = content.split("\n")

for i in CoList:
    if i:
        counter += 1

print("This is the number of lines in the file")
print(counter)

