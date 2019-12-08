# 숫자 맞추기 게임
# 1과 20 사이의 숫자를 맞추는 게임을 만드려고 합니다.

# 앞서 배운 randint 함수와, input 함수의 개념을 활용하여 직접 프로그램을 만들어보세요.

# 진행 방식

# 프로그램을 실행하면 "기회가 *번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: "가 출력됩니다. 총 4번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회 횟수가 줄어듭니다.

# 정답을 맞추면, "축하합니다. *번만에 숫자를 맞추셨습니다."가 출력되고 프로그램은 종료됩니다.

# 사용자가 입력한 수가 정답보다 작을 경우 "Up"이 출력되고, 입력한 수가 정답보다 클 경우 "Down"이 출력됩니다.

# 정답이 틀렸으면 (1)번부터 다시 진행합니다. 만약 4번의 기회를 모두 사용했는데도 답을 맞추지 못했으면, "아쉽습니다. 정답은 *였습니다."가 출력되고 프로그램은 종료됩니다.

# 기회가 4번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: 10
# Up
# 기회가 3번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: 15
# Up
# 기회가 2번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: 17
# 축하합니다. 3번만에 숫자를 맞추셨습니다.
# 기회가 4번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: 19
# Down
# 기회가 3번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: 14
# Down
# 기회가 2번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: 6
# Up
# 기회가 1번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: 10
# UP
# 아쉽습니다. 정답은 12였습니다.

# 내 답안
# from random import randint

# answer = randint(1, 20)

# chance = 4
# count = 1
# while chance != 0:
#     answer_input = int(input("정답을 입력하세요: "))
#     if answer > answer_input:
#         print('Up')
#         chance -= 1
#         count += 1

#         if count == 0:
#             print('아쉽습니다. 정답은 %d였습니다' % count)

#     elif answer < answer_input:
#         print('Down')
#         chance -= 1
#         count += 1

#         if count == 0:
#             print('아쉽습니다. 정답은 %d였습니다' % count)        

#     else:
#         print('축하합니다 %d번만에 맞추셨습니다' % count)
#         break

# 해설
from random import randint

# 상수
NUM_TRIES = 4
ANSWER = randint(1, 20)

# 변수
tries = 0
guess = 0

# 시도
while tries < NUM_TRIES and guess != ANSWER:
    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (NUM_TRIES - tries)))
    tries = tries + 1

    if guess < ANSWER:
        print("Up")
    elif guess > ANSWER:
        print("Down")

if guess == ANSWER:
    print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (tries))
else:
    print("아쉽습니다. 정답은 %d였습니다" % (ANSWER))
    