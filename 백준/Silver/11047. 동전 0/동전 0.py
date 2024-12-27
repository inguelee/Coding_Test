# 입력 처리
from sys import stdin

N, K = map(int, stdin.readline().split())
coins = [int(stdin.readline().strip()) for _ in range(N)]

# 필요한 동전 개수 계산
count = 0
for coin in reversed(coins):  # 큰 동전부터 사용
    if K == 0:
        break
    count += K // coin  # 현재 동전으로 채울 수 있는 개수
    K %= coin  # 남은 금액

print(count)
