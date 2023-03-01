import sys
sys.stdin=open("input.txt","r")
#파이썬으로 재귀를 돌릴 때 제한 코드를 넣어줘야한다.
# 이렇게 해줘야 멈춘다. 재귀로 타이트하게 돌 때 넣어준다.
# 런타임에러가 나면 이걸 넣어줘야한다.
sys.setrecursionlimit(10**6) # 이걸 넘어가면 자동으로 재귀 종료시킨다.


# 격자판의 특정 영역의 넓이와 갯수를 찾는 문제는 BFS나 DFS나 큰 차이가 없다.
# 물에 잠기고 나면 잠기지 않는 안전영역을 찾아야한다.
# DFS -> 4방향 탐색을 생각하자 
# BFS -> 8방향 탐색

# 물에 잠기는 높이보다 커야 서칭이 가능하다.
# 서칭이 끝나면 안전영역 하나 카운팅
# 방문하면 1로 체크하기
# 체크가 0이면서 안전영역인 지역 -> 서치 시작, 갯수 추가
# 이 문제는 기출문제
# 1부터 100까지라고 하지만 0부터 해야 통과가 된다.



dx = [-1,0,1,0]
dy = [0,1,0,-1]


def DFS(x,y,h): # x,y는 행과 열, h는 높이
    # 방문
    ch[x][y] = 1

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        
        if 0<=xx<n and 0<=yy<n and ch[xx][yy] == 0 and board[xx][yy] > h:
            DFS(xx,yy,h)

    
if __name__=="__main__":
    n = int(input())
    cnt = 0 # 그 떄 높이를 정해놓고 안전 영역이 몇개인가
    res = 0 # 최대 갯수를 잴 것이다.
    board =[list(map(int, input().split()))for _ in range(n)]
    # 높이 부터 정하자 0부터 99
    for h in range(100):
        # 여기서 체크리스트를 만든다. 높이가 초기화 될 때마다 방문도 초기화해야되기 때문
        ch = [[0]*n for _ in range(n)]
        # 여기서 cnt를 한 번 초기화해야한다.
        # 높이마다 cnt를 초기화해야 전 높이의 카운팅이 안 넘어 온다.
        cnt = 0
        for i in range(n):
            for j in range(n):
                if ch[i][j] == 0 and board[i][j] > h:
                    # 잠기지 않은 영역 찾았다.
                    cnt += 1
                    ch[i][j] = 1
                    DFS(i,j,h)
        if cnt > res:
            res = cnt
        # 최적화 중요, 만약 최대높이가 9인데 10 이상의 h는 굳이 for문을 안 돌려도 된다.
        # 꼭 100까지 다 할 거 아니지 않는가
        # 파이썬은 최적화가 중요하다.
        if cnt == 0:
            break

    print(res)
                    

