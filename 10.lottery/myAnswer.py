from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
def generate_numbers():
    count = 0
    ran_list = []
    
    while count < 6:
        ran_num = randint(1, 45)
        if ran_num not in ran_list:
            ran_list.append(ran_num)
        else:
            continue
        
        count += 1
    ran_list.sort()
    return ran_list

# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    
    count = 1
    while count == 1:
        bonus_num = randint(1, 45)
        if bonus_num in generate_numbers():
            continue
        count += 1
    
    bonus_list = []
    bonus_list.append(bonus_num)
    return generate_numbers() + bonus_list

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    overlap_count = 0
    list2_length = len(list2) #list2 길이 구하기
    for list2_index in range(list2_length): #list2 인덱스 활용하여 list1과 비교
        if list2[list2_index] in list1:
            overlap_count += 1
        
    return overlap_count

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    overlap_count = 0

    for numbers_index in range(6):
        if numbers[numbers_index] in winning_numbers:
            overlap_count += 1
    
    if overlap_count == 6 and winning_numbers[6] not in numbers:
        return 1000000000
        
    elif overlap_count == 5 and winning_numbers[6] in numbers:
        return 50000000
        
    elif overlap_count == 5 and winning_numbers[6] not in numbers:
        return 1000000

    elif overlap_count == 4 and winning_numbers[6] not in numbers:
        return 50000
        
    elif overlap_count == 3 and winning_numbers[6] not in numbers:
        return 5000        

# from random import randint

# # 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기
# def generate_numbers():
#     num_list = []
#     i = 0
#     while i < 6:
#         random_num = randint(1, 45)
#         while random_num in num_list:
#             random_num = randint(1, 45)
#         num_list.append(random_num)
#         i += 1
    
#     num_list.sort()
#     return num_list

# # 보너스까지 포함해 7개 숫자 뽑기
# # 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# # 예: [1, 7, 13, 23, 31, 41, 15]
# def draw_winning_numbers():
#     num_list = generate_numbers()
#     random_num = randint(1, 45)

#     while random_num in num_list:
#         random_num = randint(1, 45)

#     num_list.append(random_num)    
#     return num_list

# # 두 리스트에서 중복되는 숫자가 몇개인지 구하기
# def count_matching_numbers(list1, list2):
#     dup_count = 0
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 dup_count += 1

#     return dup_count

# # 로또 등수 확인하기
# def check(numbers, winning_numbers):
#     bonus = winning_numbers[6]
#     real_numbers = list(winning_numbers)
#     del real_numbers[6]
#     dup_count = count_matching_numbers(numbers, real_numbers)
    
#     if dup_count == 6:
#         return 1000000000
#     elif dup_count == 5 and bonus in numbers:
#         return 50000000
#     elif dup_count == 5:
#         return 1000000
#     elif dup_count == 4:
#         return 50000
#     elif dup_count == 3:
#         return 5000
#     else:
#         return 0