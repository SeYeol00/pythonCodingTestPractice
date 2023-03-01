import sys
sys.stdin = open("input.txt", "rt")

# 후위식 계산 문제는 스택에 숫자를 넣는다!!

# 연산자를 만나면 스택에서 2개를 빼낸다.
# 나중에 나온게 앞쪽, 먼저 나온게 뒤쪽으로 간다.
# 연산 결과를 스택에 append

fomula = input()
stack = []

for x in fomula:
    if x.isdecimal(): # 숫자로 변환 잊지 맙시다. 함수로 적는 것도 잊지 맙시다.
        stack.append(int(x))
    
    elif x =='+':
        b = stack.pop()
        a = stack.pop()
        result = a + b
        stack.append(result)

    elif x =='-':
        b = stack.pop()
        a = stack.pop()
        result = a - b
        stack.append(result)

    elif x =='*':
        b = stack.pop()
        a = stack.pop()
        result = a * b
        stack.append(result)
    
    elif x =='/':
        b = stack.pop()
        a = stack.pop()
        result = a / b
        stack.append(result)

print(stack.pop())
