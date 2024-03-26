import os

directory = "test_dir"

parent_dir = "C:/Users/luke/Downloads"

path = os.path.join(parent_dir, directory)

os.mkdir(path)
