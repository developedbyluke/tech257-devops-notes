shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

print(shopping_list)

print("First item:", shopping_list[0])

print("Last item:", shopping_list[-1])

print("Second item:", shopping_list[1])

print("Changing second item from bread to rice...")
shopping_list[1] = "rice"

print("Second item:", shopping_list[1])

print("Length of list:", len(shopping_list))

print("Adding item...")
shopping_list.append("carrots")

print("Length of list:", len(shopping_list))

second_list = ["toffee", "coffee"]
print("Second list:", second_list)

print("Merging lists...")
shopping_list.extend(second_list)

print("Shopping list:", shopping_list)

print("Removing bananas...")
shopping_list.remove("bananas")

print("Shopping list:", shopping_list)

print("Removing last item...")
shopping_list.pop()

print("Shopping list:", shopping_list)