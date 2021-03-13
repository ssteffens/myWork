# Opening/Creating files
# Author: Stefanie Steffens

# Opens an existing file for reading
# with open(".\\lecture1.txt", "r") as f:
#    print("create a file")


# Opens an existing file for reading and writing
# with open(".\\lecture1.txt", "r+") as f:
#    print("create a file")


# Opens an existing file or if file does not exist, creates a new one
with open(".\\lecture1.txt", "w") as f:
    print("create a file")


# Opens/creates a file for appending (if file exists, content will be added to it}
# with open(".\\lecture1.txt", "a") as f:
#    print("create a file")


# Creates a file for writing (if file exists, will display an error)
#with open(".\\lecture1.txt", "x") as f:
#    print("create a file")