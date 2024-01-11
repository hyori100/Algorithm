import numpy as np

def solution(answers):
    answer = []
    
    answerLen = len(answers)
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    
    person1 = person1 * (answerLen//len(person1)) + person1[:(answerLen%len(person1))]
    person2 = person2 * (answerLen//len(person2)) + person2[:(answerLen%len(person2))]
    person3 = person3 * (answerLen//len(person3)) + person3[:(answerLen%len(person3))]
    
    sum1 = sum([1 for i in np.equal(person1,answers) if i == True])
    sum2 = sum([1 for i in np.equal(person2,answers) if i == True])
    sum3 = sum([1 for i in np.equal(person3,answers) if i == True])
    
    if sum1 > 0:
        answer.append((1, sum1))
    if sum2 > 0 :
        answer.append((2, sum2))
    if sum3 > 0:
        answer.append((3, sum3))
    
    maxSum = max([b for a,b in answer])
    answer = [(a,b) for a,b in answer if maxSum == b]
    return [a for a,b in sorted(answer, key = lambda x: (-x[1], x[0]))]
    