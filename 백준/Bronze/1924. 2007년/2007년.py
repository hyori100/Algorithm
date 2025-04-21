months = [31,28,31,30,31,30,31,31,30,31,30,31]
weeks = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

a,b = map(int, input().split())
day= 0

for i in range(a-1):
    day += months[i]

day = (day + b) % 7

print(weeks[day])