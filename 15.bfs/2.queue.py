BFS 알고리즘을 구현하기 위해서는 'queue'라는 것을 사용해야 합니다.

Queue는 직역을 하면 '(무엇을 기다리는 사람, 자동차 등의) 줄', 또는 '대기 행렬'입니다.

컴퓨터 프로그래밍에서 queue는 리스트처럼 여러 값을 보관하는데요. Queue에 값을 추가하면 순서대로 대기를 하고, queue에서 값을 빼면 들어간 순서대로 나오게 됩니다.

deque
파이썬에서 queue를 사용하기 위해서는 'deque (double-ended queue)'라는 것을 사용해야 하는데요. 예시를 통해 알아보겠습니다.

from collections import deque

# 새로운 queue 생성
numbers = deque()

# queue에 값 추가
numbers.append(2)
numbers.append(3)
numbers.append(5)
numbers.append(7)

print(numbers)
print(len(numbers))

# queue에서 하나 제거
x = numbers.popleft()
print(x)
print(numbers)
print(len(numbers))

# queue에서 하나 제거
x = numbers.popleft()
print(x)
print(numbers)
print(len(numbers))
deque([2, 3, 5, 7])
4
2
deque([3, 5, 7])
3
3
deque([5, 7])
2