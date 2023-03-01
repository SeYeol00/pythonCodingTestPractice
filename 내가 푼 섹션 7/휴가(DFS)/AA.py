import sys
sys.stdin=open("input.txt","r")



# 이 문제에서 레벨은 l + ti가 된다.
# 종료 지점은 n+1일이다. 중요


#       날짜, 합계
def DFS(L, sum):
    global res

    # 종료 지점
    if L == n+1:
        # res 갱신
        if sum > res:
            res = sum

    else: 
        # 상담을 할 때 다음 날짜가 휴가 전 날짜여야한다.
        if (L + T[L]) <= n+1:
            # 상태트리 노드 -> 상담을 하고 다음 날짜를 선택할 때
            # 상담을 하고 난 다음 날짜
            DFS(L + T[L], sum+P[L])
            # 상태트리 노드 -> 상담을 안 할 때
        DFS(L+1,sum)



if __name__ == "__main__":
    n = int(input())
    T = list()
    P = list()
    for i in range(n):
        a,b = map(int,input().split())
        T.append(a)
        P.append(b)
    res = 0
    # 리스트의 0번 인덱스는 값을 0을 넣어야한다. 출발점이다.
    # insert를 안 해준다면 리스트의 0번부터 값이 채워지기 때문에 맞지 않다.
    # 따라서 insert로 0번 인덱스에 값을 채워서 하나씩 자리를 밀어야 한다.
    # 즉 인덱스 번호를 날짜로 사용하는 것이다. 이게 핵심이다
    # 날짜로 값을 접근한다는 개념을 알아두자
    T.insert(0,0)
    P.insert(0,0)
    # 날짜를 넘긴다.
    DFS(1,0)
    print(res)