import sys
sys.stdin=open("input.txt","r")


# 그래프 - 노드와 간선의 집합
# 방향이 설정되어 있으면 방향 그래프
# 간선의 값까지 설정되어 있으면 가중치 방향 그래프
# 무방향 그래프, 가중치 방향 그래프 순서로 해볼 것이다.

# 인접 행렬을 통해 그래프를 표현한다.
# 행 -> 열 방향으로 된다고 알아야한다.

# 인접그래프가 g라고 하면
# g[a][b] = 1 이렇게 표현한다.
# 그러면 a -> b 이렇게 간다는 것을 표현할 수 있다.

# 무방향 그래프는 a -> b, b -> a 이렇게 두 곳을 1로 해야한다.
#  g[a][b] = 1 , g[b][a] 하나씩 해가는 거다.




# 무방향 그래프 그리기
# n,m = map(int, input().split())

# # 행렬 표현식 외워두자 n이 주어진다면 n+1을 범위로 잡는다. 
# # 1 부터 n까지 돌 거다.
# g=[[0]*(n+1) for _ in range(n+1)]

# for i in range(m):
#     a,b = map(int, input().split())
#     # 무방향 그래프
#     g[a][b] = 1
#     g[b][a] = 1

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(g[i][j], end=' ')
#     print()



# 문제 해결
n,m = map(int, input().split())

# 행렬 표현식 외워두자 n이 주어진다면 n+1을 범위로 잡는다. 
# 1 부터 n까지 돌 거다.
g=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int, input().split())
    # 단방향 그래프와 가중치 설정
    g[a][b] = c

for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j], end=' ')
    print()