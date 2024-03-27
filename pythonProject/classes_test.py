class Fruit:
    def __init__(self, name, color):
        self.name=name
        self.color=color

    def func(self):
        print(self.name+" is "+self.color)

f1= Fruit("Apple", "red")
f1.func()