def solution(s):
    answer = []
    strings = s.split(" ")
    for string in strings:
        new_string = []
        for index, value in enumerate(string):
            if index % 2 == 0:
                new_value = value.upper()
            else:
                new_value = value.lower()
            new_string.append(new_value)
        answer.append(''.join(new_string))
    return ' '.join(answer)