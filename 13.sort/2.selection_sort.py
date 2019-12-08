# 선택 정렬 코드 짜기
# 선택 정렬 알고리즘을 구현해보세요. selection_sort 함수는 파라미터로 리스트 my_list를 받고, my_list 자체를 정렬 시켜줍니다. 즉, selection_sort는 새로운 리스트를 만들어서 리턴해주는 것이 아니고, 파라미터로 넘어온 리스트를 변형시켜주는 것입니다.

# 선택 정렬
def selection_sort(my_list):
    # 코드를 입력하세요.
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] > my_list[j]:
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    
    return my_list

some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)
[1, 2, 3, 4, 6, 11, 12]