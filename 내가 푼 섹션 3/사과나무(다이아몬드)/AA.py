import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

a =[]

for _ in range(n):
    lst = list(map(int, input().split()))
    a.append(lst)


# 투 포인터 전략
res = 0
s=e=n//2

for i in range(n):
    # 핵심 로직, 위에서 아래로 간다고 생각해야한다.
    for j in range(s,e+1):
        res+= a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
        
print(res)
