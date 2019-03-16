
n = int(input())
height = []
for i in range(n):
    height.append(int(input()))

max_len = 0
for i in range(len(height)-1):
    for j in range(i+1, len(height)):
        if height[i] <= height[j]:
            max_len = max( max_len, abs(i- j) )
            break
        
        
print(max_len)