## Instructions
Create a zodiacSectionLN.py file.  This file will contain your solutions to the requirements below:

a. Ask the user to enter a year of birth.  The baseline year 1900.
b. Validate user input that it should not be earlier than 1900.
c. If the user enters an invalid year then display an appropriate message then stop or abort the program.

Example:
Enter your birth year: 1800
Invalid Year, it should not be earlier than 1900

d. Otherwise determine the chinese zodiac sign based on the following starting from 1900.  Note: A zodiac sign will recur after each 12 years.

i. Rat (鼠 / Shǔ)
ii. Ox (牛 / Niú)
iii. Tiger (虎 / Hǔ)
iv. Rabbit (兔 / Tù)
v. Dragon (龙 / Lóng)
vi. Snake (蛇 / Shé)
vii. Horse (马 / Mǎ)
viii. Goat (羊 / Yáng)
ix. Monkey (猴 / Hóu)
x. Rooster (鸡 / Jī)
xi. Dog (狗 / Gǒu)
xii. Pig (猪 / Zhū)

e. CONSIDER only the year of birth.

Example input and output:
Enter your birth year: 2000
Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)

## Code
a = int(input("Enter your birth year: "))

if a < 1900:
  print("Sorry, it is not an accepted input.")
else:
  b = (a - 1900) % 12
  if b == 0:
    print("Rat (鼠 / Shǔ)")
  elif b == 1:
    print("Ox (牛 / Niú)")
  elif b == 2:
   print("Tiger (虎 / Hǔ)")
  elif b == 3:
    print("Rabbit (兔 / Tù)")
  elif b == 4:
    print("Dragon (龙 / Lóng)")
  elif b == 5:
    print("Snake (蛇 / Shé)")
  elif b == 6:
    print("Horse (马 / Mǎ)")
  elif b == 7:
    print("Goat (羊 / Yáng)")
  elif b == 8:
    print("Monkey (猴 / Hóu)")
  elif b == 9:
    print("Rooster (鸡 / Jī)")
  elif b == 10:
    print("Dog (狗 / Gǒu)")
  elif b == 11:
    print("Pig (猪 / Zhū)")

## Screenshot
<img width="1162" height="107" alt="image" src="https://github.com/user-attachments/assets/39ceb6ea-5200-40a9-80be-14c7c0c9cc71" />
