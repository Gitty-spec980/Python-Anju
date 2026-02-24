
class anjali: pass

class anjali:
    def __init__(self, name, color):
        self.name = name
        self.color = color


    def intro(self):
        print("hello, I am", self.name)


human = anjali('Anjali','Light blue')

human.intro()