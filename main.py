names = []
while True:
    name = input("What is your first name? ")
    names.append(name.strip().capitalize())
    print("Welcome", name.strip().capitalize(), ":)")
    response = input("Would you like to enter another name? (y/n)  ")
    if response.upper() != 'Y':
        break;

print("Names saved: ", names)

full_name = "John Smith"
full_name = input("Please enter your full name: ")
Full_Name = ""
for x in full_name.split():
    Full_Name += (x.strip().capitalize() + " ")

print("Welcome to Pycharm, {}!".format(Full_Name.strip()))