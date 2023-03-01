import sys
sys.stdin = open("input.txt", "rt")

board = []

for _ in range(7):
    lst = list(map(int, input().split()))
    board.append(lst)

# for x in board:
#     print(x)

cnt = 0

# 이차원 격자판에서 0 1 2만 돌린다.
# i가 3부터 시작이면 5자리가 안된다. 3, 4, 5, 6
# 그래서 i를 2까지만 돌리는 것이다.
# 결국 세로는 i를 핼 좌표에 넣으면 되기에 이렇게 돌리는 것이다.
for i in range(3):
    for j in range(7):
        # 다섯 개를 분리하는 작업
        # 리스트 인덱싱
        # 이래서 i를 0, 1, 2만 둔 것이다.
        temp = board[j][i:i+5]

        # 가로 검증문
        # 팰린드롬 확인, 이거 가로만 된다. 세로로는 슬라이싱이 불가 
        if temp == temp[::-1]:
            cnt+=1
        
        # 세로 검증문
        # 세로는 따로 for문을 돌려야한다.
        # 즉 temp를 못 쓴다.
        # 즉 우리가 따로 검사를 해야한다.
        # 회문의 길이를 2로 나눈 몫만큼만 돌면 된다.
        for k in range(5//2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt+=1


print(cnt) 