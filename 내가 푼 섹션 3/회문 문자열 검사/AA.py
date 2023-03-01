import sys
sys.stdin = open("input.txt", "rt")

n = int(input())

for i in range(1,n+1):
    string = str(input()).upper() # 전부 대문자화 시키는 메서드 외우기
    reversed = string[::-1]       # string.lower => 전부 소문자화
    # for j in range(len(string)//2):
    #       if string[j] != string[-1-j]:
    if string==reversed:
        print(f"#{i} YES")
    else:
        print(f"#{i} NO")