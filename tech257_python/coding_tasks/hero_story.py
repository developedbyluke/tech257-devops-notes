# Define a dictionary called story1. It should have the following keys: 'start', 'middle' and 'end'
story1 = {
    "start": input("What is the start of your story? "),
    "middle": input("What is the middle of your story? "),
    "end": input("What is the end of your story? ")
}

# Print the entire dictionary
print(story1)

# Print the type of your dictionary
print(type(story1))

# Print only the keys
print(story1.keys())

# Print only the values
print(story1.values())

# Print the individual values using the keys
print(story1["start"])
print(story1["middle"])
print(story1["end"])

# Now, let's add a new key:value pair: 'hero': yourSuperHero
story1["hero"] = "SuperLuke"
