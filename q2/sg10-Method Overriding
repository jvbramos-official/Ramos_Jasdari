#creates a class
class Animal:
    #data field "name" is in the class Animal
    def __init__(self, name):
        #privates name using "__"
        self.__name = name
    
    #gets the datafield name
    @property
    def name(self):
        return self.__name
        
    def eat(self):
        print(self.name, "mga yummy")
        
    def make_sound(self):
        print(self.name, "its da noise")
        
#creates child class Lion
class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    #overrides the inherited method (same for every other method/behavior of the animals)
    def make_sound(self):
        print(self.name, "roars loudly!")
        
    def eat(self):
        print(self.name, "eats fresh meat.")
            
    def drink(self):
        print(self.name, "drinks by the river.")

#creates child class Elephant
class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def make_sound(self):
        print(self.name, "trumpets!")
        
    def eat(self):
        print(self.name, "eats grass and fruits.")
        
    def drink(self):
        print(self.name, "drinks by the lake.")

#creates child class Monkey
class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def make_sound(self):
        print(self.name, "chatters!")
        
    def eat(self):
        print(self.name, "eats banana.")
            
    def drink(self):
        print(self.name, "drinks the juice of the fruit.")

#creates objects
lion1 = Lion("Simba")
elephant1 = Elephant("Dumbo")
monkey1 = Monkey("George")

#lists them#
animals = [lion1, elephant1, monkey1]

#calls them using for loop"
print("=--------------=")
for animal in animals:
    animal.make_sound()
    animal.eat()
    animal.drink()
    print("=--------------=")
