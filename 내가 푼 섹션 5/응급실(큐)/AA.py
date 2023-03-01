import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

n,m = map(int,input().split())


# 튜플 자료구조로 n번째 표현하기 pos는 번째, Val은 실제 값
lst = [(pos,val)for pos,val in enumerate(list(map(int,input().split())))]

queue = deque(lst)

print(queue)

cnt = 0

# 무한반복 돌리고 m번째가 진료 받을때 브레이크 걸기
while True:
    cur = queue.popleft()

    # 큐에서 다른 원소들과 비교하는 문법, 핵심
    # 모든 for문의 원소들 중에 하나라도 만족 안 하면 else:로 간다.
    # any를 기억할 것
    if any(cur[1]<x[1] for x in queue):
        queue.append(cur)
    else:
        cnt+=1
        if cur[0] == m:
            break
print(cnt)
    