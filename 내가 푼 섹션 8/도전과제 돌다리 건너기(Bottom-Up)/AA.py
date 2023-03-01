import sys
sys.stdin=open("input.txt","r")


n = int(input())

memo = [0] * (n+1)

memo[1] = 2
memo[2] = 3

for i in range(3,n+1):
    memo[i] = memo[i-1] + memo[i-2]

print(memo[n])
