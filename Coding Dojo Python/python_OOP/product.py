# The owner of a store wants a program to track products. Create a product class to fill the following requirements.

# Product Class:
# Attributes:

# • Price

# • Item Name

# • Weight

# • Brand

# • Status: default "for sale"

class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

# • Sell: changes status to "sold"
    def sell(self):
        self.status = "sold"
        return self

# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
    def add_tax(self,tax):
        added_tax = self.price * tax
        total = added_tax + self.price
        return total
    
#Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.
    def Return(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in box":
            self.status = "For Sale"
        else reason == "box opened":
            self.status = "used"
            self.price = self.price * 0.8
        return self
    
# Display Info: show all product details.
    def display_info(self):
        print "price: $" + str(self.price)
        print "item name: " + str(self.item_name)
        print "weight: " + str(self.weight) + "lbs"
        print "brand: " + str(self.brand)
        print "status: " + str(self.status)
        return self