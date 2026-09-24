class Plant:
    def __init__(self, name, age, color, height):
        self.Name = name
        self.Age = age
        self.Color = color
        self.__private_Height = height
        
    
    def Reproduce(self):
        baby_plant = f"baby {self.Name}"
        return baby_plant

    def Drink(self):
        print(f"{self.Name} is drinking or soaking up water.")

    def Grow(self, days):
        grow = days * 3
        self.__private_Height += grow
    
    def getHeight(self):
        return self.__private_Height

class Flower:
    def __init__(self, name, age, color, fragrance):
        super().__init__(name, age, color)
        self.Fragrance = fragrance
    
    def Bloomed_or_not(self):
        if self.Age >= 60:
            print("The flower has bloomed.")
        else:
            print("The flower has not bloomed yet.")
        
    def Grow(self, days):
        super().Grow(days)
        
        self.Age += days
        print(f"{self.Name} grew for {days} days. The age is now {self.Age}.")
