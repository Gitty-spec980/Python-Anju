# # Write a program to create a class Parrot and perform the following tasks - Create a class variable species, Create a constructor that has instance variables - name and age, Create instances of class Parrot, passing arguments as well, Print Class variable by accessing it, Print Instance variables as well.


# class Parrot:
# # class attributes
#     species = "bird"


# #instance attribute

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# #instantiate the Parrot Class
# ob1 = Parrot("Chirpy", 10)
# ob2 = Parrot("Harlow", 15)

# # access the class attributes
# print("Chirpy is a {}".format(ob1.species))
# print("Harlow is also a {}".format(ob2.species))

# #access the instance attributes
# print("{} is {} years old".format(ob1.name, ob1.age))
# print("{} is {} years old".format(ob2.name, ob2.age))



#Write a program to create a class Parrot and perform the following tasks - Create a class variable species, Create a constructor that has instance variables - name and age, Create instance methods for this class named sing and dance, making them print a message. Create instances of class Parrot, passing arguments as well, Print Class variable by accessing it, Print Instance variables as well.

class Parrot:
    species="bird"
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def sing(self, song):
        return "{} sings {} ".format(self.name,song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)
#instantiate the object
ob = Parrot("Blu", 10)

#call our instance methods
print(ob.sing("Big Girls Dont Cry"))
print(ob.dance())

        
        





