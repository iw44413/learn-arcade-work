import arcade
import random
done = False
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and outrun the natives!")
def main():
    Miles_traveled = 0.0
    Thirst = 0.0
    Camel_tiredness = 0.0
    Distance_natives_traveled = -20.0
    Drinks_in_canteen = 3
    done = False
    while not done:
        done = True
        print("1. Drink from your canteen.")
        print("2. Ahead moderate speed.")
        print("3. Ahead full speed.")
        print("4. Stop for the night.")
        print("5. Status check.")
        print("6. Quit")
        choice = int(input("You Have 6 options. What is your Choice "))
        # option 1
        if choice == 1 and Distance_natives_traveled < Miles_traveled:
            Thirst = 0
            if Drinks_in_canteen > 0:
                Drinks_in_canteen = Drinks_in_canteen - 1
            else:
                print("Your Canteen is empty!!!!")
            done = False
        # option 2
        elif choice == 2 and Distance_natives_traveled < Miles_traveled:
            Miles_traveled = Miles_traveled + random.randrange(5, 13)
            Thirst = Thirst + 1
            Camel_tiredness = Camel_tiredness + 1
            print(Miles_traveled)
            done = False
            oasis = random.randrange(0, 21)
            if oasis == 4:
                Camel_tiredness = 0
                Drinks_in_canteen = 3
                Thirst = 0
                print("You found an Oasis!!!!!!!")
        #option 3
        elif choice == 3 and Distance_natives_traveled < Miles_traveled:
            Miles_traveled = Miles_traveled + random.randrange(10,21)
            Thirst = Thirst + 1
            Camel_tiredness = Camel_tiredness + random.randrange(1,4)
            Distance_natives_traveled = Distance_natives_traveled + random.randrange(7, 15)
            print("Miles traveled",Miles_traveled)
            oasis = random.randrange(0, 21)
            if oasis == 4 and Thirst < 4:
                Camel_tiredness = 0
                Drinks_in_canteen = 3
                Thirst = 0
                print("You found an Oasis!!!!!!!")
            done = False
        # option 4
        elif choice == 4 and Distance_natives_traveled < Miles_traveled:
            print("stopped for the night")
            Camel_tiredness = 0
            print("Camel is happy")
            Distance_natives_traveled = Distance_natives_traveled + random.randrange(7,15)
            done = False
        #option 5
        elif choice == 5 and Distance_natives_traveled < Miles_traveled:
            print("Status")
            print("Miles Traveled", Miles_traveled)
            print("Drinks in canteen", Drinks_in_canteen)
            print("The natives are", Miles_traveled - Distance_natives_traveled,"miles behind you")
            print(Distance_natives_traveled)
            done = False
        #option 6
        elif choice == 6:
            print("You have Quit the game. GG")
            done = True
        else:
            print("Enter valid option")
            done = False
        if Thirst == 5 and Camel_tiredness <= 8 and Miles_traveled < 200:
            print("You are thirsty!")
        elif Thirst > 5:
            print("You have died of thirst")
            done = True
        if Camel_tiredness > 5 and Thirst < 5:
            print("Your camel is tired")
        elif Camel_tiredness >8:
            print("Your camel died. GG")
            done = True
        elif Distance_natives_traveled >= Miles_traveled:
            print("The natives have caught up to you. GG")
            done = True
        elif Miles_traveled - Distance_natives_traveled < 16 and Distance_natives_traveled < Miles_traveled:
            print("The natives are catching up")
        if Miles_traveled > 199:
            print("You have escaped the natives. Congratulations!!!")
            done = True

main()