"""
Anthony Quinn X00138635
30/11/2020
Looping / Nested Loops Lab 8 Exercises
"""

# Exercise 1
"""
lowerEntry = 50
higherEntry = 100
counter = 50

# COUNT TO 100 FROM 50 USING 'WHILE'

while counter <= higherEntry:
    print(counter)
    counter += 1

# COUNT TO 100 FROM 50 USING 'FOR'

for counter in range(50,101):
    print(counter)
    counter += 1
"""

# Exercise 2
"""
counter = 0
total = 0

for counter in range(5):
    number = float(input("Input a number: "))
    counter += 1
    total += number

print(total)
"""

# Exercise 3
"""
maximum = 20
even_total = 0
odd_total = 0
for number in range(1, maximum):
    if(number % 2 == 0):
        even_total = even_total + number
    else:
        odd_total = odd_total + number
print("The sum of even numbers from 1 to 20 is:", even_total)
print("The sum of odd numbers from 1 to 20 is:", odd_total)
"""

# Exercise 4
"""
euro = 1
total = 0
total_euro = 0
yen_rate = 124.15

while euro != 0:
    print("Enter 0 to cancel/reset!")
    euro = float(input("Euros: "))
    total_euro += euro
    conversion = euro * yen_rate
    total += conversion
print("Total yen after conversion rate applied is: ", round(total, 2))
print("Total euro is: ", round(total_euro, 2))
"""

# Exercise 5
"""
startingNumber = int(input("Enter the starting number: "))
endingNumber = int(input("Enter the end number: "))
step = int(input("Enter how much each step should increase: "))
total = 0

if step != 0:
    while startingNumber <= endingNumber:
        print(startingNumber)
        startingNumber += step
        total += startingNumber
    print(total)
else:
        print("Invalid step value! Must be greater than 0!")
"""












