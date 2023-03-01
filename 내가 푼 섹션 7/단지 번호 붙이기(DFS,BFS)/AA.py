import sys
sys.stdin=open("input.txt","r")

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 단지, 집의 갯수 세기
# 이건 DFS나 BFS로 풀 수 있다.
# DFS를 통해 풀 떄는 백트래킹을 써서 구할 수 있다.
# 백트래킹으로 계속 뒤로 간 뒤에 
# res라는 리스트를 생성하여 각 단지의 집 갯수를 append한다.
# 총 단지의 갯수는 len(res)를 하면 나온다.

def DFS(x,y):
    global cnt
    
    cnt+=1
    # 방문 했으니 0으로 만든다.
    board[x][y] = 0 

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx,yy)

        


if __name__ == "__main__":
    n = int(input())
    #                       입력 값에 띄어쓰기가 없으면 split()을 쓰지 않는다.
    board = [list(map(int, input())) for _ in range(n)]
    res = []
    # board 탐색, 이중 for문을 돌아야한다.
    for i in range(n):
        for j in range(n):
            # 1을 발견했을 때 이 때부터 퍼져나가야한다.
            # 단지를 발견했다는 뜻이다.
            # 집을 발견했다는 얘기
            if board[i][j] == 1:
                # 단지를 찾을 때마다 cnt를 초기화해야 한다.
                cnt = 0
                DFS(i,j)
                # 단지의 집 갯수가 카운트가 다 되었을 때
                # cnt를 res에 넣어준다.
                res.append(cnt)
    print(len(res))
    # 오름차순 정렬
    res.sort()
    for x in res:
        print(x)



    