def solution(array, commands):
    answer = []
    for i in range(0, len(commands)):
        arr = commands[i]
        new_arr = sorted(array[arr[0]-1:arr[1]])
        answer.append(new_arr[arr[2]-1])
    return answer