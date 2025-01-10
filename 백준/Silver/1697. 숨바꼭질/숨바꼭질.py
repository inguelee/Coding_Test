from collections import deque

def bfs(n, k):
    # 최대 범위 (문제 조건에서 주어진 값)
    max_range = 100001
    # 방문 여부와 해당 위치까지 걸린 시간을 저장하는 리스트
    visited = [0] * max_range

    # BFS 초기화
    queue = deque([n])
    visited[n] = 1  # 시작 위치 방문 처리

    while queue:
        current = queue.popleft()

        # 목표 위치에 도달하면 종료
        if current == k:
            return visited[current] - 1  # 초기값 1을 빼서 실제 시간 반환

        # 다음 가능한 이동 위치 탐색
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos < max_range and not visited[next_pos]:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

# 입력 처리
n, k = map(int, input().split())
print(bfs(n, k))
