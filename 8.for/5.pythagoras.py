# 피타고라스 수
# 피타고라스 수란 피타고라스의 정리(a^2 + b^2 = c^2)를 만족하는 세 자연수 쌍 (a, b, c) 입니다.

# 예를 들어, 3^2 + 4^2 = 5^2이기 때문에 (3, 4, 5)는 피타고라스 수입니다.

# a < b < c일때, a + b + c = 1000을 만족하는 피타고라스 수 (a, b, c)는 단 하나입니다. 이 경우, a * b * c는 얼마인가요?

# 31875000


# 335 + 334 + 331
# for c in range(3, 998):
#     for b in range(2, c):
#         for a in range(b):
#             if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
#                 print(a * b * c)
#                 print(c)
#                 break

for a in range(333):
    for b in range(a + 1, 500):
        c = 1000 - b - a
        if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
            print(a * b * c)
            print(c)
            break

            