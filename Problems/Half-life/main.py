initial = int(input())
final = int(input())
cycle = 0
while initial >= final:
    initial //= 2
    cycle += 12
print(cycle)