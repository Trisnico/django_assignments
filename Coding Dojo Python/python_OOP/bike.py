class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayinfo(self):
        print "Price is: $" + str(self.price)
        print "Max Speed: " + str(self.max_speed) + "mph"
        print "Total mile: " + str(self.miles) + " miles"

    def drive(self):
        print "Riding"
        self.miles += 10
    
    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.max_speed -= 5

bike1 = Bike(100, 15)
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()
bike1.displayinfo()

bike2 = Bike(200, 40)
bike2.drive()
bike2.drive()
bike2.reverse()
bike2.reverse()
bike2.displayinfo()

bike3 = Bike(300, 20)
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayinfo()