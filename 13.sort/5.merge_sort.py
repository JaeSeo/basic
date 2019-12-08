# 합병 정렬 코드 짜기
# 합병 정렬 알고리즘을 구현해보세요.

# 먼저 merge 함수를 쓰세요. merge는 파라미터로 정렬된 리스트 list1과 list2를 받고, 두 리스트의 요소를 모두 포함한 정렬된 새로운 리스트를 리턴시켜줍니다.

# 그리고 영상에서 본 대로 분할 정복(Divide and Conquer) 방식으로 merge_sort 함수를 써보세요. merge_sort는 파라미터로 리스트 하나를 받고, 정렬된 새로운 리스트를 리턴시켜줍니다.

# # 두 리스트 합치기
# def merge(list1, list2):
#     # 코드를 입력하세요.

# # 합병 정렬
# def merge_sort(my_list):
#     # 코드를 입력하세요.

# some_list = [11, 3, 6, 4, 12, 1, 2]
# sorted_list = merge_sort(some_list)
# print(sorted_list)
# [1, 2, 3, 4, 6, 11, 12]
# <주의> merge_sort 함수에서는 재귀(recursion)의 개념을 활용해야 합니다.

################# 
# 두 리스트 합치기
def merge(list1, list2):
    # 코드를 입력하세요.
    new_list = []
    while len(list1) != 0 and len(list2) != 0:
        if list1[0] > list2[0]:
            new_list.append(list2[0])
            list2 = list2[1:]
        else:
            new_list.append(list1[0])
            list1 = list1[1:]

    if len(list1) == 0 and len(list2) != 0:
        new_list = new_list + list2
    elif len(list1) != 0 and len(list2) == 0:
        new_list = new_list + list1

    return new_list

# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) <= 1:
        return my_list
    else:
        mid = len(my_list) // 2
        left = merge_sort(my_list[:mid])
        right = merge_sort(my_list[mid:])
        return merge(left, right)

some_list = [11, 3, 6, 4, 12, 1, 2]
sorted_list = merge_sort(some_list)
print(sorted_list)