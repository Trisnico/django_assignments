class Bicycle(object):
    def __init__(self, miles, max_speed, price):
        self.miles = miles
        self.max_speed = max_speed
        self.price = price

myBicycle = Bicycle("15lbs", 2, "$95")
print myBicycle.num_wheels