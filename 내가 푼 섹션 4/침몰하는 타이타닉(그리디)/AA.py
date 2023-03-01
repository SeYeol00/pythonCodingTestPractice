import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

n, m = map(int,input().split())

# 리스트는 pop하면 뒤에 자료들이 당겨지는 연산을 해서 비효율적이다.
# 이런게 시간을 잡아 먹으니 빼고 넣을 때는 deque를 쓰는게 좋다.
line = list(map(int, input().split()))

line.sort()
line = deque(line)

print(line)

# 그리디 -> 정렬 혹은 역정렬 -> 최대한 셀 수 있는 방안 구상
# 투 포인터로 양쪽 끝에서 더해야 최대로 셀 수 있다.
# 가우스 계산법과 같은 느낌
# 둘이 더한게 리미트를 넘어가면 오른쪽만 pop(len(line)-1) 하면 된다.
# 둘이 더한게 리미트 아래면 둘 다 pop
# 이후에 포인터를 옮긴다.
# s = 0
# e = n - 1

cnt = 0
limit = m

# line이란 deque에 원소가 존재하는 동안
# 핵심 그리디 알고리즘
# deque를 쓰는 방법을 외워두자
while line:
    if len(line) == 1:
        cnt+=1
        break
    if line[0] + line[-1]>limit:
        line.pop()
        cnt+=1
    else:
        # deque의 효율적인 메서드
        line.popleft()
        line.pop()
        cnt+=1
print(cnt)




# while s <= e:
#     print(s,e)
#     print(line)
#     # 길이가 1만 남을 수 있다. 이럴 때 에러가 날 수 있다.
#     # 그래서 하나만 남을 때는 pop해서 없애주자
#     if len(line)==1:
#         line.pop()
#         cnt+=1
#         break

#     if (line[s] + line[e]) > limit:
#         if line[e] > limit:
#             line.pop(e)
#             e-=1
#         else:
#             line.pop(e)
#             cnt+=1
#             e-=1
            
#     else:
#         line.pop(e)
#         line.pop(s)
#         cnt+=1
#         # 동시에 pop이 양 끝에서 되므로 -2를 해줘야한다.
#         e-=2
# print(cnt)