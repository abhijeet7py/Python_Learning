import os

# Specify the directory path (you can change this as needed)
directory_path = '/AMD'

# Use os.listdir() to get the contents
try:
    contents = os.listdir(directory_path)
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory {directory_path} was not found.")
except PermissionError:
    print(f"Permission denied to access {directory_path}.")
