# Reading from a file and editing it
# Author: Stefanie Steffens

with open(".\\testdata.txt", "rt") as f:
    # data = f.read(5)
    # print(data)
    for line in f: 
        print("we got: ", line.strip())

with open("output.txt", "at") as f: 
    f.write("hello mom \n test")
    print("stuss", file= f)