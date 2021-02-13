"""
File name: MyFirstPyhtonProgram.py
Date: 12-02-2021
Reason: Python Workshop
Author: Santhosh
Version: 0.1
Version History:
Date: 13 Feb 2021 @ Time
"""
import random
import math

'''print("Hello World")
x = int(input("Enter a Number"))
print("Entered Number is:",x)'''

y = random.randint(1,10)
print(f'y is {y}')
while y:   # while y is True
  rad = random.randint(0,3)
  print(f"Sine of {rad} is {math.sin(rad)}")
  y = y - 1

# End of Code
