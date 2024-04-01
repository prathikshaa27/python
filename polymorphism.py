class Person:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def duty_of_perosn(self):
        print(f"My name is {self.name} and Iam from Coimbatore")

class Family(Person):
    def duty_of_perosn(self):
        print(f"Hi Iam {self.name} and iam daugher to my parents and sister to my brother")

class Office(Person):
    def duty_of_perosn(self):
        print(f"Hi Iam {self.name} and Iam collegaue to my co-workers")

class Friends(Person):
    def duty_of_perosn(self):
        print(f"Hi Iam {self.name} and Iam a friend to my friends")
perosn=Person("prathi","meidum")
perosn1 = Family("prathi","medium")
perosn2= Office("prathi","medium")
perosn3 = Friends("prathi","medium")

perosn.duty_of_perosn()
perosn1.duty_of_perosn()
perosn2.duty_of_perosn()
perosn3.duty_of_perosn()



