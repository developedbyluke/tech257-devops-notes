# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")
# save the items as a tuple
# print the tuple
essentials_tuple = (essential_item1, essential_item2, essential_item3)  # YOUR CODE GOES HERE INSTEAD OF 'None'
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")
# try to add the 4th item to the tuple
# if you can't add the 4th item, work out how to save the 4th item to the tuple
converted_to_list = list(essentials_tuple)
converted_to_list.append(essential_item4)
essentials_tuple = tuple(converted_to_list)

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)
