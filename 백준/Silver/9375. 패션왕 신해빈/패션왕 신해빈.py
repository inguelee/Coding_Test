# 입력 처리
import sys
input = sys.stdin.read
data = input().splitlines()

# 테스트 케이스 수
T = int(data[0])
result = []

# 각 테스트 케이스 처리
index = 1
for _ in range(T):
    n = int(data[index])  # 의상의 수
    index += 1
    
    if n == 0:
        result.append(0)
        continue

    clothes = {}
    for _ in range(n):
        name, category = data[index].split()
        index += 1
        
        # 종류별 의상 개수 기록
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1

    # 경우의 수 계산
    combinations = 1
    for count in clothes.values():
        combinations *= (count + 1)  # 입지 않는 경우 포함

    result.append(combinations - 1)  # 알몸 제외

# 출력
print("\n".join(map(str, result)))
