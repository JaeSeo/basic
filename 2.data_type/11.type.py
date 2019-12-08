# 프로그래밍을 하다가 어떤 값이 무슨 자료형인지 기억나지 않을 때가 있습니다. 그럴 때에는 type라는 걸 쓰면 됩니다!

# 각 자료형 별 type 함수 써보기
print(type(1))
print(type(1.0))
print(type("1"))
print(type(2 > 4))
print()

# 헷갈리는 두 자료형 비교
print(type("True"))
print(type(True))
print()

# print 함수의 type 확인
print(type(print))
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>

# <class 'str'>
# <class 'bool'>

# <class 'builtin_function_or_method'>
# 1은 정수형이기 때문에, <class 'int'>가 나옵니다.
# 1.0은 소수형이기 때문에, <class 'float'>가 나옵니다. 여기서 파이썬이 1과 1.0을 명확하게 구분하고 있다는 걸 알 수 있습니다.
# "1"은 문자열이기 때문에, <class 'str'>이 나옵니다. 여기서도 파이썬이 1과 "1"을 명확하게 구분하고 있다는 걸 알 수 있습니다.
# 2 > 4의 결과는 불린값 False입니다. 따라서 <class 'bool'>이 나옵니다.
# "True"는 걸핏보면 불린인 것 같지만 쌍따옴표에 둘러싸여 있기 때문에, 일반적인 문자열입니다. 따라서 <class 'str'>이 나옵니다.
# True는 불린값이기 때문에, <class 'bool'>이 나옵니다.
# print는 파이썬에 기본적으로 있는 내장 함수이므로, <class 'builtin_function_or_method'>이 나옵니다. 함수에 대해서는 다음 섹션에서 더 자세히 살펴볼 것입니다.