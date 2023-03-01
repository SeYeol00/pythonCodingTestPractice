import sys
sys.stdin = open("input.txt", "rt")

# 해쉬 -> 딕셔너리
# 자바 해쉬맵 -> 딕셔너리
# 어떻게 보면 json이다.


n = int(input())


# 딕셔너리 선언
p = dict()

for _ in range(n):
    word = input()

    # 그냥 리스트 처럼 넣어버리면 된다.
    p[word] = 0

# print(p)

for _ in range(n-1):
    check = input()
    p[check]+=1

# 딕셔너리 출력하기
for key, val in p.items():
    # print(key, val)
    if val == 0:
        print(key)

# for i in p:
#     if p[i] == 0:
#         print(i)