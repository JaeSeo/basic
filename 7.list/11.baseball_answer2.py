현재까지 쓴 코드입니다:

from random import randint

# 번호 뽑기
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
초기값 설정
이제 이어서 실제로 게임을 하는 부분을 만들어볼텐데요. 먼저 처음에 필요한 상수와 변수들을 정의합시다.

정답 번호 세개는 우리가 써놓은 generate_numbers 함수를 호출해서 한번 정하면 바뀌지 않기 때문에 상수로 쓰겠습니다. 그리고 시도 횟수, 스트라이크 개수, 볼 개수는 모두 0으로 시작하겠습니다.

# 정답 뽑기
ANSWER = generate_numbers()

# 변수 초기값 설정
tries = 0        # 시도 횟수
strike_count = 0 # 스트라이크 개수
ball_count = 0   # 볼 개수
반복문
사실상 게임을 진행시키는 반복문을 써야 합니다. 먼저 조건 부분부터 생각해 봅시다. '숫자 야구' 게임은 시도 횟수와는 상관 없이, 번호를 모두 맞추어 스트라이크 3개가 나올때까지 끝이 나면 안 됩니다. 따라서 반복문은 이렇게 쓸 수 있습니다:

# 번호를 모두 맞출때까지 반복
while strike_count < 3:
그리고 반복문의 수행 부분의 틀을 짜보면 대충 이렇습니다:

# 번호를 모두 맞출때까지 반복
while strike_count < 3:
    # 번호 3개 입력 받기

    # 스트라이크, 볼 개수 세기

    # 시도 횟수 추가
한 부분씩 살펴봅시다.

번호 3개 입력 받기
사용자로부터 콘솔에 입력값 세개를 받는 코드를 써야합니다. 이 부분은 이전에 우리가 쓴 generate_numbers 함수와 굉장히 비슷합니다. 차이점은 새로운 수가 randint에 의해 결정되는 것이 아니고 input에 의해 결정된다는 것입니다.

또한 사용자가 규칙에 벗어나는 값을 입력할 수도 있기 때문에 경우에 따라 오류 메시지를 출력해야 합니다.

# 번호 3개 입력 받기
guess = []
while len(guess) < 3:
    # 새로 입력한 수가 guess에 없을 경우에만 추가
    new_number = int(input("%d번째 수를 입력하세요: " % (len(guess) + 1)))

    # 범위를 벗어나면 설명 메시지 출력
    if new_number < 0 or new_number > 9:
        print("0에서 9까지의 수를 입력해주세요!")
    # 중복된 수를 입력하면 설명 메시지 출력
    elif new_number in guess:
        print("새로운 수를 입력해주세요!")
    # 타당한 값이면 guess에 추가
    else:
        guess.append(new_number)
스트라이크, 볼 개수 세기
이제 ANSWER 리스트와 guess 리스트를 비교해 스트라이크, 볼 개수를 세야 합니다.

일단 필요한 변수들의 초기값을 설정합시다. 스트라이크와 볼을 세기 전에 항상 이렇게 초기화를 시켜서 모든 값이 0부터 시작해야 한다는 점을 주의해주세요.

# 스트라이크, 볼 개수 세기
strike_count = 0 # 스트라이크 개수
ball_count = 0   # 볼 개수
i = 0            # 인덱싱 변수
스트라이크 개수를 세는 것은 쉽습니다. guess[0]과 ANSWER[0]이 같으면 strike_count에 1을 추가하고, guess[1]과 ANSWER[1]이 같으면 strike_count에 1을 추가하고, 또 guess[2]와 ANSWER[2]가 같으면 strike_count에 1을 추가하면 됩니다.

# 스트라이크, 볼 개수 세기
strike_count = 0 # 스트라이크 개수
ball_count = 0   # 볼 개수
i = 0            # 인덱싱 변수

while i < 3:
    if guess[i] == ANSWER[i]:
        strike_count = strike_count + 1
    i = i + 1
조금만 머리를 굴려보면 볼 개수를 세는 것도 어렵지 않습니다. guess[i]가 ANSWER[i]와 같지는 않지만 (즉, if문의 조건 부분은 False지만), guess[i]가 ANSWER 리스트 안에 존재하면 (guess[i] in ANSWER이 True면) ball_count에 1을 추가하면 됩니다.

# 스트라이크, 볼 개수 세기
strike_count = 0 # 스트라이크 개수
ball_count = 0   # 볼 개수
i = 0            # 인덱싱 변수

while i < 3:
    if guess[i] == ANSWER[i]:
        strike_count = strike_count + 1
    elif guess[i] in ANSWER:
        ball_count = ball_count + 1
    i = i + 1
이제 사용자에게 스트라이크와 볼 개수를 알려주면 됩니다.

print("%dS %dB" % (strike_count, ball_count))
시도 횟수 추가
시도 횟수 추가는 쉽죠?

# 시도 횟수 추가
tries = tries + 1
모범 답안
마지막에 "축하합니다" 메시지까지 포함한 모범 답안입니다:
#############################

from random import randint

# 번호 뽑기
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

# 정답 뽑기
ANSWER = generate_numbers()

# 변수 초기값 설정
tries = 0        # 시도 횟수
strike_count = 0 # 스트라이크 개수
ball_count = 0   # 볼 개수

# 번호를 모두 맞출때까지 반복
while strike_count < 3:
    # 번호 3개 입력 받기
    guess = []
    while len(guess) < 3:
        # 새로 입력한 수가 guess에 없을 경우에만 추가
        new_number = int(input("%d번째 수를 입력하세요: " % (len(guess) + 1)))

        # 범위를 벗어나면 설명 메시지 출력
        if new_number < 0 or new_number > 9:
            print("0에서 9까지의 수를 입력해주세요!")
        # 중복된 수를 입력하면 설명 메시지 출력
        elif new_number in guess:
            print("새로운 수를 입력해주세요!")
        # 타당한 값이면 guess에 추가
        else:
            guess.append(new_number)

    # 스트라이크, 볼 개수 세기
    strike_count = 0 # 스트라이크 개수
    ball_count = 0   # 볼 개수
    i = 0            # 인덱싱 변수

    while i < 3:
        if guess[i] == ANSWER[i]:
            strike_count = strike_count + 1
        elif guess[i] in ANSWER:
            ball_count = ball_count + 1
        i = i + 1

    print("%dS %dB" % (strike_count, ball_count))

    # 시도 횟수 추가
    tries = tries + 1

# 축하 메시지
print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (tries))