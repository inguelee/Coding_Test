def solution(num_list):
    odds = 0
    evens = 0
    for i in range(0, len(num_list), 2):
        odds += num_list[i]
    for i in range(1, len(num_list), 2):
        evens += num_list[i]
    answer = max(odds, evens)
    return answer