# 입력 처리
import sys
input = sys.stdin.read
data = input().splitlines()

# 유저 수 N, 친구 관계 수 M
N, M = map(int, data[0].split())

# 무한대 값 정의
INF = float('inf')

# 그래프 초기화
dist = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dist[i][i] = 0  # 자기 자신까지의 거리는 0

# 친구 관계 입력
for i in range(1, M + 1):
    A, B = map(int, data[i].split())
    dist[A][B] = 1
    dist[B][A] = 1

# 플로이드-워셜 알고리즘
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 케빈 베이컨 수 계산
min_kevin_bacon = INF
min_user = 0

for i in range(1, N + 1):
    kevin_bacon = sum(dist[i][1:])  # i번째 사람의 케빈 베이컨 수
    if kevin_bacon < min_kevin_bacon:
        min_kevin_bacon = kevin_bacon
        min_user = i
    elif kevin_bacon == min_kevin_bacon:  # 같은 경우에는 번호가 작은 사람 우선
        min_user = min(min_user, i)

# 결과 출력
print(min_user)
