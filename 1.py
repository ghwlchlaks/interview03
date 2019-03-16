
n = int(input())

answer = n
for i in range(1, n+1):
    value = abs(i - (n/i))
    if (n%i == 0 and value < answer):
        answer = int(value)
        
print(answer)