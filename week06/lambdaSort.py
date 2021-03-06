# Sorting a dictionary with and without Lambda Function
# Author: Stefanie Steffens

# 1. Without Lambda Function

data = [{'first': 'Guido',  'last': 'van Rossum',   'YOB': 1956},
        {'first': 'Grace',  'last': 'Hopper',       'YOB': 1906},
        {'first': 'Alan',   'last': 'Turing',       'YOB': 1912}]


def sortFun(item):
    return item['YOB']

newData = sorted(data, key = sortFun)
for item in newData:
    print (item)


# 2. With Lambda Function

data = [{'first': 'Guido',  'last': 'van Rossum',   'YOB': 1956},
        {'first': 'Grace',  'last': 'Hopper',       'YOB': 1906},
        {'first': 'Alan',   'last': 'Turing',       'YOB': 1912}]

newData = sorted(data, key = lambda item: item['first'])
for item in newData:
    print (item)