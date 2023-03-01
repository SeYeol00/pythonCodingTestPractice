import sys
from collections import deque
sys.stdin = open("input.txt", "rt")


# 큐는 선입선출 , FIFO
# 파이썬에서는 deque를 사용해서 구현한다.
# from collection import deque

# 문제에서 원이 나온다. -> 큐의 앞과 뒤를 연결해서 생각하자.
# 1번 왕자가 popleft()로 나와서 맨 뒤로 간다.(원으로 돈다.)
# 2번 왕자도 마찬가지
# 3번 왕자는 인덱스가 3이라 (카운트가 3이라) popleft() 후 나간다.
# 카운트 초기화 -> 0
# 4번 왕자는 카운트 1이므로 맨뒤로
# 5번도
# 6번 왕자는 카운트가 3이라 아예 탈출


n,k= map(int, input().split())

# 범위를 정해줄 수 있다., 코테에서 중요한 건 시간복잡도이므로 이걸 잘 쓰자.
lst = list(range(1,n+1))
# 1 부터 8까지 값이 삽입된 리스트


queue = deque(lst) # deque화

while queue:
    for _ in range(k-1):
        # k-1번 반복한다. 즉 1번쨰, 2번째 때는 for문을 돌린다.
        cur = queue.popleft()
        queue.append(cur)
    
    # 3번째는 나가라
    queue.popleft()

    # 정답 도출
    if(len(queue))==1:
        print(queue[0])
        queue.popleft()
    
