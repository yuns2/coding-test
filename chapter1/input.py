# 1
n = int(input())  # 데이터의 개수 입력

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 2 : 공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k = map(int, input().split())
print(n, m, k)
print(m)

# 3
import sys
data = sys.stdin.readline().rstrip()
print(data)