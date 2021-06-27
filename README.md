# All my coding tasks

## Calculator
```python
class Calculator:

    def add(self, x, y):
        return x+y

    def subtract(self, x, y):
        return x-y

    def divide(self, x, y):
        return x/y

    def multiply(self, x ,y):
        return x*y
```
## Advanced Calculator
```python
from calculator import Calculator
import math

class Functional_calculator(Calculator):

    def __init__(self):
        super().__init__() #get all of calculator's methods

    def circle_area(self, r):
        return math.pi*(r*r) #pi r squared

    def square_area(self, x):
        return x*x #x squared

    def triangle_area(self, x, h):
        return 0.5*x*h #half base times height
```
## Age & Permission
```python
class AgeCheck:
    age = 19
    drivers_licence = True

    def loop(self):
        while True:
            self.age = input("Please enter your age: ")
            if(self.age.lower() == "exit"):
                break
            self.drivers_licence = input("Please enter your age: ")
            if (self.drivers_licence.lower() == "exit"):
                break

            if(self.age >= 18):
                if(self.drivers_licence == True):
                    print("You can vote and drive")
                else:
                    print("You can vote but can't drive")
            elif(16 <= self.age < 18):
                print("You can't legally drink but your mates/uncles might have your back")
            else:
                if(self.drivers_licence == True):
                    print("You can't vote but you can drive")
                else:
                    print("You're too young, go back to school!")
```
## Age Check
```python
age = input("enter your age: ")
while True:
    try:
        int(age)
        print(age)
        break
    except ValueError:
        age = input("you messed up, please try again: ")
```
## Fizzbuzz
```python
def fizzbuzz(fizz, buzz):
    for fizzbuzz in range(100):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print(fizz+buzz)
            continue
        elif fizzbuzz % 3 == 0:
            print(buzz)
            continue
        elif fizzbuzz % 5 == 0:
            print(buzz)
            continue
        print(fizzbuzz)

fizzbuzz("beep", "boop")
```
## Loop example
```python
for i in range(10):
    print("Hello")

names = []
while True:
    name = input("What is your first name? ")
    names.append(name.strip().capitalize())
    print("Welcome", name.strip().capitalize(), ":)")
    response = input("Would you like to enter another name? (y/n)  ")
    if response.upper() != 'Y':
        break;

list_names_lower = []
for i, x in enumerate(names):
    list_names_lower.append(names[i].lower())
    if (len(names[i])%2==0):
        print("name " + str(i) + " is even")
    else:
        print("name " + str(i) + " is odd")
```
## Guess what year you were born
```python
import datetime

now = datetime.datetime.now()
age = input("type in your age: ")
name = input("type in your name: ")
print("OMG " + name + ", you are " + age + " years old so you were born in " + str(now.year-int(age)) + \
      " or " + str(now.year-int(age)-1))
```