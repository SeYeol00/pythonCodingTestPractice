import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

need = input()

n = int(input())

# 파이썬에서는 for - else 가 있다.

# 입력 순서 그대로 지켜야한다. -> 큐
# 아니다 선위 -> 후위 같이 순서를 바꿔야한다. -> 스택

# for문과 같이 사용되는 else문은 
# for문이 break 등으로 중간에 빠져나오지 않고 
# 끝까지 실행 됐을 경우 else문이 실행되는 방식으로 진행됩니다.

for i in range(n):
    plan = input()
    # 스트링 객체를 넣어도 deque함수를 쓸 수 있다.
    dq = deque(need)

    for x in plan:
            # in 외워두기, 핵심
            # x가 C B A 에 있냐?
        if x in dq:
            if x!=dq.popleft():
                print(f"#{i+1} NO")
                break

    # break가 즐어간 if문이 실행이 되지 않았을 때 실행
    # 정상적으로 출력한 뒤에 마지막 체크시 사용
    else:
        if len(dq)==0:
            print(f"#{i+1} YES")
        else:
            print(f"#{i+1} NO")