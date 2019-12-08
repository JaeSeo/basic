# 선택 정렬
def selection_sort(my_list):
    # 코드를 입력하세요.

# 테스트
some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)
selection_sort 함수는 파라미터로 리스트 my_list를 받습니다.

가장 작은 값을 찾아서 my_list의 0번 인덱스에 넣어주고, 그 다음으로 작은 값을 찾아서 1번 인덱스에 넣어주고, 그 다음으로 작은 값을 찾아서 2번 인덱스에 넣어주고... 이런식으로 len(my_list) - 1번 인덱스까지 반복하면 선택 정렬이 완료됩니다.

여기서 우리가 각 경우의 최소값을 넣어줄 인덱스를 i라고 부릅시다. i는 0부터 len(my_list) - 1까지 반복되기 때문에 반복문을 이렇게 쓸 수 있습니다:

# 바깥쪽 반복문
for i in range(len(my_list)):
매번 반복문의 수행 부분에 들어갈 때 이 두 가지를 생각하고 있어야 합니다:

my_list[:i](0번 인덱스부터 i - 1번 인덱스까지)는 정렬되어 있다.
my_list[i:len(my_list)](i번 인덱스부터 len(my_list) - 1번 인덱스까지)에서의 최소값을 i번 인덱스에 넣어줘야 한다.
최소값 찾기
my_list[i:len(my_list)]의 최소값을 찾는 코드를 써봅시다. 먼저 현재까지 최소값의 위치를 보관하는 변수를 만들어야 하는데요. 일단은 첫번째 값(i번 인덱스에 있는 값)을 최소값으로 설정합시다.

min_index = i
그리고 i + 1번 인덱스에 있는 값부터 len(my_list) - 1번 인덱스에 있는 값까지 하나씩 보면서 min_index의 값보다 작은 값이 있으면 min_index에 새로운 인덱스를 지정해주면 됩니다.

# 안쪽 반복문
for j in range(i + 1, len(my_list)):
    value = my_list[j]
    if value < my_list[min_index]:
        min_index = j
자리 바꿔주기
'안쪽 반복문'이 끝나면 my_list[i:len(my_list)]의 최소값을 찾았겠죠? 이제 그 최소값을 i 인덱스의 자리에 넣어줘야 합니다. i 인덱스의 값과 min_index 인덱스의 값의 자리를 바꿔줍시다.

# 자리 바꾸기
temp = my_list[i]
my_list[i] = my_list[min_index]
my_list[min_index] = temp
모범 답안
위의 코드를 합치면 selection_sort 함수는 완성됩니다. 테스트를 해봅시다!

# 선택 정렬
def selection_sort(my_list):
    # 바깥쪽 반복문
    for i in range(len(my_list)):
        min_index = i

        # 안쪽 반복문
        for j in range(i + 1, len(my_list)):
            value = my_list[j]
            if value < my_list[min_index]:
                min_index = j

        # 자리 바꾸기
        temp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = temp

# 테스트
some_list = [11, 3, 6, 4, 12, 1, 2]
selection_sort(some_list)
print(some_list)
[1, 2, 3, 4, 6, 11, 12]