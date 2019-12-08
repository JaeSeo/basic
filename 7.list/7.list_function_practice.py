# 리스트 함수 활용하기
# 리스트 함수를 활용하여 아래의 지시사항을 따르세요.

# numbers라는 빈 리스트를 만들어준다.

# append를 이용해서 numbers에 자연수 1부터 10까지의 값들을 추가한다. 즉 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]이 되게 만든다. 그 후 리스트를 출력한다.

# numbers 리스트의 원소들 중에 홀수는 모두 제거한다. 그 후 다시 리스트를 출력한다.

# numbers 리스트의 인덱스 0 자리에 20이라는 수를 삽입한 후 출력한다.

# 정렬이 되어있지 않으므로, numbers라는 리스트를 정렬한 후 출력한다.

# # 빈 리스트 만들기
# numbers = []

# # numbers에 자연수 1부터 10까지 추가
# # 코드를 입력하세요
# print(numbers)

# # numbers에서 홀수 제거
# # 코드를 입력하세요
# print(numbers)

# # numbers의 인덱스 0 자리에 20이라는 값 삽입
# # 코드를 입력하세요
# print(numbers)

# # numbers를 정렬해서 출력
# # 코드를 입력하세요
# print(numbers)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [2, 4, 6, 8, 10]
# [20, 2, 4, 6, 8, 10]
# [2, 4, 6, 8, 10, 20]
# (자동 채점 과제이기 때문에, 콘솔과 동일한 값이 출력되어야 합니다. )

# (문제의 조건을 정확히 따라주시기 바랍니다. 각각의 명령에 필요한 append, del, insert, sort 함수/메소드는 딱 한 번씩만 써야 합니다.)

# #

# 빈 리스트 만들기
numbers = []

# numbers에 자연수 1부터 10까지 추가
# 코드를 입력하세요
i = 1
while i <= 20:
    numbers.append(i)
    i += 1

print(numbers)

# numbers에서 홀수 제거
# 코드를 입력하세요
i = len(numbers) - 1
while i >= 0:
    if numbers[i] % 2 == 1:
        del numbers[i]
    i -= 1

print(numbers)

# numbers의 인덱스 0 자리에 20이라는 값 삽입
# 코드를 입력하세요
numbers.insert(0, 20)

print(numbers)

# numbers를 정렬해서 출력
# 코드를 입력하세요
print(sorted(numbers))
