이름 규칙
모든 변수와 함수 이름은 소문자로 써주시고, 여러 단어일 경우 _로 나눠주세요.

# bad
someVariableName = 1
SomeVariableName = 1

def someFunctionName():
    print("Hello")

# good
some_variable_name = 1

def some_function_name():
    print("Hello")
모든 상수 이름은 대문자로 써주시고, 여러 단어일 경우 _로 나눠주세요.

# bad
someConstant = 3.14
SomeConstant = 3.14
some_constant = 3.14

# good
SOME_CONSTANT = 3.14
의미있는 변수/함수 이름
# bad
a = 2
b = 3.14
print(b * a * a)

# good
radius = 2
pi = 3.14
print(pi * radius * radius)
# bad
def do_something():
    print("Hello, world!")

# good
def say_hello():
    print("Hello, world!")
화이트 스페이스
적당한 화이트 스페이스는 코드를 읽기 편하게 합니다.

# bad
print(1+1)

# bad
print(1  +   1)

# good
print(1 + 1)
# bad
def print_product(a,b,c):
    print(a * b * c)

# bad
def print_product(a , b , c):
    print(a * b * c)

# good
def print_product(a, b, c):
    print(a * b * c)
글 쓸때 문단을 나누듯이 프로그램을 짤때도 엔터키를 써서 적당히 나눠주세요.

# bad
PI = 3.14
radius = 4
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)
radius = 8
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)

# good
PI = 3.14

radius = 4
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)

radius = 8
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)
적당한 추상화
# bad
PI = 3.14

radius = 4
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)

radius = 8
print(2 * PI * radius)
print(PI * radius * radius)
print(4 / 3 * PI * radius * radius * radius)

# good
PI = 3.14

def calculate_circumference(r):
    return 2 * PI * r

def calculate_area(r):
    return PI * r * r

def calculate_volume(r):
    return 4 / 3 * PI * r * r * r

radius = 4
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))

radius = 8
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))
적당한 코멘트
# bad (설명 부족)
PI = 3.14

def calculate_circumference(r):
    return 2 * PI * r

def calculate_area(r):
    return PI * r * r

def calculate_volume(r):
    return 4 / 3 * PI * r * r * r

radius = 4
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))

radius = 8
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))

# bad (설명 과다)
PI = 3.14   # 원주율 

# 반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    # 둘레는 2 * 파이 * 반지름
    return 2 * PI * r

# 반지름이 r인 원의 넓이 계산
def calculate_area(r):
    # 넓이는 파이 * 반지름 * 반지름
    return PI * r * r

# 반지름이 r인 구의 부피 계산
def calculate_volume(r):
    # 부피는 4 / 3 * 파이 * 반지름 * 반지름 * 반지름
    return 4 / 3 * PI * r * r * r

# 반지름이 4인 경우
radius = 4    # 반지름
print(calculate_circumference(radius))  # 반지름 4인 경우 둘레
print(calculate_area(radius))           # 반지름 4인 경우 넓이
print(calculate_volume(radius))         # 반지름 4인 경우 부피

# 반지름이 8인 경우
radius = 8    # 반지름
print(calculate_circumference(radius))  # 반지름 8인 경우 둘레
print(calculate_area(radius))           # 반지름 8인 경우 넓이
print(calculate_volume(radius))         # 반지름 8인 경우 부피

# good
PI = 3.14   # 원주율

# 반지름이 r인 원의 둘레 계산
def calculate_circumference(r):
    return 2 * PI * r

# 반지름이 r인 원의 넓이 계산
def calculate_area(r):
    return PI * r * r

# 반지름이 r인 구의 부피 계산
def calculate_volume(r):
    return 4 / 3 * PI * r * r * r

# 반지름이 4인 경우
radius = 4    # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))

# 반지름이 8인 경우
radius = 8    # 반지름
print(calculate_circumference(radius))
print(calculate_area(radius))
print(calculate_volume(radius))
적당한 줄 길이
한 줄에 80자를 넘기지 맙시다.

# bad
print("오늘은 " + str(2016) + "년 " + str(4) + "월 " + str(15) + "일 " + "금" + "요일입니다.")

# good
print("오늘은 " + str(2016) + "년 " + str(4) + "월 " + str(15) +
    "일 " + "금" + "요일입니다.")