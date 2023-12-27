def solution(n):
    waterMelonStr = "수박"
    a,b = divmod(n,2)
    return waterMelonStr*a if b==0 else waterMelonStr*a + "수"