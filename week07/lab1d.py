# Lab question 1d

with open ("test-d.txt", "w") as f: 
    data = f.write("test d\n") 
    print(data)

with open ("test-d.txt", "a") as f2:
    data = f2.write("another line\n")
    print(data)