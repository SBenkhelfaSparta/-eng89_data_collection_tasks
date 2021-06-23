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