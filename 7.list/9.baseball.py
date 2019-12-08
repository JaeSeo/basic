# 숫자 야구
# 숫자 맞추기 게임에 이어, 숫자 야구 게임을 만들려고 합니다. 룰은 다음과 같습니다.

# 컴퓨터는 0과 9 사이의 서로 다른 세 숫자를 임의의 순서로 뽑습니다. 사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추려고 합니다.

# 컴퓨터는 사용자가 입력한 세 숫자에 대해서, 아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려줍니다.

# 숫자의 값과 위치가 모두 일치하면 S입니다.
# 숫자의 값은 일치하지만 위치가 틀렸으면 B입니다.
# 예를 들어 컴퓨터가 1, 2, 3을 생성하였는데, 사용자가 1, 3, 5를 입력하면, 1S(1의 값과 위치가 일치) 1B(3의 값만 일치)입니다.
# 기회는 무제한입니다. 하지만 몇번의 시도 끝에 맞췄는지 기록됩니다.

# 3S(세 숫자의 값과 위치를 모두 맞춘 경우)일 때 게임이 끝납니다.

# 진행 방식

# "0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다."가 출력됩니다.

# "세 수를 하나씩 차례대로 입력하세요."가 출력됩니다.

# "1번째 수를 입력하세요: "가 출력되고, 사용자로부터 입력을 받습니다. 마찬가지로 "2번째 수를 입력하세요: ", "3번째 수를 입력하세요: "가 출력되고, 사용자로부터 각각 입력을 받습니다. 만약 사용자가 중복되는 수를 입력하거나 범위에 벗어나는 수를 입력할 경우, 사용자로부터 입력을 다시 받습니다.

# 사용자가 올바르게 서로 다른 세 수를 입력한 경우, 규칙에 따라 "*S *B"가 출력됩니다. 만약 3S가 아닌 경우 (2)번줄부터 다시 진행됩니다.

# 사용자가 3S를 달성했을 때, "축하합니다. *번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다."가 출력됩니다.

# 예시는 아래와 같습니다.

# 0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.

# 세 수를 하나씩 차례대로 입력하세요.
# 1번째 수를 입력하세요: 2
# 2번째 수를 입력하세요: 2
# 중복되는 수 입니다. 다시 입력해주세요.
# 2번째 수를 입력하세요: 11
# 범위를 벗어나는 수입니다. 다시 입력해주세요.
# 2번째 수를 입력해주세요: 3
# 3번째 수를 입력하세요: 8
# 1S 1B

# 세 수를 하나씩 차례대로 입력하세요.
# 1번째 수를 입력하세요: 8
# 2번째 수를 입력하세요: 2
# 3번째 수를 입력하세요: 0
# 1S 2B

# 세 수를 하나씩 차례대로 입력하세요.
# 1번째 수를 입력하세요: 2
# 2번째 수를 입력하세요: 8
# 3번째 수를 입력하세요: 0
# 3S 0B

# 축하합니다. 3번만에 세 숫자의 값과 위치를 모두 맞추셨습니다.

from random import randint

quiz = []
ran_number_count = 0

while ran_number_count < 3:
    quiz_num = randint(0, 9)
    while quiz_num in quiz:
        quiz_num = randint(0, 9)
    quiz.append(quiz_num)
    ran_number_count += 1

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

answer = []
order = 1
count = 0

while True:
    print("세 수를 하나씩 차례대로 입력하세요.")
    while len(answer) < 3:
        answer_element = int(input("%d번째 수를 입력하세요: " % (order)))
        if answer_element in answer:
            print("이미 입력된 수 입니다")
            continue
        answer.append(answer_element)
        order += 1
    count += 1

    i = 0
    strike = 0
    ball = 0
    while i < 3:
        if answer[i] == quiz[i]:
            strike += 1
        elif answer[i] in quiz:
            ball += 1
        i += 1

    print("%dS %dB" % (strike, ball))
    if strike == 3:
        break

    answer = []
    order = 1
    strike = 0
    ball = 0

print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % count)

#모범 답안
# from random import randint

# # 번호 뽑기
# def generate_numbers():
#     # 숫자 3개를 보관할 리스트 생성
#     numbers = []

#     # 3개의 요소가 있을때까지 반복
#     while len(numbers) < 3:
#         # 새로 뽑은 수가 numbers에 없을 경우에만 추가
#         new_number = randint(0, 9)
#         if new_number not in numbers:
#             numbers.append(new_number)

#     # 리스트 리턴
#     return numbers

# # 정답 뽑기
# ANSWER = generate_numbers()

# # 변수 초기값 설정
# tries = 0        # 시도 횟수
# strike_count = 0 # 스트라이크 개수
# ball_count = 0   # 볼 개수

# # 번호를 모두 맞출때까지 반복
# while strike_count < 3:
#     # 번호 3개 입력 받기
#     guess = []
#     while len(guess) < 3:
#         # 새로 입력한 수가 guess에 없을 경우에만 추가
#         new_number = int(input("%d번째 수를 입력하세요: " % (len(guess) + 1)))

#         # 범위를 벗어나면 설명 메시지 출력
#         if new_number < 0 or new_number > 9:
#             print("0에서 9까지의 수를 입력해주세요!")
#         # 중복된 수를 입력하면 설명 메시지 출력
#         elif new_number in guess:
#             print("새로운 수를 입력해주세요!")
#         # 타당한 값이면 guess에 추가
#         else:
#             guess.append(new_number)

#     # 스트라이크, 볼 개수 세기
#     strike_count = 0 # 스트라이크 개수
#     ball_count = 0   # 볼 개수
#     i = 0            # 인덱싱 변수

#     while i < 3:
#         if guess[i] == ANSWER[i]:
#             strike_count = strike_count + 1
#         elif guess[i] in ANSWER:
#             ball_count = ball_count + 1
#         i = i + 1

#     print("%dS %dB" % (strike_count, ball_count))

#     # 시도 횟수 추가
#     tries = tries + 1

# # 축하 메시지
# print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (tries))






