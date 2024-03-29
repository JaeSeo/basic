# 재귀 함수
# 파라미터로 정수값 n을 받고 n의 각 자릿수의 합을 리턴해주는 재귀함수 sum_digits를 쓰세요. 반복문을 쓰지 말고, 재귀(recursion)의 개념을 활용해주세요!

# # n의 각 자릿수의 합을 리턴
# def sum_digits(n):
#     # 코드를 작성하세요.

# # 테스트
# print(sum_digits(22541))
# print(sum_digits(92130))
# print(sum_digits(12634))
# print(sum_digits(704))
# print(sum_digits(3755))
# 14
# 15
# 16
# 11
# 20

# n의 각 자릿수의 합을 리턴
# 내 답안
# def sum_digits(n):
#     if len(str(n)) == 1:
#         value = str(n)[0]
#         int_value = int(value)
#         return int_value
    
#     index = len(str(n)) - 1
#     value = str(n)[index]
#     int_value = int(value)
#     return int_value + sum_digits(str(n)[:index])

# n의 각 자릿수의 합을 리턴
def sum_digits(n):
    if n < 10:
        return n
    else:
        str_n = str(n)
        return int(str_n[0]) + sum_digits(int(str_n[1:]))

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))