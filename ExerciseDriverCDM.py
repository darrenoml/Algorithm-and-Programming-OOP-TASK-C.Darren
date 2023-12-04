import ProgramExerciseCDM
def ItemList():
    Items = []
    NumItems = int(input("Enter the number of items you wish to add"))
    while True:
        try:
            if NumItems < 1:
                print("Please enter a number bigger than 1")
                break
        except ValueError:
            print("Invalid Number")

    for i in range(NumItems):
        print(f"Item (i+1)")
        while True:
            food = input("Enter food:")
            amount = float(input("Enter amount:"))
            if amount <= 0:
                print("amount must be greater than 0")
                break
        Items.append(ProgramExerciseCDM(food, amount))
    return Items

def display(Items):
    for item in list:
        print(f"Item:")
        
