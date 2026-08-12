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
