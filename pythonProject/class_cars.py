class Cars:
    def __init__(self, name, speed, mileage):
        self.name=name
        self.speed=speed
        self.mileage=mileage

    def carname(self):
        print(self.name)

    def mileage_scam(self):
        print(self.mileage*10)

c=Cars("Sleeper", 420, 250000)
c.carname()
c.mileage_scam()