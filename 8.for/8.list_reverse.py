# 리스트 뒤집기
# 리스트에 있는 데이터의 순서를 거꾸로 뒤집는 방법을 생각해내려고 합니다.

# numbers = [2, 4, 6, 8, 10, 12, 14]

# # 리스트 뒤집기
# # 코드를 입력하세요.

# print("뒤집어진 리스트: " + str(numbers))
# 위와 같이 numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집어 아래의 내용이 출력되게 하세요.

# 뒤집어진 리스트: [14, 12, 10, 8, 6, 4, 2]

# 
# 내 답안
# numbers = [2, 4, 6, 8, 10, 12, 14]
# temp = []

# for i in range(len(numbers)):
#     temp.append(numbers[len(numbers) - i - 1])

# numbers = temp
# print("뒤집어진 리스트: " + str(numbers))

# 모범 답안

numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
for left_index in range(int(len(numbers) / 2)):
    # 오른쪽 인덱스 계산
    right_index = len(numbers) - left_index - 1

    # 원소 바꾸기
    temp = numbers[left_index]
    numbers[left_index] = numbers[right_index]
    numbers[right_index] = temp

print("뒤집어진 리스트: " + str(numbers))

# 해설
# 리스트에 요소가 7개 있으면 가장 왼쪽 인덱스는 0이고 가장 오른쪽 인덱스는 6입니다. 왼쪽에서 두번째 인덱스는 1이고 오른쪽에서 두번째 인덱스는 5입니다. 왼쪽에서 세번째 인덱스는 2이고 오른쪽에서 세번째 인덱스는 4입니다.

# 리스트를 가운데를 기점으로 반으로 나누면 대칭되는 두 인덱스의 합은 늘 6입니다. 이걸 통해서 알 수 있는 것은: 왼쪽 인덱스 + 오른쪽 인덱스 = 총 요소 개수 - 1

# 이걸 코드로 표현해봅시다. 리스트 numbers와 왼쪽 인덱스 left_index가 주어졌을 때, right_index는 이렇게 계산할 수 있습니다: right_index = len(numbers) - left_index - 1

# numbers = [2, 4, 6, 8, 10, 12, 14]

# # 리스트 뒤집기
# for left_index in range(int(len(numbers) / 2)):
#     # 오른쪽 인덱스 계산
#     right_index = len(numbers) - left_index - 1

#     # 원소 바꾸기
#     temp = numbers[left_index]
#     numbers[left_index] = numbers[right_index]
#     numbers[right_index] = temp

# print("뒤집어진 리스트: " + str(numbers))
# range(len(numbers)) 대신 range(int(len(numbers) / 2))를 하는 이유는 뭘까요?