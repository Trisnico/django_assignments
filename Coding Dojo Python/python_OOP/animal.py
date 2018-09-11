class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def DisplayInfo(self):
        print "Name: " + str(self.name)
        print "Vitals: {} points".format(self.health)

    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self 

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10 
        return self
    def DisplayInfo(self):
        print "This is a dragon" 
        super(Dragon, self).DisplayInfo()



animal = Animal('Garfield')
animal.walk().walk().walk().run().run().DisplayInfo()

dog = Dog('Odie')
dog.walk().walk().walk().run().run().pet().DisplayInfo()

dragon = Dragon('Nightwing')
dragon.fly().DisplayInfo()