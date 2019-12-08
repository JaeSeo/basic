먼저 0에서 9까지의 임의의 숫자 3개를 중복되지 않게 뽑는 코드를 작성해봅시다. 우리가 쓸 generate_numbers 함수는 파라미터를 받지 않고, 세개의 숫자를 갖고 있는 리스트를 리턴해야 합니다.

기본적인 틀은 이렇습니다:

# 번호 뽑기
def generate_numbers():
    # 숫자 3개를 보관할 리스트 생성

    # 리스트 채우기

    # 리스트 리턴
숫자 3개를 보관할 리스트 생성
리스트 생성은 쉽죠?

# 번호 뽑기
def generate_numbers():
    # 숫자 3개를 보관할 리스트 생성
    numbers = []
리스트 채우기
이제 이 리스트를 하나씩 채워봅시다.

randint
일단 임의의 값을 추가시켜줘야 한다는 점에서 바로 randint 함수가 생각납니다. 코드 맨 위에 import문을 씁시다.

from random import randint
반복문
리스트에 임의의 숫자 세개를 추가해야 합니다. 그러면 세번 같은 코드를 쓰는 것보다는 반복문을 쓰는 게 낫겠죠? numbers 리스트가 3개의 요소가 있을때까지 반복합시다.

while len(numbers) < 3:
그리고 수행 부분에서 numbers에 임의의 숫자를 추가하면 되는데요. 너무 순진하게 생각한 분들은 수행 부분에 이런 코드를 쓰셨을 수도 있습니다.

while len(numbers) < 3:
    numbers.append(randint(0, 9))
이 코드의 문제는 뭘까요?

이렇게 하면 0에서 9까지의 임의의 숫자 3개가 numbers 리스트에 들어가겠지만, 중복이 있을 수 있습니다. randint(0, 9)가 세번 모두 5가 나오면 numbers는 [5, 5, 5]가 되는 거죠.

이 문제를 해결하기 위해서 새로 뽑은 숫자가 numbers에 없는 경우에만 추가하도록 하겠습니다.

from random import randint

def generate_numbers():
    # 숫자 3개를 보관할 리스트 생성
    numbers = []

    # 3개의 요소가 있을때까지 반복
    while len(numbers) < 3:
        # 새로 뽑은 수가 numbers에 없을 경우에만 추가
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)
만약 numbers가 현재 [4, 6]인데 randint(0, 9)가 6이 나오면 new_number not in numbers는 False가 나오고 if문의 수행 부분은 뛰어 넘게 됩니다. len(numbers)는 아직 2이기 때문에 numbers가 3개의 값을 갖게 될 때까지 반복문은 계속 진행됩니다.

리스트 리턴
이제 그냥 채워진 리스트(numbers)를 리턴해주면 됩니다.

from random import randint

def generate_numbers():
    # 숫자 3개를 보관할 리스트 생성
    numbers = []

    # 3개의 요소가 있을때까지 반복
    while len(numbers) < 3:
        # 새로 뽑은 수가 numbers에 없을 경우에만 추가
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    # 리스트 리턴
    return numbers
테스트
아래의 테스트를 여러번 실행해보세요. 아무리 많이 실행시켜도 중복되는 값을 볼 수 없죠? 중복되는 값이 나오면 뭔가를 잘못 쓰셨습니다... 잘 확인해보세요~

# 테스트
answers = generate_numbers()
print(answers)