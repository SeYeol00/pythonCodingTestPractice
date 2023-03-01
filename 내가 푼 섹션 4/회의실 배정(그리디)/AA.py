import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

# 그리디 알고리즘 -> 단계에서 제일 좋은 것을 선택하는 것
# 그리디 알고리즘 -> 정렬
# 정렬한 다음에 차례차례 선택해나가면 된다.
# 거의 대부분 그리디는 정렬과 같이 동반된다.


# 최대 사용할 수 있는 회의 수 => 그리디
# 그리디 시작
# 회의가 끝나는 시간을 기준으로 정렬한다.
# 그리디는 대부분 쌍을 쥐어준다.
# 시작 시간이 중요한게 아니라 끝나는 시간이 빨리 끝나는게 중요하다.
# 시간이 크거나 같으면 진행 가능
# 끝나는 시간을 기준으로 정렬 시키고 이어붙이는 느낌

meeting = []
# 그리디 -> 튜플, 리스트, 정렬
# 쌍이 나오면 튜플 형태로 저장하는 것을 유념하자!!!!!!!!
for _ in range(n):
    time = tuple(map(int,input().split()))
    meeting.append(time)

print(meeting)

# 외워두자 정렬하는 키의 기준
# 람다 함수를 써야한다.
# 핵심         x는 원소고 x의 1번을 첫 순위, x의 0번을 후순위로 둬라
meeting.sort(key=lambda x : (x[1],x[0]))
print(meeting)
cnt = 0
# 끝나는 시간은 기록해두자, temp와 같다
end_time = 0
for i in range(len(meeting)):
    s = meeting[i][0]
    e = meeting[i][1]
    if s >= end_time:
        cnt+=1
        end_time = e
    
print(cnt)

