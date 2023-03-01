import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

lst = []

for _ in range(n):
    lst.append(list(map(int,input().split())))

# # 매트릭스 출력
# for x in lst:
#     print(x)

m = int(input())

for _ in range(m):

    h , t , k = map(int, input().split())
    
    #방향 정해주기
    if t==0: # 왼쪽으로 돌리기
        #회전 시키기
        for _ in range(k):
            # 파이썬 리스트는 pop(index)을 하면 자동으로 당겨진다. 좀 사기인듯
            # 행에다 넣어야한다.
            front = lst[h-1].pop(0)
            lst[h-1].append(front)
    else: # 오른쪽으로 돌리기
        for _ in range(k):
            # 파이썬 리스트는 pop(index)을 하면 자동으로 당겨진다. 좀 사기인듯
            last = lst[h-1].pop() # 값을 안 넣으면 마지막 값을 팝 함
            # 행에다 넣어야한다.
            lst[h-1].insert(0,last)

# for x in lst:
#     print(x)

ans = 0
s = 0
e = n-1

for i in range(n):
    # 핵심 로직, 위에서 아래로 간다고 생각해야한다.
    for j in range(s,e+1):
        ans+=lst[i][j]
    # 이런 건 행으로 따져라
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(ans)
    