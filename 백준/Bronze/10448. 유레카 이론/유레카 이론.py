T = [n*(n+1)//2 for n in range(46)]

def isPossible(num):
    for i in range(1, 46):
        for j in range(i, 46):
            for z in range(j, 46):
                if T[i] + T[j] + T[z] == num:
                    return 1
    return 0

for i in range(int(input())):
    print(isPossible(int(input())))