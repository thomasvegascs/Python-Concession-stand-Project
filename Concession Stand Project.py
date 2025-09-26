# Concession Stand Program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "lemonade": 4.00,
        "chips": 2.50,
        "soda": 2.00,
        "pretzel": 3.25,
        "hot dog": 3.50,
        "popcorn": 3.00}
cart = []
total = 0

print("------------ MENU ------------")
for key, value in menu.items():
    print(f"{key.capitalize():10}: ${value:.2f}")
print("------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER ------")
for food in cart:
    total += menu.get(food)
    print(food.capitalize(), end=" ")

print()
print(f"Total is: {total:.2f}")