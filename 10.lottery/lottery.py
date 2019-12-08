# 로또
# 로또 시뮬레이션 프로그램을 만들어봅시다. lottery.py에 코드를 작성해 주세요.

# 규칙
# 참가자는 한 번 할 때마다 1과 45 사이의 서로 다른 번호 여섯개를 뽑아야합니다. 당첨 번호는 1과 45 사이의 서로 다른 일반 번호 여섯개와 또 다른 보너스 번호 하나입니다. 여기서 당첨 액수는 아래의 규칙에 따라 결정됩니다:

# 내가 뽑은 번호 6개와 일반 번호 6개 모두 일치 (10억원)
# 내가 뽑은 번호 5개와 일반 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만원)
# 내가 뽑은 번호 5개와 일반 번호 5개 일치 (100만원)
# 내가 뽑은 번호 4개와 일반 번호 4개 일치 (5만원)
# 내가 뽑은 번호 3개와 일반 번호 3개 일치 (5천원)
# 과제 설명
# lottery.py는 시뮬레이션을 위한 함수들이 정리되어 있는 모듈입니다. 저희가 제공해주는 lottery_driver.py를 실행하면 lottery 모듈에 있는 함수들을 사용하여 로또 100장 시뮬레이션을 한 후, lottery.html 파일을 만들어줍니다. 웹 브라우저로 이 html 파일을 열면 아래 사진처럼 예쁘게 시뮬레이션의 결과가 표시됩니다.

# source: imgur.com

# 일단 lottery.py에 써야하는 함수들을 봅시다.

# generate_numbers 함수는 무작위로 1과 45 사이의 서로 다른 숫자 여섯개를 뽑아서 오름차순으로 정렬되어 있는 리스트를 리턴시켜줍니다. 이 함수는 참가자의 번호 여섯개를 뽑는데에도 쓰이고, 보너스를 제외한 당첨 번호 여섯개를 뽑는데에도 쓰입니다.

# draw_winning_numbers 함수는 앞서 얘기한 것처럼 generate_numbers 함수를 이용해 정렬되어 있는 당첨 번호 여섯개에다가 맨 마지막에 보너스를 포함시킨 리스트를 리턴시켜줍니다. 일곱개의 번호는 서로 달라야하고, 첫 여섯개만 정렬되어 있으면 됩니다.

# count_matching_numbers 함수는 파라미터로 리스트 list1와 리스트 list2를 받고, 두 리스트 사이에 겹치는 번호 개수를 리턴시켜줍니다. 만약에 list1이 [2, 7, 11, 14, 25, 40]이고 list2가 [2, 11, 13, 14, 30, 35]면 정수 3을 리턴하고, list1이 [2, 7, 11, 14, 25, 40]이고 list2가 [14]면 정수 1을 리턴시켜줍니다.

# 마지막으로 check 함수는 파라미터로 참가자의 번호 여섯개가 있는 리스트 numbers와 당첨 일반 번호 여섯개와 보너스 한개가 있는 리스트 winning_numbers를 받고, 규칙에 따라 당첨 금액을 리턴시켜줍니다. 만약 번호 4개가 일치한다면 정수 50000을 리턴시켜줘야 하는 것이죠.

# from random import randint

# # 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
# def generate_numbers():
#     # 코드를 입력하세요

# # 보너스까지 포함해 7개 숫자 뽑기
# # 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# # 예: [1, 7, 13, 23, 31, 41, 15]
# def draw_winning_numbers():
#     # 코드를 입력하세요

# # 두 리스트에서 중복되는 숫자가 몇개인지 구하기
# def count_matching_numbers(list1, list2):
#     # 코드를 입력하세요

# # 로또 등수 확인하기
# def check(numbers, winning_numbers):
#     # 코드를 입력하세요
# 설명에 따라 위의 lottery.py를 완성시키고, lottery_driver.py를 실행시키세요. 그렇게 생성된 lottery.html을 웹 브라우저로 열면 멋있게 결과가 나올겁니다!

# <주의> 함수 안에서 global 변수를 생성하거나 이용하면 안 됩니다. 즉 함수 밖에 변수를 생성하지 마시길 바랍니다.

# <주의> 네 함수 모두 특정한 값을 리턴해야 하며, draw_winning_numbers 함수 내에서는 generate_numbers의 리턴값을, check 함수 내에서는 count_matching_numbers 함수의 리턴값을 사용해주세요.

# <주의> count_matching_numbers 함수는 임의의 길이의 두 리스트가 공통으로 갖고 있는 원소의 개수를 구해주어야 합니다. 즉 count_matching_numbers([1, 4, 7], [1, 3, 5, 6]) 등 파라미터로 넘겨진 리스트의 길이가 달라지더라도, 공통 원소의 개수를 올바르게 계산해야 합니다.

# <주의> check 함수는 "1등", "2등"과 같은 문자열이 아닌, 1000000000, 50000000과 같은 정수형 값을 리턴해야 합니다.

from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    num_list = []

    while len(num_list) < 6:
        random_num = randint(1, 45)
        # while random_num in num_list:
        #     random_num = randint(1, 45)
        # num_list.append(random_num)
        # 모범 답안이 더 효율적이어서 아래와 같이 수정.
        if random_num not in num_list:
            num_list.append(random_num)

    # num_list.sort()
    return sorted(num_list)

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    # num_list = generate_numbers()
    # random_num = randint(1, 45)

    # while random_num in num_list:
    #     random_num = randint(1, 45)

    # num_list.append(random_num)    
    # return num_list
    # 문제 해석을 다르게 하여 아래 모범 답안으로 변경함.
    
    winning_numbers = generate_numbers()
    while len(winning_numbers) < 7:
        new_number = randint(1, 45)
        if new_number not in winning_numbers:
            winning_numbers.append(new_number)

    # 정렬하지 않고 리턴
    return winning_numbers

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    # dup_count = 0
    # for i in list1:
    #     for j in list2:
    #         if i == j:
    #             dup_count += 1

    # return dup_count
    # 아래 모범 답안이 더 효율적이어서 변경함.
    count = 0

    for num in list1:
        # num이 winning_numbers에 있으면 count에 1 추가
        if num in list2:
            count = count + 1

    return count

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    # bonus = winning_numbers[6]
    # real_numbers = list(winning_numbers)
    # del real_numbers[6]
    # dup_count = count_matching_numbers(numbers, real_numbers)
    
    # if dup_count == 6:
    #     return 1000000000
    # elif dup_count == 5 and bonus in numbers:
    #     return 50000000
    # elif dup_count == 5:
    #     return 1000000
    # elif dup_count == 4:
    #     return 50000
    # elif dup_count == 3:
    #     return 5000
    # else:
    #     return 0

    # 아래 모범 답안
    # 번호 당첨 개수 확인
    count = count_matching_numbers(numbers, winning_numbers[:6])

    # 보너스 당첨 확인
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])

    # 상금 확인
    if count == 6:
        return 1000000000
    elif count == 5 and bonus_count == 1:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

