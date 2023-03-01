import sys
sys.stdin = open("input.txt", "rt")


sudoku = []

for _ in range(9):
    lst = list(map(int,input().split()))
    sudoku.append(lst)

for x in sudoku:
    print(x)

# 스도쿠의 조건 -> 같은 행 끼리 중복 x, 같은 열 끼리 중복 x, 같은 그룹 안에 중복 x
# 체크리스트가 3개 필요하다.
# 행 체크 리스트, 열 체크 리스트, 그룹 체크 리스트

# sudoku[i][j] 값을 인덱스로 준다.
# ch[sudoku[i][j]] 이게 2 이상이면 중복이라 탈락이 되는 느낌
# sum(ch)가 9라면 통과 아니면 탈락

def check(a):
    for i in range(9):
        # 매 i마다 리스트 초기화
        # 아래로 서술하는게 시간이 덜 걸린다.
        h_ch=[0]*10 # n+1을 곱해준다.
        y_ch=[0]*10 # n+1을 곱해준다.
        for j in range(9):
            h_ch[a[i][j]] = 1 #f행과 열은 인덱스 번호를 바꾸면 된다. 기억하기
            y_ch[a[j][i]] = 1 # 여기서 열의 합도 나온다.
        if sum(h_ch) != 9 or sum(y_ch) != 9:
            return False

    # 행과 열의 체크가 끝났으니 완전히 새로 하자
    # 먼저 9*9를 3*3으로 쪼개자
    # 즉 첫번째 그룹, 두 번째 그룹, 세번째 그룹 ~ 아홉번째 그룹
    for i in range(3):
        for j in range(3):
            # 그룹마다 체크리스트 초기화
            # 이게 방문 리스트랑 같은 느낌이라 자주 쓰임
            g_ch=[0]*10 # 이게 시간이 덜 걸린다.

            # 쪼갠걸 이제 좌표를 찍자
            for k in range(3):
                for s in range(3):
                    # 해석하자면 1번째 3*3그룹, 2번쨰 3*3그룹 이런 느낌
                    # 그 다음에 k와 s를 더해야 안에 있는 좌표를 가리킴
                    # 즉 몇 번째 그룹의 (k,s)의 좌표
                    g_ch[a[i*3+k][j*3+s]] = 1
            if sum(g_ch) != 9:
                return False
    return True

if check(sudoku):
    print("YES")
else:
    print("NO")


            