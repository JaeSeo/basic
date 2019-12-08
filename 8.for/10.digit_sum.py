# 자리수 합 구하기
# 파라미터로 정수형 num의 값을 받는 sum_digit 함수를 쓰세요. sum_digit은 num의 각 자리수를 더한 값을 리턴해주는 역할을 합니다.

# 예를 들어 12의 각 자리수는 1, 2이므로 sum_digit(12)는 3(1 + 2)을 리턴해줍니다.

# 마찬가지로 486의 각 자리수는 4, 8, 6이므로 sum_digit(486)은 18(4 + 8 + 6)을 리턴해줍니다.

# for문을 사용하여, sum_digit(1)부터 sum_digit(1000)까지의 합을 구해보세요.

# # 자리수 합 리턴
# def sum_digit(num):
#     # 코드를 입력하세요.

# # sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# # 코드를 입력하세요.
# 13501

def sum_digit(num):
    sum = 0
    # for i in range(len(str(num)):
    #     sum += int(str(num)[i])
    for i in str(num):
        sum += int(i)
    return sum

total = 0
for i in range(1, 1001):
    total += sum_digit(i)

print(total)

#해설

# 먼저 sum_digit 함수를 써봅시다.

# 일단 각 자리수를 편하게 쓸 수 있도록 num을 문자열로 형 변환 시킵니다. 그리고 자리수의 합을 저장할 변수 sum을 정의합니다.

# # 자리수 합 리턴
# def sum_digit(num):
#     str_num = str(num)
#     sum = 0
# 문자열을 for문에서 쓸 수 있다는 점을 살려서 sum에 각 자리수를 더합니다. digit을 다시 정수로 형 변환 시켜야한다는 것도 잊지말아야죠. 다 더하고 나서 sum을 리턴해주면 sum_digit 함수는 완성됩니다.

# # 자리수 합 리턴
# def sum_digit(num):
#     str_num = str(num)
#     sum = 0

#     # 각 자리수를 sum_digit에 추가
#     for digit in str_num:
#         sum = sum + int(digit)
#     return sum
# 잘 썼는지 확인 겸 테스트도 몇개 해보고요.

# print(sum_digit(10))
# print(sum_digit(425))
# print(sum_digit(9))
# 1
# 11
# 9
# 이제 total이라는 변수를 만들고, sum_digit(1)부터 sum_digit(1000)까지의 결과값을 모두 total에 추가해주면 끝납니다.

# # 자리수 합 리턴
# def sum_digit(num):
#     str_num = str(num)
#     sum = 0

#     # 각 자리수를 sum_digit에 추가
#     for digit in str_num:
#         sum = sum + int(digit)
#     return sum

# # sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
# total = 0
# for i in range(1, 1001):
#     total = total + sum_digit(i)
# print(total)
