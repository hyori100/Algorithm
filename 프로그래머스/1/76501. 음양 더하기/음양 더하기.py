def solution(absolutes, signs):
    answer = []
    for index, value in enumerate(signs):
        if value == False:
            answer.append(absolutes[index] * -1)
        else:
            answer.append(absolutes[index])
    return sum(answer)