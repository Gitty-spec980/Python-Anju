class circle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("The length of the circle is ", self.length)
        print("The width of the circle is ", self.width)
        print("The area of the circle is ", self.length*self.width)

ob1=circle(7,7)
ob1.area()