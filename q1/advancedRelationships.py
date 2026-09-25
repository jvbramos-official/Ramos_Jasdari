
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
    
Plant1 = Plant("Basil", 2, "Green", 5)

print("Parent Attribute:")
print(f"Height = {Plant1.getHeight()}")
print("-")

class Stamen:
    def __init__(self, countpollen=676):
        self.PollenCount = countpollen

    def ReleasePollen(self):
        if self.PollenCount > 0:
            self.PollenCount -= 367
            return "= Pollen is everywhere now. ="
        else:
            return "No more pollen left :c."


class Flower(Plant):
    def __init__(self, name, age, color, height, fragrance):
        super().__init__(name, age, color, height)
        self.Fragrance = fragrance
        
        self.stamen_part = Stamen(countpollen=676)
        
    def Grow(self, days):
        super().Grow(days)
        self.Age += days
        print(f"{self.Name} grew for {days} days. The age is now {self.Age}.")


Flower1 = Flower("Rose", 4, "Red", 10, "Damask")

print("Child Object:")
print(f"Name: {Flower1.Name}")
print(f"Height: {Flower1.getHeight()}")
print("-")

print(f"Object: {Flower1.Name}")
print(f"Pollen Count before: {Flower1.stamen_part.PollenCount}")
    
spread = Flower1.stamen_part.ReleasePollen()
print(spread)
    
print(f"Pollen Count now: {Flower1.stamen_part.PollenCount}")
