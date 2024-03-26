import builtins
import os

# current working directory
print(os.getcwd())


def print_username():
    # reads env variable
    # if USERNAME is None, get USER instead
    # works for Windows and Linux
    username = os.environ.get("USERNAME") or os.environ.get("USER")
    print(f"The current user is: {username}")


def print_total_cpu_cores():
    # prints total CPU cores in the systemdef print_total_cpu_cores():
    cpu_cores = os.cpu_count()
    print(f'Total CPU cores: {cpu_cores}')


for name in dir(builtins):
    if name[0].islower():
        print(name)

print_username()
print_total_cpu_cores()
