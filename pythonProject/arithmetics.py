class Arithmetics:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def addition(self):
        print(self.x+self.y)

    def subtraction(self):
        if self.x<self.y:
            print(self.y-self.x)
        else: print(self.x-self.y)

    def pythogoras(self):
        h=self.x**2+self.y**2
        p=float(h**(1/2))
        print(p)

i=Arithmetics(5,8)
i.addition()
i.subtraction()
i.pythogoras()