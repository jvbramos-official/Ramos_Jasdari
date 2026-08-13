# Computational Thinking Exercise
## Smart School Canteen Queue

**Name:** Jasdari Vyel B. Ramos
**Section:** 9 - Platinum
**Date:** 8/12/2026

## Step 1: Identify the big problem
Main Problem: The PSHS school canteen system is poor and its operations are manual. This results in severe overcrowding during the 
lunch brakes of students with inefficient and slow lines piling over time. This may cause issues like the lack of time for eating
resulting in hunger and low energy among the students.

## Step 2: Identify three to four Sub-Problems
1. Students take a long time in choosing the food they want to buy.
2. The operation system is manual so the cashier has to manually calculate the total themselves give the change.
3. There is nothing that tracks the food supply and its amount in the given moment.

## Step 3: Define computational thinking approaches
| Long time selecting of food | Abstraction | Make the options less complex and more simple and easy to understand |
| Manual calculation | Algorithm Design | Create a system that is able to calculate the total and change automatically |
| Tracker of food supply | Pattern Recognition | Create a system that is able to track & recognize the patterns of the supply until it is almost near 0 or none|

## Step 4: Draw a flowchart or write a pseudocode
### Selected Sub-Problem
Manual calculation
### Pseudocode
``` START 
INPUT price_item
INPUT quantity 

price_total = price_item * quantity 
DISPLAY price_total

INPUT payment 

IF payment >= price_total 
  THEN change = payment - price_total
  DISPLAY change 
ELSE 
  DISPLAY "Not enough money" 

END

```
