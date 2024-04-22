# 1. input()보다 sys.stdin.readline()이 더 빠르다.
import sys

# 한 개의 정수를 입력
n = int(sys.stdin.readline())

# 한 개의 문자를 입력
n = sys.stdin.readline().rstrip()
# sys 라이브러리를 사용할 때는 한 줄 입력받고 나서 rstrip() 함수를 꼭 호출해야 한다.

# 띄어쓰기로 구분된 두 개의 정수를 입력
a, b = [int(x) for x in sys.stdin.readline().split()]

# 띄어쓰기로 두 문자열 입력
c, d = sys.stdin.readline().split()

# 띄어쓰기로 구분되어 있는 배열을 입력
arr = [int(x) for x in sys.stdin.readline().split()]

# 2. if문에 두 개 이상의 조건이 주어질 때, 조건의 순서를 생각하면서 작성한다.
if condition1 and condition2:
  pass

if condition1 or condition2:
  pass

# 3. 문자열을 붙일 때 +연산 대신 join()을 사용한다.
## + 연산
for str in string_list:
	concatenate_string += str

## join()함수
concatenate_string = "".join(string_list)

# 4. List Comprehension을 사용한다.
## for loop
numbers = []
for i in range(1000):
	numbers.append(i) # (X)
    
## comprehension
numbers = [i for i in range(1000)]

# + 배열을 만들때 for loop을 돌리는 것보다 multiplication으로 할당하는 것이 빠르다!

## 7의 배수 10개 저장하기
# 수정 전
arr = []
for num in range(1, 11):
    arr.append(num * 7)
    
# 수정 후
arr = [0 for _ in range(10)]
for num in range(1, 11):
    arr[num] = num * 7

# [1, 2, 3, 4]를 줄바꿈으로 하나씩 출력하기
# 1
# 2
# 3
# 4

# 수정 전
arr = [1, 2, 3, 4]
for n in arr:
    print(n)
    
# 수정 후
answer = ""
for n in arr:
    answer += str(n) + '\n'
print(answer) # print(answer[:-1]) 대신 print(answer.rstrip())쓴다!!!




# 수정 전
queue = []
for i in range(N):
	queue.append(i)
for i in range(N):
    print(queue[-1])
    queue.pop(-1)

# 수정 후
from collections import deque

queue = deque()
for i in range(N):
	queue.append(i)
for i in range(N):
	queue.popleft()
