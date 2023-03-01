import sys
import heapq as hq # 파이썬에서는 힙큐라는 것이 존재한다.
# 힙을 구현할 때 제일 좋은 방법
sys.stdin=open("input.txt","r")

a = [] # 여기에 자료를 푸쉬 팝을 할 거다. 힙이라 가정

# -1이 들어오기 전까지는 루프가 돌아야한다.
while True:
    n = int(input())
    if n == -1:
        break
    # 들어오는 n이 0일 때
    if n == 0:
        # 힙에 아무것도 없을 때
        if len(a) == 0:
            print(-1)
        # 힙에 자료가 있을 때 -> 힙에서 데이터 출력
        else:
            # hq.heappop()을 하면 힙에서 가장 작은 값을 꺼낸다.
            print(hq.heappop(a))
    # 0이 아닐 때
    # 값을 힙에다 push()해줘야한다.
    # 이때 hq.heappush()를 쓰자
    else: # hq.heappush(리스트, 인자) -> 리스트에 힙 구성으로 인자를 넣자
        hq.heappush(a, n)

