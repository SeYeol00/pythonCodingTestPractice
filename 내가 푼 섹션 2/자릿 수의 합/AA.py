import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

lst = list(map(int,input().split()))

# print(n)
# print(lst)

# print(lst)


# def digt_sum(lst):
#     max_index = 0
#     max = lst[0]
#     for i in range(len(lst)):
#         n = lst[i]
#         plus = 0
#         while n > 10:
#             plus+= n%10
#             n = n//10 # 소수 점 안 나오는 거
#         plus+=n
#         if max > plus:
#             max_index = i

#     print(lst[max_index])


def digit_sum(x):
    sum=0
    for i in str(x): #str로 문자열화 시켜준다.
        sum+=int(i)
    return sum

max = 0
for x in lst:
    tot = digit_sum(x)
    if tot>max:
        max = tot
        res = x
print(res)