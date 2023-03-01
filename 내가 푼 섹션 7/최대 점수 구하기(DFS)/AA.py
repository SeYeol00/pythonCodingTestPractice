import sys
sys.stdin=open("input.txt","r")


# 내가 풀기로 한 문제들을 부분집합으로 받는다.
# {1,2,3,4,5}의 문제 중
# 점수와 시간을 비교해서 부분집합을 만들어 푼다.
# {1,2,3}을 시간 내에 풀 수 있다.
# 상태트리 -> 1번을 푼다, 풀지 않는다.
#           2번을 푼다, 풀지 않는다.
#           3번을 푼다 풀지 않는다.

def DFS(level,sum,time):
    global res

    # 시간은 m을 넘어서면 안 된다.
    if time > m:
        # 가지치기
        return

    # 상태 트리의 마지막 레벨에 접근했을 때
    if level == n:
        # 점수의 최댓값 찾기
        if sum > res:
            res = sum
        
    else:
        # 상태 트리 중에 문제를 푸는 노드 접근
        # 레벨 하나 추가, 합에 추가, 시간 추가
        DFS(level+1, sum + pv[level], time + pt[level])

        # 상태 트리 중에 문제를 안 푸는 노드 접근
        DFS(level+1, sum , time)
    

if __name__ == "__main__":
    n,m = map(int, input().split(" "))
    
    pv = list() # problem value
    pt = list() # problem time
    for i in range(n):
        a,b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = 0
    DFS(0,0,0) # 레벨, 총점, 시간
    print(res)