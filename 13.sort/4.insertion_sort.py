# 삽입 정렬 코드 짜기
# 삽입 정렬 알고리즘을 구현해보세요. insertion_sort 함수는 파라미터로 리스트 my_list를 받고, my_list 자체를 정렬 시켜줍니다. 즉, insertion_sort는 새로운 리스트를 만들어서 리턴해주는 것이 아니고, 파라미터로 넘어온 리스트를 변형시켜주는 것입니다.

# 삽입 정렬
def insertion_sort(my_list):
    # 코드를 입력하세요.
    for i in range(1, len(my_list)):
        value = my_list[i]
        min_index = i
        for j in range(i - 1, -1, -1):
            if my_list[j] > value:
                my_list[j + 1] = my_list[j]
                min_index = j
        
        my_list[min_index] = value

    return my_list

some_list = [11, 3, 6, 4, 12, 1, 2]
insertion_sort(some_list)
print(some_list)
# [1, 2, 3, 4, 6, 11, 12]
# <주의> key값이 들어가야 할 자리를 찾는 삽입 정렬의 개념을 활용해야 합니다.