def max_fruit_tanghulu_length(N, fruits):
    from collections import defaultdict

    left = 0
    fruit_count = defaultdict(int)
    max_length = 0

    for right in range(N):
        fruit_count[fruits[right]] += 1

        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1

        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length

# 입력 처리
N = int(input())
fruits = list(map(int, input().split()))

# 결과 출력
print(max_fruit_tanghulu_length(N, fruits))
