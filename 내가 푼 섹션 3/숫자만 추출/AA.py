import sys
sys.stdin = open("input.txt", "rt")

string = input()



# 자동으로 최고 첫자리는 0이 무시되게 숫자를 조합하는 알고리즘
res = 0
for x in string:
    # print(x, end=" ")
    if x.isdecimal(): # 0부터 9까지의 수인지 알 수 있다. 
        res=res*10+int(x) # 모든 숫자는 다 찾아줌 -> string.isdigit()
print(res)


#약수 갯수 출력하기
count = 0
for i in range(1,res+1):
    if res%i == 0:
        count += 1
print(count)