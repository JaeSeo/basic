모듈(module)이란 변수, 함수, 클래스 등을 모아 놓은 파일입니다. 모듈에 정보를 한번만 정의해두면 여러 프로그램에서 쉽게 가져다 쓸 수 있습니다.

calculator.py라는 모듈을 만들고, 다른 파일에서 이 calculator 모듈을 가져다 써봅시다.

# calculator.py
# calculator 모듈

# 합
def sum(x, y):
    return x + y

# 차이
def difference(x, y):
    return x - y
  
# 곱
def product(x, y):
    return x * y

# 제곱
def square(x):
    return x * x
test.py라는 파일을 만들어 calculator 모듈을 사용해봅시다. 모듈 안에 정의된 변수, 함수, 클래스를 호출하는 방식은 다음과 같습니다.

from 모듈 파일의 이름 import 불러올 변수/함수/클래스
예를 들어 calculator.py에 정의된 sum이라는 함수를 호출해봅시다.

# test.py

# calculator.py에서 sum 함수 불러오기
from calculator import sum

print(sum(3, 5))
8
만약 모듈에 정의된 모든 변수, 함수, 클래스를 호출하려면 어떻게 할까요?

from calculator import sum, difference, product, square
위와 같은 방식으로 호출할 수도 있습니다만, 모듈에서 쓰고 싶은 변수, 함수, 클래스가 100개 이상이라면 그것들을 일일이 입력하는 것은 바보 같은 일이겠죠?

*를 쓰면, 모듈 안에 정의된 모든 변수/함수/클래스를 불러올 수 있습니다.

from calculator import *

print(sum(3, 5))
print(difference(3, 5))
print(product(3, 5))
print(square(3))
8
-2
15
9
그러나 모듈 파일의 일부만 사용하려고 할 때, *를 쓰는 것은 좋지 않은 습관(practice)입니다. 100개의 함수가 정의되어 있는데 4개만 사용하려고 한다면, *를 이용하기보다 하나 하나 직접 호출하는게 낫습니다. 스스로 상황 별로 적절히 잘 판단하여, 하나하나 직접 호출할지, 아니면 모듈에 정의된 모든 것을 호출할지 결정해야 합니다.

randint 함수와 uniform 함수
randint는 두 정수 사이의 어떤 랜덤한 정수(난수)를 리턴시켜주는 함수입니다. randint는 파이썬에 기본적으로 깔려있는 random이라는 모듈에 정의되어 있습니다. 따라서 이 함수를 사용하기 위해서는 random이라는 모듈로부터 불러와야 합니다.

from random import randint
함수를 불러오는 방법에 대해 봤으니, 이제 사용하는 방법에 대해 알아보겠습니다.

# a <= N <= b인, 랜덤한 정수(난수) N의 값을 리턴시켜준다.
randint(a, b)
x에 randint(1, 20)을 지정하고 출력해봅시다. 프로그램을 실행하면 1과 20사이의 랜덤한 정수가 콘솔에 출력됩니다. 다시 실행하면 또 랜덤한 정수가 콘솔에 출력됩니다.

from random import randint

x = randint(1, 20)
print(x)
uniform은 random이라는 모듈 안에 정의되어 있는, 두 수 사이의 랜덤한 소수(난수)를 리턴시켜주는 함수입니다. uniform 함수를 사용하는 방법에 대해 알아보겠습니다.

# a <= N <= b인, 랜덤한 소수(난수) N의 값을 리턴시켜준다.
uniform(a, b)
x에 uniform(0, 1)을 지정하고 출력해봅시다. 아래 프로그램을 실행하면 0과 1사이의 랜덤한 소수가 콘솔에 출력됩니다.

from random import uniform

x = uniform(0, 1)
print(x)