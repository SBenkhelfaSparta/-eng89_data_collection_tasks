age = input("enter your age: ")
while True:
    try:
        int(age)
        print(age)
        break
    except ValueError:
        age = input("you messed up, please try again: ")