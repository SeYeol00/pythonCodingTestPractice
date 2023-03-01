import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

lst = []

for i in range(n+2):
    if i == 0 or i == n+1:
        a = []
        for l in range(n+2):
            a.append(0)
        lst.append(a)
    else:
        a = list(map(int,input().split()))
        a.insert(0,0)
        a.append(0)
        lst.append(a)

for x in lst:
    print(x)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

num = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        print(j)
        # 내가 만든 건데 놓치기가 쉬우니 정신 차려라
        if lst[i][j] > lst[i-1][j] and lst[i][j] > lst[i+1][j] and lst[i][j] > lst[i][j-1] and lst[i][j]>lst[i][j+1]:
            print(lst[i][j],i,j)
            num+=1
        # 상하좌우 공식
        # if all(lst[i][j]>lst[i+dx[k]][j+dy[k]] for k in range(4)):
        #     print(lst[i][j],i,j)
        #     num+=1
print()
print(num)