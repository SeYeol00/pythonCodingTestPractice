import sys, math
sys.stdin = open("input.txt", "rt")


n = int(input())

compare = []


# for i in range(n):
#     lst = list(map(int,input().split()))
#     num = 0
#     cal = 0
#     same = 0
#     for j in range(0,2):
#         for k in range(j+1,3):
#             if lst[j]==lst[k]:
#                 same+=1
#                 cal = lst[j]
#     if same == 0:
#         num = max(lst)
#         compare.append(num*100)
#     elif same == 1:
#         num = 1000 + cal*100
#         compare.append(num)
#     else:
#         num = 10000 + cal*1000
#         compare.append(num)
# print(max(compare))

res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort() # nlogn일텐데 퀵 소트
    a,b,c = map(int,tmp)
    if a==b and b ==c:
        money=10000 + a*1000
    elif a==b or b==c:
        money=1000+(a*100)
    elif b==c:
        money=1000+(b*100)
    else:
        money=c*100

    if money > res:
        res = money

print(res)