import sys
sys.stdin = open("input.txt", "rt")



# sm = 0
# for i in range(n):
#     plus_list[i] = sm + lst[i]
#     sm += lst[i]

#print(plus_list)


def Count(capacity):
    cnt = 1
    sum = 0
    for i in lst:
        # 누적합이 캐패시티 넘을 때
        if (sum+i)>capacity:
            # dvd 갯수 한 번 세주고
            cnt+=1
            # 현재 기준의 음악을 새로 잡아서 계산하자
            sum = i
        # 넘지 않으면 계속 더해준다.
        else:
            sum+=i
    return cnt

n, m = map(int,input().split())

lst = list(map(int,input().split()))

plus_list = [0]*9

mx = max(lst)

s = 1 #1분이 최소
e = sum(lst)
res = 0

while s<=e:
    middle = (s+e)//2
    # 갯수를 출력, 미들을 총합의 기준으로 두고 제한
    # 미들은 dvd의 용량
    if Count(middle) > m:
        s = middle + 1
    
    # 갯수가 m이랑 같아도 가능
    # 미들이 적어도 리스트의 가장 긴 노래보다 같거나 커야한다.
    # 무작정 갯수가 m보다 작거나 같다고 허용하면 안됨, 그럼 노래 길이 문제가 생긴다.
    elif middle >= mx and Count(middle) <= m:
        # 여기서 답을 정해주어야함
        res = middle
        e = middle - 1

# 최솟값을 뽑으랬으니 미들 바로 위를 뽑아라
print(res)