# 선형 탐색
# '선형 탐색(Linear Search)' 알고리즘을 사용해서 어떤 원소가 리스트 안에 포함되어 있는지 확인하려고 합니다. 선형 탐색이란, 리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행하는 알고리즘입니다.

# 파라미터로 탐색할 값 element와 리스트 some_list를 받는 함수 linear_search를 작성하세요. 0번 인덱스부터 순서대로 하나씩 확인해서 만약 element를 some_list에서 발견할 시 그 위치(인덱스)를 리턴해주면 됩니다. element가 some_list에 존재하지 않는 값이면 None을 리턴해주세요.

# 템플릿 (Template)
# def linear_search(element, some_list):
#     # 코드를 작성하세요.

# print(linear_search(2, [2, 3, 5, 7, 11]))
# print(linear_search(0, [2, 3, 5, 7, 11]))
# print(linear_search(5, [2, 3, 5, 7, 11]))
# print(linear_search(3, [2, 3, 5, 7, 11]))
# print(linear_search(11, [2, 3, 5, 7, 11]))
# 0
# None
# 2
# 1
# 4
# <주의> 'if 원소 in 리스트'의 'in' 키워드 또는 'if 원소 not in 리스트'의 'not in' 키워드는 사용하면 안됩니다. 왜냐하면 'in' 키워드는 탐색 알고리즘 자체의 결과를 불러오기 때문에, 해당 키워드를 사용하지 않고 알고리즘을 직접 구현하셔야 합니다.

def linear_search(element, some_list):
    # 코드를 작성하세요.
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
    return None

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))