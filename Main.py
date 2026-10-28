"""Boba4Me - A simple Python drink ordering project."""

print("Welcome to Boba4Me!")
name = input("What is your name? ").strip()
if not name:
    name = "Customer"

print(f"\nHi, {name}! Let's make your drink.")

print("\nChoose your drink:")
print("1. Tea")
print("2. Milk Tea")
print("3. Fresh Milk")

drink_choice = input("Enter 1, 2, or 3: ").strip()
while drink_choice not in ("1", "2", "3"):
    drink_choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

toppings = []

if drink_choice == "1" or drink_choice == "2":
    print("\nChoose your tea flavor:")
    print("1. Black Tea")
    print("2. Green Tea")
    print("3. Jasmine Tea")
    print("4. Oolong Tea")

    flavor_choice = input("Enter 1, 2, 3, or 4: ").strip()
    while flavor_choice not in ("1", "2", "3", "4"):
        flavor_choice = input("Invalid choice. Enter 1, 2, 3, or 4: ").strip()

    tea_flavors = ["Black", "Green", "Jasmine", "Oolong"]
    flavor = tea_flavors[int(flavor_choice) - 1]

    if drink_choice == "1":
        drink_name = flavor + " Tea"
    else:
        drink_name = flavor + " Milk Tea"
else:
    print("\nChoose your milk flavor:")
    print("1. Strawberry")
    print("2. Mango")
    print("3. Taro")
    print("4. Matcha")
    print("5. Chocolate")
    print("6. Brown Sugar")

    flavor_choice = input("Enter 1, 2, 3, 4, 5, or 6: ").strip()
    while flavor_choice not in ("1", "2", "3", "4", "5", "6"):
        flavor_choice = input("Invalid choice. Enter 1, 2, 3, 4, 5, or 6: ").strip()

    milk_flavors = ["Strawberry", "Mango", "Taro", "Matcha", "Chocolate", "Brown Sugar"]
    flavor = milk_flavors[int(flavor_choice) - 1]

    if flavor == "Brown Sugar":
        drink_name = "Brown Sugar Boba Pearls Milk"
        toppings.append("Boba Pearls")
        print("\nBoba pearls are already included in this drink!")
    else:
        drink_name = flavor + " Milk"

# Ask about boba only if the drink does not already include it.
if "Boba Pearls" not in toppings:
    pearls = input("\nWould you like boba pearls? (yes/no/y/n): ").strip().lower()
    while pearls not in ("yes", "y", "no", "n"):
        pearls = input("Please enter yes, y, no, or n: ").strip().lower()
    if pearls in ("yes", "y"):
        toppings.append("Boba Pearls")

other = input("Would you like another topping? (yes/no/y/n): ").strip().lower()
while other not in ("yes", "y", "no", "n"):
    other = input("Please enter yes, y, no, or n: ").strip().lower()

if other in ("yes", "y"):
    print("\nChoose an extra topping:")
    print("1. Grass Jelly")
    print("2. Pudding")
    print("3. Aloe Vera")

    topping_choice = input("Enter 1, 2, or 3: ").strip()
    while topping_choice not in ("1", "2", "3"):
        topping_choice = input("Invalid choice. Enter 1, 2, or 3: ").strip()

    extra_toppings = ["Grass Jelly", "Pudding", "Aloe Vera"]
    toppings.append(extra_toppings[int(topping_choice) - 1])

print("\n========== Boba4Me Order ==========")
print(f"Name: {name}")
print(f"Drink: {drink_name}")
if toppings:
    print("Toppings: " + ", ".join(toppings))
else:
    print("Toppings: None")
print("Thank you for ordering from Boba4Me!")
print("===================================")
