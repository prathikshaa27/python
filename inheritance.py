class Animal:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
class Dog(Animal):
    def sound(self):
        print(f"He is {self.name} his breed is {self.breed} and he barks")
dog1 = Dog("Mike","Dalmation")
dog2 = Dog("Tucker","Golden retriever")

dog1.sound()
dog2.sound()

#multiple inheritance
class Click:
    def click(self):
        print("You have clicked")
class Drag:
    def drag(self):
        print("You have dragged")

class Button(Click,Drag):
    def button(self) :
        print("Button uses the method in from the two parent class")
button1 = Button()
button1.click()
button1.drag()
button1.button()