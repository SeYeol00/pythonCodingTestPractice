import sys
sys.stdin = open("input.txt", "rt")

# 앞에서 풀었던 미로탐색 문제에 저점에서 고점인 조건만 추가한 것이다.
# 풀이법은 똑같다.

# 차이점은 출발점과 시작점이 입력값에 의해 정해진다는 것이다.


dx = [-1,0,1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global cnt

    if x == ex and y == ey:
        cnt+=1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            # 여기 조건이 핵심, 다음에 갈 곳이 전에 있던 곳보다 값이 커야한다.
            if 0 <=xx< n and 0 <=yy< n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] == 1
                DFS(xx,yy)
                # 백트래킹, 다시 돌아갈 때
                ch[xx][yy] == 0



if __name__ == '__main__':
    n = int(input())

    # 값들 저장, 여기서는 기본적으로 초기화하고 아래서 값을 넣을 것이다.
    board = [[0]*n for _ in range(n)]

    # 체크리스트
    ch = [[0]*n for _ in range(n)]

    # 이 문제는 결국 DFS보다 최솟값과 최댓값을 찾는게 중요한 문제다.
    max = -2147000000
    min = 2147000000

    # 값들을 넣으면서 최댓값과 최솟값을 찾을 것이다.
    for i in range(n):
        # 한 줄 입력 받기
        temp = list(map(int,input().split()))
        # min() max() 함수를 최대한 배제하자 시간 복잡도를 생각하면 이게 맞다.
        for j in range(n):
            if temp[j] < min:
                min = temp[j]
                # 출발점 좌표 갱신
                sx = i
                sy = j
            if temp[j] > max:
                max = temp[j]
                # 도착점 좌표 갱신
                ex = i
                ey = j
            # 입력
            board[i][j] = temp[j]    

     # 출발점 방문
    ch[sx][sy] = 1
    cnt = 0
    DFS(sx,sy)
    print(cnt)