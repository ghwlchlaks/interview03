
from collections import OrderedDict

tables = []
for i in range(2):
    row = int(input())
    table = {}
    for j in range(row):
        datas = list(input().split(' '))
        table[datas[0]] = datas[1:]
    tables.append(table)
    
result = {}
for key, value in tables[0].items():
    if key in tables[1]:
        total = value + tables[1][key]
    else:
        total = value
    result[key] = list(OrderedDict.fromkeys(total))

sort_key = sorted(result)

print('id' + ' ', end='')
for j in range(len(result['id'])):
    print(str(result['id'][j]) + ' ', end='')
print()

for i in range(len(sort_key) -1 ):
    index = sort_key[i]
    print(str(index) + ' ', end="")
    for j in range(len(result[index])):
        lastIndex = j
        print(str(result[index][j]) + ' ', end="")
    for q in range(lastIndex+1, len(result['id'])):
        print('NULL' + ' ', end='')
    print()
    

        
        
        
        
    