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