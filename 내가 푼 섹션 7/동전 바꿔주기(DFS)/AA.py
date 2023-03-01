import sys
sys.stdin=open("input.txt","r")

# 처음에 만들어야하는 금액 -> sum
# 종류를 받고 이걸 레벨로 인덱싱  n이 들어오면 L==n 정지 조건

# 상태 트리 가짓수 => 주어진 동전의 갯수 +1
# 왜 +1?? => 하나도 안 넣을 때를 생각하자

# 예를 들어 5원 짜리 세개가 들어왔다.
# => 0개를 넣을까, 1개를 넣을까, 2개를 넣을까, 3개를 넣을까

# 10원짜리 2개가 들어왔다.
# 0개를 넣을까, 1개를 넣을까, 2개를 넣을까

# 주어진 목표 금액보다 높다? => if 조건으로 자르기


def DFS(L,sum):
    global cnt

    if sum > T:
        return

    if L == k:
        if sum == T:
            cnt+=1

    else:
        for i in range(cn[L]+1):
            DFS(L+1,sum+cv[L]*i)


if __name__ == '__main__':
    T = int(input())
    k = int(input())
    
    cv = list()
    cn = list()


    for _ in range(k):
        a,b = map(int,input().split())
        cv.append(a)
        cn.append(b)
        
    cnt = 0
    DFS(0,0)
    print(cnt)