class Plant:
    def __init__(self, name, age, color, height):
        self.Name = name
        self.Age = age
        self.Color = color
        self.__private_Height = height
        
        self.host_Insects = []
    
    def Reproduce(self):
        baby_plant = f"baby {self.Name}"
        return baby_plant

    def Drink(self):
        print(f"{self.Name} is drinking or soaking up water.")

    def Grow(self, days):
        grow = days * 3
        self.__private_Height += grow
 
    def Add_Insect(self, insect_obj):
        self.host_Insects.append(insect_obj)
    
    def getHeight(self):
        return self.__private_Height


class Insect:
  def __init__(self, name, type, color, age):
    self.Name2 = name
    self.Type2 = type
    self.Color2 = color
    self.__private_Age2 = age
    
  def Reproduce(self):
      baby_insect = f"baby {self.Name2}"
      return baby_insect

  def Grow(self, Days):
      grow = Days * 2
      self.__private_Age2 += grow
    
  def getAge2(self):
      return self.__private_Age2
      
  def Crawl(self):
      print("The insect is crawling.")

print("--- BEFORE RELATIONSHIP ---")
Plantt = Plant("Basil", 2, "Green", 5)
Insect1 = Insect("Aphid A", "Harmful", "Yellow", 5)
Insect2 = Insect("Aphid B", "Harmful", "Yellow", 6)
Insect3 = Insect("Ladybug", "Beneficial", "Red/Black", 12)

print(f"Plant created: {Plantt.Name}, Insects hosted: {len(Plantt.host_Insects)}")
print(f"Insects living independently: {Insect1.Name2}, {Insect2.Name2}, {Insect3.Name2}")


print("\n--- BUILDING RELATIONSHIP ---")
print(f"Adding insects to the {Plantt.Name} plant...")
Plantt.Add_Insect(Insect1)
Plantt.Add_Insect(Insect2)
Plantt.Add_Insect(Insect3)


print("\n--- AFTER RELATIONSHIP ---")
print(f"Plant: {Plantt.Name}, Height: {Plantt.getHeight()} cm")
print("Related object(s):")
for bug in Plantt.host_Insects:
    print(f"Insect Name: {bug.Name2}, Type: {bug.Type2}, Age: {bug.getAge2()} days")
