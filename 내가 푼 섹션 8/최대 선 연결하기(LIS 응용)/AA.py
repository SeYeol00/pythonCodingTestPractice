import sys
sys.stdin=open("input.txt","r")



n = int(input())

arr = list(map(int, input().split()))
memo = [0]*(n+1)
memo[0] = 0
memo[1] = 1

res = 0

for i in range(2,n):
    max = 0
    # i 번쨰의 앞 부터 역으로 서칭
    for j in range(i-1,0,-1):
        if arr[j] < arr[i]:
            if memo [j] > max:
                max = memo[j]
        memo[i] = max + 1
    if memo[i] > res:
        res = memo[i]

print(res)
            