import sys
sys.stdin = open("input.txt", "rt")

# 해쉬 -> 딕셔너리
# 자바 해쉬맵 -> 딕셔너리
# 어떻게 보면 json이다.

word_one = input()
word_two = input()

dct_one = {}
dct_two = {}

# for char in word_one:
#     dct_one[char] = 0

# for char in word_one:
#     dct_one[char]+=1

# 위 계산이 아래에서 한 방에 해결된다.
# char라는 키가 있으면 1을 더하고 없으면 0을 기본값으로 넣어라
for char in word_one:
    dct_one[char] = dct_one.get(char,0)+1


# for key, val in dct_one.items():
#     print(key,val)

# print("\n")

# for char in word_two:
#     dct_two[char] = 0

# for char in word_two:
#     dct_two[char]+=1

# 위 계산이 아래에서 한 방에 해결된다.
# char라는 키가 있으면 1을 더하고 없으면 0을 기본값으로 넣어라
for char in word_two:
    dct_two[char] = dct_two.get(char,0)+1

# for key, val in dct_two.items():
#     print(key,val)



# 핵심 알고리즘

# 키값만 접근하고 싶다.
# 큐도 그렇고 in이라는 함수가 중요하다. 
# in을 생각하면 어디 어디에 있냐 이게 떠올려진다.
for i in dct_one.keys():
    # word_one에는 있는데 word_two에는 없으면 안된다.
    # 아나그램은 모든 원소들이 같이 존재해야하는 것이다.
    if i in dct_two.keys():
        # 갯수 비교 
        if dct_one[i] != dct_two[i]:
            print("NO")
            break
    else:
        print("NO")
        break

# 정상 케이스
else:
    print("YES")


#  위랑 아래를 비교해봅시다.

print("\n")
Hash = {}



# 개선 코드

for char in word_one:
    Hash[char] = Hash.get(char,0)+1

print(Hash)

for char in word_two:
    Hash[char] = Hash.get(char,0)-1

# 이러면 하나의 딕셔너리를 이용해서 풀 수 있다.

print(Hash)


for x in word_one:
    if Hash.get(x) != 0:
        print("NO")
        break
else:
    print("YES")