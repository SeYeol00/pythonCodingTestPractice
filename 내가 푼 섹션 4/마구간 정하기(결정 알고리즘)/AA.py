import sys
sys.stdin = open("input.txt", "rt")

n,m = map(int, input().split())

lst = [0]*n

for i in range(n):
    lst[i] = int(input())

lst.sort()
print(lst)

# 가장 가까운 두 말의 거리를 그리면서 숫자를 나열해보자
# 가장 가까운 두 말의 거리는 결국 lst[n-1]을 넘지 않는다.
# 그 다음은 중간값을 생각해보자 (1+9)//2 = 5 일 것 아닌가
# 5가 답이 되는가? 가장 가까운 두 말의 거리 == 5??
# 모든 말의 거리는 5보다 크거나 같아야 답이 된다.
# 1 = start point, 9 = end point
# 2 -1은 5보다 작아서 안 됨 그 다음은 4 - 1
# 8 - 1은 7 즉 1, 8
# 그 다음은 어차피 5보다 작아서 배치 불가 즉 5로는 2마리가 한계
# 그러면 5보다 작은 4를 엔드 포인트로 하고 다시 돌리자 => 2
# 2는 되는가? 


# 추가 구현을 고민해라
def Count(len):
    cnt = 1
    e = lst[0] # 첫번 째에 배치 완료

    # 두 번째 배치 잡기
    for i in range(1,n):
        if (lst[i] - e) >= len:
            # 이러면 다음 말을 배치 가능하다.
            cnt+=1
            e = lst[i]
    return cnt # 배치한 말의 갯수


s = lst[0]
e = lst[n-1]
res = 0
while s<=e:
    mid = (s+e)//2
    # mid는 검증 기준
    # 답이 되는 기준
    if Count(mid)>=m:
        res = mid
        s = mid + 1
        
    else:
        e = mid - 1
print(res)