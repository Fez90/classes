# Creating and using a class
# Each instance created from the Dog class will store a name and an age , and we'll give each dog the ability to sit() and roll_over()
class Dog:
    """A simple attemt to model a dog"""
    def __init__(self,name,age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over")
# Making an Instance from a Class
my_dog = Dog('Willie',6)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
# Accessing Attributes using dot notation my_dog.name//
# calling methods
# after we create instance form the class Dog, we can use dot notation to call any method defined in Dog. Let's make our dog sit and roll over//
my_dog.sit()
my_dog.roll_over()
# to call a method, give the name of the instance(in this case,my_dog)//

# Creating multiple instances
# you can create as many instances from a class as you need.Second dog your_dog//
my_dog = Dog('Willie',6)
your_dog = Dog('Lucy',3)
print(f"\nMy dog name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
print(f"Your dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()

# Working with Classes and Instances
# Modify the attributes associated with a particular instance, you can write methods thats update attributes in specific ways
# Example: Car Class
class Car:
    """A simple attempt to represent a car"""
    def __init__(self,make,model,year):
        """Initialize attribites to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self,mileage):
        """Set the odometer reading to the given value"""
        """Reject the change if it attemts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    
    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

my_new_car = Car("audi",'a4','2019')
print(my_new_car.get_descriptive_name())
# Setting a Default Value for an Attribute//
# When instance is created attributes can be defined without changing parameters.These atrributes can be defined in _init_ method.Let's add AttributeErrorcalled odometer_readingthat always starts with value 0/
my_new_car.read_odometer()
# Modifying Attribute Values
# Three ways to modify: 1 - directly through an instance, 2 - set a value through a method, 3 - increment the value (add certain amount to it) throuhg a method
# 1 Modifying an Attributes Value Directly
# my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# 2 Modifying an Attributes Value Through a Method.
my_new_car.update_odometer(50)
my_new_car.read_odometer()
# Update to make shure no one tries to roll back odometer
# 3 Modifying an Attributes Value Through a Method
my_used_car = Car('subaru','outback', 2015)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
# Inheritance. You can inherit a class from a main Class (parent class),inherit class called child class
# 
# The _init_()Method for a child class
# When writing a new class based on existing class you want to call _init_() method form parent class.This will initializa any attributes that were defined in parent _init_() method.
# Example Electricclass based on Car class

# Instances as Attributes
# When modeling something from the real world in code you may find that you're adding more and more detail to a class, you'll have growing class of attributes and methods. In this situation you can break a Class in different subClasses
# Breaking BatteryClass from a Electricclass
# Adding method that reports range of the car based on battery size

class Battery:
    """A simple attemt to model a battery for electric car"""
    def __init__(self,battery_size=75):
        """Initialize battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing battery size"""
        print(f"This car has {self.battery_size} kwh")

    def get_range(self):
        """Print statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self,make,model,year):
        """Initialize attributes of the parent class"""
        super().__init__(make,model,year)
        self.battery = Battery()
    
    def describe_battery(self):
        """Print statement describing battery size"""
        print(f"This car has a {self.battery_size} kwh battery")

    def fill_gas_tank(self):
        """Electric cars don't have gas tank"""
        print("This car doesn't need a gas tank!")
my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
# Defining Attributes and Methods for the Child Class//
# Adding attributes that's specific to ElectricCar class, battery attribute example
# my_tesla.describe_battery()
# Overiding methods form the Parent Class
# Say the Class Car had a method called fill_gas_tank().This method is meaningless to an all electric vehicles,so you might override this method lene #107
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()