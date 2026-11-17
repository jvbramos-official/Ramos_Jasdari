#1. a. Duck typing allows objects to be treated as a certain type as long as they have the minimum necessary attributes and methods that follow the requirement.
    #It allows to achieve polymorphism without using inheritance.

   #b. The car needs to have the "speak method" in order to work inside the same loop. This is because the object must follow the minimum method requirement.
      #The previous method was "honk", which does not follow the same method in the loop. This results the output to have an error.

#2. Code:
class Car:
  def move(self):
    print("The car drives on the road. ")

  def start_trip(self, vehicle):
    vehicle.move()
    
class Boat:
  def move(self):
    print("The boat sails on water. ")

  def start_trip(self,vehicle):
    vehicle.move()

class Drone:
  def move(self):
    print("The drone flies in the sky. ")

  def start_trip(self, vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

print("=-------------------------=")
print("Output:\n")
vehicles = [car1, boat1, drone1]
for vehicle in vehicles:
  vehicle.start_trip(vehicle)
print("=-------------------------=")

#3. The code demonstrated polymorphism because it shows how a single method can be used by different distinct classes that produces its own individual outputs.
    #For instance, the 3 classes (Car, Boat, Drone) responds differently to the same method "speak".
