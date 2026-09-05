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
Plant2 = Plant("Fern", 3, "Yellow", 10)

print("---BEFORE---")
print(f"Plant1 = Name: {Plant1.Name}, Age: {Plant1.Age}, Color: {Plant1.Color}, Height: {Plant1.getHeight()}")
print(f"Plant2 = Name: {Plant2.Name}, Age: {Plant2.Age}, Color: {Plant2.Color}, Height: {Plant2.getHeight()}")

print("Performing action on Object 1...")

Plant1.Grow(5)

print("---AFTER---")
print(f"Plant1 = Name: {Plant1.Name}, Age: {Plant1.Age}, Color: {Plant1.Color}, Height: {Plant1.getHeight()}")
print(f"Plant2 = Name: {Plant2.Name}, Age: {Plant2.Age}, Color: {Plant2.Color}, Height: {Plant2.getHeight()}")
