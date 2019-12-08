# 리스트 뒤집기
# 파라미터로 리스트 some_list를 받고, 뒤집힌 리스트를 리턴해주는 재귀 함수 flip을 쓰세요.

# 반복문은 쓰면 안됩니다!

# # 파라미터 some_list를 거꾸로 뒤집는 함수
# def flip(some_list):
#     # 코드를 입력하세요.

# # 테스트
# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# some_list = flip(some_list)
# print(some_list)
# [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 파라미터 some_list를 거꾸로 뒤집는 함수
# 내 답안
# def flip(some_list):
#     length = len(some_list)

#     def flip_order(list_provided, index):
#         if index >= length // 2:
#             return list_provided

#         temp = list_provided[index]
#         list_provided[index] = list_provided[length - index - 1]
#         list_provided[length - index - 1] = temp
#         return flip_order(list_provided, index + 1)

#     return flip_order(some_list, 0)

# 모범답안
def flip(some_list):
    if len(some_list) < 2:
        return some_list
    else:
        return flip(some_list[1:]) + some_list[:1]

# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)
[9, 8, 7, 6, 5, 4, 3, 2, 1]

# 해설
# 이 문제에서도 base case와 recursive case를 생각해야 합니다.

# Base Case
# Base case는 문제가 충분히 작아서 곧바로 풀 수 있는 경우인데요. 리스트의 요소가 아예 없거나 하나밖에 없는 경우에는 리스트를 뒤집어도 똑같죠? 따라서 base case로, 리스트의 길이가 2보다 작을 때 파라미터로 받은 리스트를 그대로 리턴시켜주면 됩니다.

# # 파라미터 some_list를 거꾸로 뒤집는 함수
# def flip(some_list):
#     if len(some_list) < 2:
#         return some_list
# Recursive Case
# Recursive case는 리스트의 요소가 두개 이상인 경우입니다.

# 파라미터 some_list로 리스트 [9, 2, 1, 3, 0]을 받고, flip 함수가 뒤집힌 리스트를 제대로 리턴해준다고 가정합시다. 뒤집힌 some_list([9, 2, 1, 3, 0])를 어떻게 재귀적으로 표현할까요?

# 보통 재귀적으로 문제를 풀때는 문제의 사이즈를 줄이는 것이 목표입니다. 원래 파라미터였던 [9, 2, 1, 3, 0]을 쪼개서 [9]와 [2, 1, 3, 0]으로 나눠봅시다.

# flip 함수가 제대로 작동하기 때문에 flip([2, 1, 3, 0])은 [0, 3, 1, 2]를 리턴해주겠죠? 그리고 그 끝에 [9]를 붙여주면 [0, 3, 1, 2, 9]가 나옵니다. 이걸 더 일반적으로 표현하면 flip(some_list[1:]) 뒤에 some_list[:1]를 붙여준 셈이죠.

# # recursive case
# else:
#     return flip(some_list[1:]) + some_list[:1]
# 모범 답안
# Base case와 recursive case가 모두 나와있는 모범 답안입니다:

# # 파라미터 some_list를 거꾸로 뒤집는 함수
# def flip(some_list):
#     if len(some_list) < 2:
#         return some_list
#     else:
#         return flip(some_list[1:]) + some_list[:1]