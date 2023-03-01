import sys
sys.stdin = open("input.txt", "rt")

#자동으로 들어간다.
lst = list(range(21))

for _ in range(10): #언더바로 하면 변수없이 반복되서 시간이 적게 걸림
    a, b =map(int,input().split())
    #mock을 쓰자, 아래가 핵심, 이러면 가운데 제외하고 각각 반대의 지점을 바꿀 수 있다.
    for i in range((b - a + 1)//2): #횟수 지정
        lst[a+i], lst[b-i] = lst[b-i],lst[a+i]

for i in lst[1:]:
    print(i,end=' ')
# deck = [0]*20

# for i in range(len(deck)):
#     deck[i] = i+1

#print(deck)


#a,b =map(int,input().split())
#파이썬 스왑 공식
# a,b = b,a


