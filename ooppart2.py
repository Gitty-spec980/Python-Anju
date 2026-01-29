#Write a Python class named Rectangle with a length and width and a method that computes the area of a rectangle. Display the dimensions and calculated area of the rectangle as well.
# class rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print("The length of the rectangle is ", self.length)
#         print("The width of the rectangel is ", self.width)
#         print("The area of the rectangle is ", self.length*self.width)

# ob1=rectangle(7,7)
# ob1.area()
        
# Write a Python class named Car that has the following data members:
# brand
# model
# mileage (distance traveled in km)
# fuel_used (fuel consumed in liters)

# The class should include:
# A method to calculate the fuel efficiency of the car (km per liter).
# A method to display the car’s brand, model, mileage, fuel used, and fuel efficiency.
# Create an object of the class and display the car details.
class car:
    def __init__(self,brand,model,mileage,fuel_used):
        self.brand=brand
        self.model=model
        self.mileage=mileage
        self.fuel_used=fuel_used
    def fuel_efficiency(self):
        return self.mileage/self.fuel_used
    def display(self):
        print("The brand is", self.brand)
        print("The model is ", self.model)
        print("The mileage is ", self.mileage)
        print("The amount of fuel used is ", self.fuel_used)
        print("The fuel efficiency is ", self.fuel_efficiency())
car1=car("Ford","Mustang",500,20)
car1.display()
