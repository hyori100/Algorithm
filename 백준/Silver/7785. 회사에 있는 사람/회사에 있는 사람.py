import sys
from collections import Counter

logLen = int(sys.stdin.readline())
dict = {}

for i in range(logLen):
    person, action = sys.stdin.readline().split()
    if action == "enter" and person not in dict:
        dict[person] = 1
    elif action == "leave" and person in dict:
        dict.pop(person)

for key in sorted(dict, reverse=True):
    print(key)