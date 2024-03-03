# Write a Python program to list only directories, files and all directories, files in a specified path.

import os

def list_directories_and_files(path):
    directories = []
    files = []
    all_items = []

    # Iterate over all items in the specified path
    for item in os.listdir(path):
        # Join the path with the item name to get the full path
        full_path = os.path.join(path, item)
        # Check if the item is a directory
        if os.path.isdir(full_path):
            directories.append(item)
        else:
            files.append(item)
        all_items.append(item)

    return directories, files, all_items

path = "/Users/aminayegenberdiyeva/Desktop"

directories_only, _, _ = list_directories_and_files(path)
print("Directories:")
for directory in directories_only:
    print(directory)

_, files_only, _ = list_directories_and_files(path)
print("\nFiles:")
for file in files_only:
    print(file)

all_directories_and_files = list_directories_and_files(path)[2]
print("\nAll Directories and Files:")
for item in all_directories_and_files:
    print(item)

#done