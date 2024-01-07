def solution(cards1, cards2, goal):
    dic1 = dict([(cards1[i], i) for i in range(len(cards1))])
    dic2 = dict([(cards2[i], i) for i in range(len(cards2))])
    Alist = []
    Blist = []
    for word in goal:
        if word in dic1:
            Alist.append(dic1[word])
        else:
            Blist.append(dic2[word])

    return "Yes" if all(x<y and x+1==y for x, y in zip(Alist[:-1], Alist[1:])) and all(x<y and x+1==y for x, y in zip(Blist[:-1], Blist[1:])) else "No"
