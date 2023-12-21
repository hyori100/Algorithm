def solution(absolutes, signs):
    answer = []
    for absolute,sign in zip(absolutes, signs):
        if sign == False:
            answer.append(absolute * -1)
        else:
            answer.append(absolute)
    return sum(answer)