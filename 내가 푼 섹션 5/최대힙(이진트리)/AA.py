import sys
import heapq as hq # 파이썬에서는 힙큐라는 것이 존재한다.
sys.stdin=open("input.txt","r")


# 최대힙은 최소힙에서 약간 변경만 하면 된다.

# heapq는 기본적으로 최소 힙으로 작동한다.

# 최대힙의 효과를 내려면 입력을 할 때 부호를 바꿔버려야한다.
# 예를 들어 3과 4를 넣어버리면 최소힙일 때는 그대로 3 - 4 가 되겠지만
# 마이너스 부호를 붙여서 넣으면 -3 - -4가 되어 한 번 스왑을 해야한다.
# ->  -4 - -3
# 그다음 hp.heappop()을 할 때 다시 마이너스를 붙여서 꺼내면
# -(-4) = 4 가 되어서 정상 출력이 된다.
# 즉 힙큐에서 저장하고 있을 때는 모든 원소가 - 부호를 가지고 있는 것이다.
# 그 상태로 힙정렬을 하면 부호가 없는 상태에서는 
# 최대힙의 성질을 가지고 있는 것이다.

a = []

while True:
    n =  int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-(hq.heappop(a))) # 이 때가 중요
    else:
        hq.heappush(a, -n) # 이 떄가 중요

# 즉 이진트리의 힙 로직은 최소힙인데
# 입력과 출력에서 부호를 반대로 바꾸어 주기 때문에 
# 결과적으로 최대 힙의 효과를 내는 것이다.


