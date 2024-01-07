def solution(cards1, cards2, goal):
    dic = {}
    for index, card in enumerate(cards1):
        dic[card] = ('A', index)
    for index, card in enumerate(cards2):
        dic[card] = ('B', index)
    for index, word in enumerate(goal):
        goal[index] = dic[word]
        
    Alist = [y for x,y in goal if x == "A"]
    Blist = [y for x,y in goal if x == "B"]

    return "Yes" if all(x<y and x+1==y for x, y in zip(Alist[:-1], Alist[1:])) and all(x<y and x+1==y for x, y in zip(Blist[:-1], Blist[1:])) else "No"