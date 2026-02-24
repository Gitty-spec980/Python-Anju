# open a file
# file = open('xyz.txt', 'r')

# # read and print the contents of the file
# print(file.read())

# print("Coding is basically the computer language used to develop apps, websites, and software. Without it, we’d have none of the most popular technology we’ve come to rely on such as Facebook, our smartphones, the browser. It all runs on code.To put it very simply, the code is what tells your computer what to do. To go a bit deeper, computers don’t understand words. They only understand the concepts of on and off.  Binary code represents these on and off signals as the digits 1 and 0. In order to make binary code manageable, computer programming languages were formed. ")
# f.close()

f = open('xyz.txt','w')

f.write("Coding is basically the computer language used to develop apps, websites, and software. Without it, we’d have none of the most popular technology we’ve come to rely on such as Facebook, our smartphones, the browser. It all runs on code.To put it very simply, the code is what tells your computer what to do. To go a bit deeper, computers don’t understand words. They only understand the concepts of on and off.  Binary code represents these on and off signals as the digits 1 and 0. In order to make binary code manageable, computer programming languages were formed. ")
f.close()

f = open('xyz.txt','a')
f.write('My favorite subject is social studies:).')
f.close()
