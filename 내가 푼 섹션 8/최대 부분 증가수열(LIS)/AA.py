import sys
sys.stdin=open("input.txt","r")

# 인덱스를 돌면서 현재 인덱스의 수가 부분 중가 수열의 마지막 항이라고 생각하자
# 부분 증가 수열 => dp 점화식 문제

# memo를 만들어 각 자리가 마지막 항이 되는 수열의 최대 길이를 준다.
# 다음 memo에 전에 수열을 만들 수 있는 값들 중 가장 큰 값에 + 1

# 즉 전 항들이 가능한 값들 중 가장 큰 값을 정해서 + 1 하는 것이다.

# 그 다음 memo 값들 중에 가장 큰 값이 최대 길이가 된다.


if __name__ == "__main__":
    n = int(input())
    # 1번 부터 인덱스에 맞춰서 할게용
    arr = list(map(int, input().split()))
    arr.insert(0, 0)

    memo = [0] * (n+1)
    memo[0] = 0
    # 1번 인덱스는 1로 초기화
    memo[1] = 1

    res = 0

    # for 문을 두 번 돈다.
    for i in range(2,n+1):
        max = 0
        # i 바로 앞에서 부터 돌아야하니까 i-1이 되어야한다.
        # 즉 i번째면 i 앞쪽 부터 1번까지 돌면서 arr[i]보다 작은 값을 찾는다.
        for j in range(i-1, 0 , -1):
            # 부분 증가 수열의 조건을 만족할 때
            if arr[j] < arr[i]:
                if memo[j] > max:
                    max = memo[j]    
            memo[i] = max + 1
        # memo 값 중에 가장 큰 값을 찾자 => 최대 길이
        if memo[i] > res:
            res = memo[i]
    
    print(res)

        

    # 최대 부분 증가수열은 또 하나의 리스트가 필요하다.

    
    