import sys
sys.stdin = open("input.txt", "rt")

# 쇠막대기의 표현을 괄호로 표현
# 닫는 괄호가 바로 나오면 레이저, 아니면 카운팅 시작하기
# 그 이외의 닿는 괄호가 나오면 바로 뒤를 체크하고 그게 여는 괄호가 아니면 쇠막대기로 카운팅
# 닿는 괄호의 쇠막대기가 나오면 카운팅
# 스택이라는 자료 구조를 사용하면 가능하다.
# 파이썬의 리스트 인덱싱이 너무 깡패라 스택 대용으로 쓰는 거다.
# len(stack)을 sum에다 누적하자.
# 레이저, 레이저면 또 sum에 누적한다. 
# 닿는 괄호, 닿는 괄호면 막대기가 끝나는 것으로 sum에 하나 더하기
# 막대기가 끝나는 지점은 pop()하고 카운팅 하자

# lst = list(map(str,input()))

# print(lst)

s = input()

stack =[]

cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        # 아직 안 잘렸음
    else:
        if s[i-1] == '(':
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1

print(cnt)

            



