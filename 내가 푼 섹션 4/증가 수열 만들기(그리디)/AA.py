import sys
from collections import deque
sys.stdin = open("input.txt", "rt")

n = int(input())


# 왼 쪽 끝 혹은 오른쪽 끝 -> deque
lst = list(map(int,input().split()))


# 가장 긴 , 최대 등등의 워딩은 그리디...
# 그리디 => 튜플 정렬, 리스트 정렬, 덱 등등 혹은 투 포인터로 움직이던
# 투 포인터 전략
# 그리디 -> 어떻게든 정렬이 개입된다.

s = 0
e = n - 1
last = 0
res = ""
# 이 리스트는 두 개 혹은 하나만 넣을 거라 임시용이다.
temp = []

# 그냥 괄호 두 개면 튜플 생성된다. 시발
while s<=e:
    if lst[s]>last:
        temp.append((lst[s],"L"))
    if lst[e]>last:
        temp.append((lst[e],"R"))

    # 둘 중에 작은 값을 다음 수열의 값으로 지정해야한다.
    temp.sort(key=lambda x : x[0])
    # 안 들어 갔을 때
    if len(temp) == 0:
        break

    last = temp[0][0]
    res+=temp[0][1]

    if temp[0][0] == lst[s]:
        s+=1
    elif temp[0][0] == lst[e]:
        e-=1
    # 비워주자
    temp.clear()

# 문자열의 길이가 곧 길이
print(len(res))
print(res)




# word = ""

# # print(x,end="")
# # 전에 꺼
# count = 0
# before = 0
# while len(lst) > 1:
#     a = lst[0]
#     b = lst[-1]
    
#     if a > b and b > before:
#         # print("R",end="")
#         word += "R"
#         before = b
#         lst.pop()
#         count+=1
#     elif a < b and a > before:
#         word += "L"
#         before = a
#         lst.popleft()
#         count+=1
#     elif a > b and b < before and a > before:
#         word += "L"
#         before = a
#         lst.popleft()
#         count+=1
#     elif a < b and b > before and a < before:
#         word += "R"
#         before = b
#         lst.pop()
#         count+=1

# if before < lst[0]:
#     word += "L"
#     lst.popleft()
#     count+=1   
# print(count)
# print(word)
    