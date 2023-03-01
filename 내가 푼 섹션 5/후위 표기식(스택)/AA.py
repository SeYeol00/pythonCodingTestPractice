import sys
sys.stdin = open("input.txt", "rt")

fomula = input()

stack = []

# 파이썬은 스트링을 더할 수 있다.
res = ''

# 더하기와 뺴기는 스택에 넣어두고 숫자는 그대로 출력
# 곱하기와 나누기를 만났으면 스택에서 곱하기와 나누기만 꺼내야한다.
# 없으면 곱하기 혹은 나누기를 넣는다.
# 여는 괄호가 나왔으면 일단 스택에 넣고
# 닿는 괄호가 나올 때 여는 괄호 전의 연산자들을 우선순위를 통해 pop()한다.
# 즉 여는 괄호 뒤에 연산자를 만나면 여는 괄호 뒤에 들어간 연산자를 연산처리한다.
# 여는 괄호 뒤에 연산자가 없으면 그냥 현재를 넣는다.
# 우선순위가 높은 연산자를 스택의 상단에 위치시키는게 핵심이다.

# 기본적으로 연산자면 자기 순서도 append 한다는 것을 잊지 말자

for x in fomula:
    if x.isdecimal():
        res+=x
    else:
        if x == '(':
            stack.append(x)

        # 연산자 우선순위 높음
        elif x == '*' or x == '/':

            # ~~할 동안
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res+=stack.pop()
            stack.append(x)

        # 연산자 우선순위 낮음
        elif x == '+' or x == '-':
            while stack and stack[-1] !='(':
                res+=stack.pop()
            stack.append(x)

        elif x == ')':
            while stack and stack[-1] !='(':
                res+=stack.pop()

            # 여는 괄호 '(' 빼버리기
            stack.pop()

# 스택에 연산자가 남아있을 수 있다.
while stack:
    res+=stack.pop()

print(res)