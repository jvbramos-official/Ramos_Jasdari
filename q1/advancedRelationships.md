# Advanced Class Relationships
## Previous Activities
[classAttrib](classAttributesMethods.md)
[classRel](classRelationships.md)
## Existing System Description
1. What classes currently exist in your system?
Class 1: Plant Class 2: Insect
2. What problem or limitation exists in your current design?
Explain: The classes are too large and general. For example, plants could be a tree, have a flower, or be a shrub.
## Inheritance Relationship
Parent: Plant
Child: Flower
Explanation: Some plants are genotypes, which means the plant has flowers.
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Composition
Class containing another object: Flower
Contained object: Stamen
Explanation: A flower needs its stamen in order to reproduce.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Questions:
1. Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
- I chose "Flower" as my inheritance relationship to the parent class "Plant" because it satisfies the IS-A relationship. Additionally, a plant can have a flower or not. For example, a basil doesn't have a flower but a Rose Plant does.

2. How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
- Inheritance reduce duplicate codes by reusing data fields such as Name, Age, Color, Height that's been inherited from the Class Plant. These attributes is in class Plant which gets inherited by the child class Flower. These prevents duplicate codes through inheriting.
  
3. Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
- My HAS-A relationship is Composition because Stamen is directly tied with the Flower. This is because Stamen is the male reproductive part of the Flower and can't exist without it. Without a reproductive part, the pollen can't spread in order to reproduce.

4. What is the difference between Association from Part III and the advanced relationship you implemented?
- The Association from Part 3 is independent from each other while the advanced relationship inherits instead from a class. For example, the class Insect can independently exist and has its own data fields and methods. Child class Flower on the other hand is part of class Plant and inherits instead with additional attributes.
  
5. How does your design follow the DRY principle?
- My design follows the DRY (Don't repeat yourself) principle. It ensures that every unique piece of data or behavior is exactly made once in the source code. The structure of the code ensures it follows the DRY principle.
