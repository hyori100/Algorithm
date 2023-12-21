def solution(absolutes, signs):
    answer = []
    for absolute,sign in zip(absolutes, signs): #zip - 다중 리스트를 순서대로 요소를 뽑아줌
        if sign == False:
            answer.append(absolute * -1)
        else:
            answer.append(absolute)
    return sum(answer)