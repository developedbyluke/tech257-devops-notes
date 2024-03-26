list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

for num in list_data:
    print(num * 2)

print("\n--------------------\n")

for data in embedded_lists:
    print(data)
    for num in data:
        print(num)

print("\n--------------------\n")

for key in dict_data:
    print(key)

print("\n--------------------\n")

for key in dict_data:
    print(dict_data[key])

print("\n--------------------\n")

for value in dict_data.values():
    for i in value.values():
        print(i)

print("\n--------------------\n")

for key in dict_data:
    print(dict_data[key]["money"])

print("\n--------------------\n")

for num in list_data:
    if num < 3:
        print("Less than 3")
    elif num == 3:
        print("I found three")
    elif num > 3:
        print("Greater than 3")
