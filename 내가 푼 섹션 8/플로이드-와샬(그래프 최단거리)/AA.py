import sys
sys.stdin=open("input.txt","r")



# 플로이드 와샬도 냅색 알고리즘과 동일한 원리이다.
# 냅색과 같이 기존 값이랑 경우를 더해서 비교한다.
# 인접행렬을 초기화한다. 
# 맨 처음에 들어오는 값들은 노드에서 다른 노드로 직행하는 값
# 이후에 0,0을 제외하고 다 큰 값을 넣어 최솟값 도출을 위해 정리한다.

# i노드에서 j노드로 갈 때 k노드를 거쳐서 가는 비용식 
# => board[i][k] + board[k][j]

# 현재 노드에서 타겟 노드로 직행하는 것 vs i노드에서 j노드로 갈 때 k노드를 거쳐서 가기
# 이 두 가지 케이스를 비교해서 더 작은 값을 갱신한다.
# board[i][j] = min(board[i][j], board[i][k] + board[k][j])

# 다이나믹 테이블(메모)에서 순서는 순열이 적용이 된다.
# 즉 순서가 상관이 없다는 뜻이다. 어차피 최소 경로, 즉 제일 좋은 순서대로 메모가 채워진다.

# 어차피 n,n은 자기 자신으로 가는 값으로 기본적으로 0이다.
# 그래서 동적으로 프로그래밍이 될 때 예를 들어 5 -3 - 3이라고 해도
# 결국 5 - 3만 적용이 된다.


if __name__ == "__main__":
    
    n, m = map(int,input().split())
    
    board = [[2147000000]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        board[i][i] = 0


    # for x in range(n+1):
    #     print(board[x])

    # print()
    
    for _ in range(m):
        x,y,v = map(int,input().split())
        board[x][y] = v
    
    # 중간에 거치는 노드 k가 필요하기 때문에 결국 3중 for문을 돌아야 한다.
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if board[i][j] > board[i][k] + board[k][j]:
                    board[i][j] = board[i][k] + board[k][j]


    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i][j] == 2147000000:
                print("M", end=" ")
            else:
                print(board[i][j], end=" ")
        print()