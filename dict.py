import random

count = 0
List = []

while count < 50:
    num = random.randint(1, 100)
    if num in List:
        continue
    else:
        List.append(num)
    count += 1
print('ListMain = ', List)

dictionary = {'List1': [], 'List2': [], 'sum1': int, 'sum2': int}

for num in List:
    if num % 2 == 0:
        dictionary['List1'].append(num)
    else:
        dictionary['List2'].append(num)

print('List 1 = ', dictionary['List1'])
print('List 2 = ', dictionary['List2'])

print('SumList1 = ', sum(dictionary['List1']))
print('SumList2 = ', sum(dictionary['List2']))
