import sys
sys.stdin=open("input.txt","r")



# 중복 불가면 체크리스트를 사용하자. 핵심!
# 순열 -> 체크리스트를 사용하는  DFS 문제

def DFS(l):
    global cnt
    # 호출이 들어오면 맨 처음 보는 곳
    if l == m:
        for i in lst: # 두 수
            print(i,end=" ")
            
        print()
        cnt+=1
    else:
        for i in range(1,n+1):
            if check[i] == 0:

                # 호출 전
                # 작업을 하고 호출이 일어난 것
                check[i] = 1
                lst[l] = i

                # 호출, 스택이 쌓이는 것을 생각하자
                DFS(l+1) # 체크가 안 되어 있으면 아래로 내려가라

                # 호출 아래에 있는 것은 위쪽과 대칭이어야한다.
                # 호출이 끝나고 되돌아온 것
                # 스택으로 생각하자
                # 호출의 밑 지접은 호출이 끝나고 백하고 돌아온 곳
                # 트리의 아래 노드에서 다시 온 거다
                check[i]=0




if __name__ == "__main__":
    n,m = map(int,input().split())
    lst = [0]*m
    check = [0]*(n+1)
    cnt=0
    DFS(0)
    print(cnt)