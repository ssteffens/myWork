# This program puts 10 random numbers into queue. The program then outputs all values, then print the numbers
# from the queue one at a time as well as the current numbers still in the queue. 
# Author: Stefanie Steffens

import random
queue = []
numberofNumbers = 10
rangeTo = 100

for n in range(0,numberofNumbers):
    queue.append(random.randint(0,rangeTo))
print("queue is {}".format(queue))

while len(queue) !=0:
    currentNumber = queue.pop(0)
    print ("current Number is {} and the queue is {} ".format(currentNumber, queue))

print ("the queue is now empty")