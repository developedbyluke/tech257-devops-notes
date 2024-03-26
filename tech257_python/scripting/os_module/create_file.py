import os

directory = "test_dir"

parent_dir = "C:/Users/luke/Downloads"

path = os.path.join(parent_dir, directory)

filename = "testfile.txt"
filepath = os.path.join(path, filename)

# Make file
with open(filepath, "w") as file1:
    content = "Contents of the file are here"
    file1.write(content)

print(f"File {filename} created in {path}")
