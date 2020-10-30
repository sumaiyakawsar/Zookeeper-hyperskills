deposit = int(input())
year = 0
while deposit < 700000:
    interest_rate = 1.071
    year += 1
    deposit = deposit * interest_rate
print(year)
