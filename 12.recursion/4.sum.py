# 숫자 합
# n번째 삼각수(triangle number)는 자연수 1부터 n까지의 합입니다. 파라미터로 정수값 n을 받고 n번째 삼각수를 리턴해주는 재귀 함수 triangle_number를 쓰세요. n은 1 이상의 자연수라고 가정합시다.

# 함수 안에 반복문은 쓰면 안됩니다!

# # 1부터 n까지의 합을 리턴
# def triangle_number(n):
#     # 코드를 입력하세요

# # 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
# for i in range(1, 11):
#     print(triangle_number(i))
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55

# 1부터 n까지의 합을 리턴
def triangle_number(n):
    if n == 1:        
        return n
    return n + triangle_number(n - 1)
    

# 테스트: triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))


# 해설
# 뭔가 새로운 문제를 푼다고 생각할 수 있는데 사실 이 문제는 팩토리얼 문제랑 거의 똑같다고 보시면 됩니다.

# 팩토리얼을 재귀적으로 계산하는 함수입니다:

# def factorial(n):
#     if n == 0:
#         return 1
#     return factorial(n - 1) * n
# 여기서 조금만 바꾸면 됩니다:

# def triangle_number(n):
#     if n == 1:
#         return 1
#     return triangle_number(n - 1) + n