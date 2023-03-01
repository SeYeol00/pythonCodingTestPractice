import sys
sys.stdin=open("input.txt","r")

# 무게 -> 금액

if __name__ == "__main__":
    n = int(input())
    
    coin_value = list(map(int, input().split()))
    
    # 금액
    limit = int(input())

    memo = [2147000]*(limit+1)
    memo[0] = 0
    
    for i in range(n):
        for j in range(coin_value[i],limit+1):
            if j%coin_value[i] == 0:
                if memo[j] > j%coin_value[i]:
                    memo[j] = j//coin_value[i]
            else: # 갯수로 생각을 해야한다. 메모에 들어가는 것은 갯수다.
                # 즉 코인의 가치를 뺀 만큼 그 갯수를 더해주는 것이다.
                # 막히면 메모에 무엇이 들어가는지 한 번 생각해보자
                if memo[j] > (memo[j-coin_value[i]] + 1):
                    memo[j] = memo[j-coin_value[i]] + 1


    print(memo[limit])