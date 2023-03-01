import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

list = list(map(int,input().split()))

# print(n)
# print(list)

sum = 0

for i in list:
    sum+=i

average = int(sum/n)

dif = []

#정수형에서 가장 큰 값
min = 2147000000

#abs() -> 절댓값 함수
for i in range(len(list)):
    temp = abs(list[i]-average)
    if temp < min:
        min = temp
        score = list[i] # 미니멈의 점수 저장
        res = i +1
    elif temp == min:
        if list[i] > score: #절댓값이 최솟값과 같을 때 점수가 큰 걸 쓴다.
            score = list[i]
            res = i +1


print(average, res)