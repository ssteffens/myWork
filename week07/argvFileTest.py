# How to access text file content using the command line
# https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python


import sys
#with open (sys.argv[1], "r") as f:              # opens the file specified in the command line
    #contents = f.read()
    # firstFive = f.read(5)
# print(contents)
# print(firstFive)
    #print(f.read())
    #print(f.readline())
    #print(f.readline())


def readFile():
    with open (sys.argv[1], "rt") as f: 
        return f.read()

contents = readFile()
countE = contents.count("e") + contents.count("E")           # https://www.w3schools.com/python/ref_string_count.asp
                                                            # https://stackoverflow.com/questions/32414205/count-multiple-letters-in-string-python
# print(contents)
print(countE)