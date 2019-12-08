# 불린은 참과 거짓을 표현하는 자료형입니다. 불린 자료형을 만들기 위해, 아래의 조건 연산 부호(conditional operator)들이 자주 쓰입니다. 연산 부호들과 함께 예시를 살펴봅시다.

# 연산자	뜻
# >	초과 (greater than)
# <	미만 (less than)
# >=	이상 (greater than or equal to)
# <=	이하 (less than or equal to)
# ==	같다 (equal to)
# !=	같지 않다 (not equal to)
print(True)
print(False)
print()
print(2 > 1)    # 2는 1 초과이다
print(2 < 1)    # 2는 1 미만이다
print(3 >= 2)   # 3은 2 이상이다
print(3 <= 3)   # 3은 3 이하이다
print(2 == 2)   # 2는 2와 같다
print(2 != 2)   # 2는 2와 같지 않다
True
False

True
False
True
True
True
False
# 아래의 네 가지 규칙을 따르면 더 다양한 방법으로 참과 거짓을 나타낼 수 있습니다.

# 식이 and로 이어진 경우 왼쪽과 오른쪽 모두 True여야만 참이고, 나머지 경우에는 모두 False입니다.
# 식이 or로 이어진 경우 왼쪽과 오른쪽 모두 False여야만 거짓이고, 나머지 경우에는 모두 True입니다.
# not True는 False고 not False는 True입니다.
# 괄호가 포함된 연산은, 괄호 안부터 값을 계산하고 그 후 괄호 밖과 연산합니다.
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print()

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print()

print(not True)
print(not False)
True
False
False
False

True
True
True
False

False
True
# 심화 예시를 살펴봅시다.

x = 3
print(x > 4 or (x < 2 or x != 3))

print((4 < 3 and 12 > 10) or 7 == 7)
print(not 4 < 3)
print(not not True)
False
True
True
True