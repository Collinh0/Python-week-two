class Product:
# class attributes
    date_stocked = "Jan 1st, 2023" 
    payment_method = "Cash" 

    # instance attributes 
    def __init__(self, name, serial_number, unit_price, quantity, value_added_tax, expiry_date):
    
        self.name = name
        self.serial_number = serial_number
        self.unit_price = unit_price
        self.quantity = quantity
        self.value_added_tax = value_added_tax
        self.expiry_date = expiry_date

"""
Discuss a scenario related to products where you might think an attribute should be an instance attribute, but upon further consideration,
 realize it would be better as a class attribute (or vice versa).
 Explain your reasoning.
"""
#VAT -> its an instance attribute because it is unique to each product but also is a normally-fixed-rate (16%) for all products so can pass to be a class attribute
   
product1 = Product("Milk", "SN001", 55, 10, 0.16, "2025-12-31")
product2 = Product("Bread", "SN002", 60, 20, 0.16, "2025-12-30")
product3 = Product("Sugar", "SN003", 100, 5, 0.16, "2025-12-11")
product4 = Product("Flour", "SN004", 120, 15, 0.16, "2025-12-01")

"""
When might you want a class attribute in the Product class (like a tax rate) to be mutable?
 What are the potential implications or side effects in your inventory system if this mutable class attribute is changed while product objects exist?
When might you want an instance attribute of a Product (like a unique product ID) to be immutable once the object is created?
How would you ensure immutability (or a strong convention of it) for such an attribute in your chosen programming language?
"""
#date_stocked -> initial stocking is done at once for all products,but the products sell out at diffrent times so the need to restock at different intervals
#potential implications -> if the date is changed, it will affect the inventory system as it will not be able to track the restocking of products accurately(imbalance of books)

#ensure immutability -> store the class attr as a tupple
date_stocked = ("Jan 2nd, 2023", "Jan 2nd, 2023", "Jan 2nd, 2023")  

#Instance vs. Class Methods:
 #Instance -> discount.  Discount varies among the products