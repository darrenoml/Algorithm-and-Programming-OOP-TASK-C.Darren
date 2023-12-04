from ProgramExerciseCDM import Inventory

def create_objects_list():
    items_list = []
    num_items = int(input("How many items will you order today? "))
    while num_items < 1:
        print("Number of items must be at least 1.")
        num_items = int(input("How many items will you order today? "))
    
    for i in range(num_items):
        food = input(f"Item #{i + 1}-\nEnter food: ")
        amount = float(input("Enter amount of pounds: "))
        while amount <= 0:
            print("Amount of pounds must be greater than 0.")
            amount = float(input("Enter amount of pounds: "))
        
        item = Inventory(food, amount)
        items_list.append(item)
    
    return items_list

def display_items_list(items_list):
    for item in items_list:
        print("\nItem:", item.get_food())
        print("Amount ordered:", f"{item.get_amount()}", "pounds")
        print("Price per pound: $", f"{item.PriceList()}")
        print("Price of order: $", f"{item.calculate()}")

def calculate_total_cost(items_list):
    total_cost = 0
    for item in items_list:
        total_cost += item.get_calculated_price()
    return total_cost

def main():
    items_list = create_objects_list()
    display_items_list(items_list)
    total_cost = calculate_total_cost(items_list)
    print("Total Cost: $", (total_cost))

main()
