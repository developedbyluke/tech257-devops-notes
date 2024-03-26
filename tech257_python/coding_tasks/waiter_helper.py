# Rationale: To practice lists
# Script should act like a waiter at a restaurant taking orders

customer_order_list = []

# level 1

# Greet the user
print("Welcome to the restaurant.")

# Print a list of starters
starters = [
    {"name": "Garlic Bread", "price": 3.50},
    {"name": "Nachos", "price": 4.00},
    {"name": "Spring Rolls", "price": 2.50},
    {"name": "Chilli Potatoes", "price": 3.00}
]

for index, starter in enumerate(starters, start=1):
    print(f"{index}. {starter["name"]} - £{"%.2f" % starter["price"]}")

# Take an input for the user for their starter
starter = input("What starter would you like? ")
customer_order_list.append(starters[int(starter) - 1])

# Print a list of mains
mains = [
    {"name": "Cheese Pizza", "price": 10.50},
    {"name": "Spaghetti Bolognese", "price": 13.00},
    {"name": "Lasagne", "price": 15.50},
]

for index, main in enumerate(mains, start=1):
    print(f"{index}. {main["name"]} - £{"%.2f" % main["price"]}")

# Take an input for the user for their main course
main = input("What main would you like? ")
customer_order_list.append(mains[int(main) - 1])

# Print a list of desserts
desserts = [
    {"name": "Chocolate Cake", "price": 4.50},
    {"name": "Chocolate Fudge Brownie", "price": 5.00},
    {"name": "Ice Cream", "price": 3.50},
]

for index, dessert in enumerate(desserts, start=1):
    print(f"{index}. {dessert["name"]} - £{"%.2f" % dessert["price"]}")

# Take an input for the user for their dessert
dessert = input("What dessert would you like? ")
customer_order_list.append(desserts[int(dessert) - 1])

# Print all the user's choices
print(f"\nYou ordered:")
for customer_order in customer_order_list:
    print(customer_order["name"])

# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'

# if time: level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.
total_sum = 0

for customer_order in customer_order_list:
    total_sum += customer_order["price"]

print(f"Your bill is: £{"%.2f" % total_sum}")

# if time: level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.
