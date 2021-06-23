import datetime

now = datetime.datetime.now()
age = input("type in your age: ")
name = input("type in your name: ")
print("OMG " + name + ", you are " + age + " years old so you were born in " + str(now.year-int(age)) + \
      " or " + str(now.year-int(age)-1))