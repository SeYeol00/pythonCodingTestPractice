import sys
sys.stdin = open("input.txt", "rt")

# 자기 앞에 지울 수 있는 숫자가 있으면 지운다.
# 5 2 7 6 8 2 3
# 5는 앞이 없음
# 2는 앞에 5가 있어서 그대로 적기
# 7은 앞에 2가 있어서 2를 지운다. 
# 그 다음에 앞에 5가 있으니 지운다.
# 6은 앞에 7이라 그대로 있는다.
# 8은 앞이 6이니 6을 지운다.
# 2는 그대로
# 3은 이미  5 2 6 즉 3개를 지웠으니 그대로 둔다.

# 스택을 사용하기
# 스택 -> 선입후출
# 파이썬에서는 따로 스택이 없고 리스트로 구현한다.

# 숫자를 스트링으로 한 다음에 리스트화
# 리스트가 비어있으면 처음 숫자를 넣는다. 
# 그 다음 원소는 스택에 있는게 자기보다 작으면 빼버리고 아니면 원소를 넣는다.
# 스택의 탑을 리스트의 [-1]로 구현하면 쉽다.
# list 함수 내에 pop()이 있기 때문에 파이썬에서는 스택이 없다.
# 이런 식의 알고리즘을 짜면 내림차순으로 스택이 정리된다.
# 남은 숫자를 m개라 치면 남은 걸 다 넣고 
# 리스트의 인덱싱을 통해 list[:-m]을 해버리면 정리가 된다.


num,m = map(int, input().split())

# 숫자로 들어온 배열을 스트링화하고 다시 숫자로 만든다.
# 스트링으로 바꿔야 자바의 toCharArray처럼 쪼개진다.
num=list(map(int,str(num)))

# 리스트를 스택 삼아 쓸 거다.
stack=[]

last = 0
for x in num:
    # 스택이나 큐를 쓸 때는 while문을 적극 활용하자.
    # m은 숫자를 지울 때마다 1씩 줄일 거다.
    # 스택의 top이 x보다 작으면 끄집어 낼 것이기 때문이다.
    # 즉 스택의 탑이 x보다 커야 반복을 멈추고 x를 append할 것이다.
    while len(stack)>0 and m>0 and stack[-1] < x:
        stack.pop()
        # pop()을 했으므로 1번 숫자를 지운 것
        m-=1
    stack.append(x)

# 횟수는 남았는데 이미 스택에 다 들어가버린 상황
# 이 때는 계속 1의 자리의 숫자를 m만큼 지워야 한다.
if m>0:
    while m>0:
        stack.pop()
        # pop()을 했으므로 1번 숫자를 지운 것
        m-=1

for x in stack:
    print(x,end="")