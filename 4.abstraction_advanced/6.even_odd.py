# 짝수? 홀수?
# 짝수인지 홀수인지 판단해주는 is_evenly_divisible 함수를 쓰세요.

# is_evenly_divisible는 number(수)를 파라미터로 받습니다.
# 짝수인 경우에는, 즉 number가 2로 나누어 떨어질 경우에는 True를 리턴해줍니다.
# 홀수인 경우에는, 즉 number가 2로 나누어 떨어지지 않을 경우에는 False를 리턴해줍니다.

# 함수 안에는 print문을 사용하시면 안 되고, return문을 사용하여야 합니다.
# '불린' 개념을 사용하면, 함수 단 '한 줄'로 쓸 수 있습니다!

# def is_evenly_divisible(number):
#     # 코드를 작성하세요

# print(is_evenly_divisible(3))
# print(is_evenly_divisible(7))
# print(is_evenly_divisible(8))
# False
# False
# True

def is_evenly_divisible(number):
    return number % 2 == 0

print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))

# 해설
# 짝수인지 홀수인지 판단해주려면, is_evenly_divisible 함수의 파라미터인 number가 2로 나뉘어 떨어지는지 아닌지를 확인해주어야 합니다. 짝수이면 True를, 홀수이면 False를 리턴해주어야 하는데요. 참 또는 거짓을 판단하는 불린 자료형과 관련된 문제임을 알 수 있죠?

# 불린 자료형에서 배운 내용을 복습해보면, 7 % 2 == 0은 False이고, 8 % 2 == 0은 True이죠?
# 이를 일반화하면 number % 2 == 0가 되는데, 이 코드는 number가 짝수일 경우 True가 되고, 홀수일 경우 False가 됩니다. 이를 return문과 함께 작성해주면 됩니다!

# # is_evenly_divisible 함수
# def is_evenly_divisible(number):
#     return number % 2 == 0

# print(is_evenly_divisible(3))
# print(is_evenly_divisible(7))
# print(is_evenly_divisible(8))