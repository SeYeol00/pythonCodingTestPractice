import sys
from collections import deque
sys.stdin=open("input.txt","r")


# 애너지 최소량 구하기, 

# 디피는 다이나믹 테이블을 그리면서 해결한다.
# 여기서는 memo



dx = [-1,0,1,0]
dy = [0,1,0,-1]


# 바텀 업 또는 탑 다운 둘 다 구현 해보자

# 탑 다운 방식
#                      DFS(2,2)
#                    /         \
#             DFS(2,1)         DFS(1,2)
#            /       \         /       \
#      DFS(1,1)   DFS(2,0)  DFS(1,1)   DFS(0,2)

# 탑 다운 방식은 일반적인 재귀를 생각하고 그 다음에 메모이제이션을 생각하여 
# 메모가 존재하면 그대로 리턴해주는 정지 조건을 추가해주면 된다.
# 탑 다운 방식을 쓰기 이전에는 먼저 노트에 DFS()의 진행 트리를 적어보고
# 그 다음에 겹치는 DFS()가 존재하면 그걸 제거해주는 메모를 적어서
# 정지 조건에 추가해주자.


def DFS(i,j):
    # 출발 지점
    if i==0 and j==0:
        return board[0][0]

    # 메모를 통한 최적화
    if memo[i][j] != 0:
        return memo[i][j]
    
    else:
        # 행이나 열이 0이면 한 가지 쪽으로만 호출해야한다.
        # 재귀를 돌릴 때 자기 자신을 밟아야한다.
        if i == 0:
            memo[i][j] = DFS(i,j-1) + board[i][j]
            return DFS(i,j-1) + board[i][j]
        
        if j == 0:
            memo[i][j] = DFS(i-1,j) + board[i][j]
            return DFS(i-1,j) + board[i][j]

        # DFS를 리턴해주어야한다. + 현재 밟은 자리를 더해주어야한다.
        memo[i][j] = min(DFS(i-1,j),DFS(i,j-1)) + board[i][j]
        return min(DFS(i-1,j),DFS(i,j-1)) + board[i][j]


if __name__ == "__main__": 

    # 탑 다운
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]

    memo = [[0]*n for _ in range(n)]

    # 탑 다운 끝에서 부터 뒤로 가는 것이다.
    print(DFS(n-1,n-1))






























    # # 바텀업
    # n = int(input())

    # board = [list(map(int, input().split())) for _ in range(n)]

    # memo = [[0]*n for _ in range(n)]

    # memo[0][0] = board[0][0]
    
    # # 먼저 맨 위와 맨 왼쪽의 값들을 정해주어야한다.
    # # 이 것들은 전에 있던 메모에서 그대로 가져와서 쭉 가면 된다.
    
    # # 핵심 위에서 아래로, 왼쪽에서 오른쪽으로 가는 최소 거리들을 먼저 더해주자.

    # # 0행들의 최소 거리
    # for i in range(1,n):
    #     memo[i][0] = memo[i-1][0]+board[i][0]
    
    # # 0열들의 최소 거리
    # for j in range(1,n):
    #     memo[0][j] = memo[0][j-1]+board[0][j]

    # # 이제 사이를 비교할 차례, 
    # # 왼쪽 좌표와 위쪽 좌표의 보드 값들을 비교하여 작은 값을 찾는다.
    # for i in range(1,n):
    #     for j in range(1,n):
    #         if memo[i-1][j] > memo[i][j-1]:
    #             memo[i][j] = memo[i][j-1] + board[i][j]   
    #         elif memo[i][j-1] > memo[i-1][j]:
    #             memo[i][j] = memo[i-1][j] + board[i][j]   
    #         else:
    #             memo[i][j] = memo[i-1][j]+board[i][j]

    # for x in range(n):
    #     print(board[x])

    # print()

    # for x in range(n):
    #     print(memo[x])

    # print()
    # print(memo[n-1][n-1])
            
