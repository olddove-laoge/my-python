n = input()
datas = map(int, input().split())
numbers = [0]*1000
efficient_number = 0
efficient_numbers = set()
for i in datas:
    numbers[i-1] += 1
for i in range(1000):
    if numbers[i]!= 0:
        efficient_number += 1
        efficient_numbers.add(i+1)
        
print(efficient_number)
efficient_numbers = sorted(efficient_numbers)
print(' '.join(map(str, efficient_numbers)))
