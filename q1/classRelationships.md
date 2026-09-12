# Class Relationships: Association and Multiplicity
## Previous Work
[Part I - Classes and Objects](classObjectUML.md)
[Part II - Class Attributes and Methods](classAttributesMethods.md)
## Existing Class
Class: Plant
Description: The class contains different kinds of plants, their description and behaviour.
## New Related Class
Class: Insect
Description: The class contains different kinds of insects, their description and behavior.
## Association
Relationship: Plant HAS Insects
Explanation: There can be one to many insects in a plant that is beneficial, neutral or harmful.
## Multiplicity

Multiplicity: 1..*
Explanation: A plant could have an insects, few, or many depending on its condition and what type.
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
- 
### What multiplicity did you choose and why?
-
### How did you implement the relationship in Python?
-
### Why did you store an object reference instead of copying its data?
-
### If your relationship uses many, why is a list appropriate?
-
