import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

a = list(map(int,input().split()))

m = int(input())

b = list(map(int,input().split()))

ans =[]

countA = 0
countB = 0
# and 조건임 시발
while(n > countA and m > countB):
        if a[countA] >= b[countB]:
            ans.append(b[countB])
            countB += 1
        elif a[countA] < b[countB]:
            ans.append(a[countA])
            countA += 1
        else:
            break

if n == countA:
    ans = ans+b[countB:]
elif m == countB:
    ans = ans+a[countA:]

for i in ans:
    print(i,end=" ")
