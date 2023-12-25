def solution(price, money, count):
    sumPrice = sum([price*i for i in range(1, count+1)])
    return sumPrice-money if sumPrice > money else 0