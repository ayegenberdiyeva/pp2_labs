# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os
import sys

if len(sys.argv) < 2:
    print("Write arguments!")
    sys.exit()
if not os.path.exists(sys.argv[1]):
    print("Path doesn't exist")
    sys.exit()

print(f"Is dir readable: {os.access(sys.argv[1], os.R_OK)}")
print(f"Is dir writeable: {os.access(sys.argv[1], os.W_OK)}")
print(f"Is dir executable: {os.access(sys.argv[1], os.X_OK)}")