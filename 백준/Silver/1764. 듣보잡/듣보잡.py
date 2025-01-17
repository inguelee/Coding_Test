# 입력 처리
import sys
input = sys.stdin.read
data = input().splitlines()

N, M = map(int, data[0].split())  # 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
not_heard = set(data[1:N+1])  # 듣도 못한 사람의 명단
not_seen = set(data[N+1:])  # 보도 못한 사람의 명단

# 교집합 구하기
heard_and_seen = sorted(not_heard & not_seen)

# 출력
print(len(heard_and_seen))
print("\n".join(heard_and_seen))
