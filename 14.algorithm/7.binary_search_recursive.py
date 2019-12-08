# 이진 탐색 - 재귀
# '이진 탐색(Binary Search)' 알고리즘의 개념은 앞에서 설명되어 있고, 반복문을 사용하여 문제를 해결하셨을 것입니다. 이번에는 재귀(recursion)를 사용하여 문제를 해결해보세요!

# 템플릿에 있는 함수 정의를 보시면 optional parameter를 사용하는데요. 이 내용이 기억 안 나시면 '추상화' 섹션의 '추상화 꿀팁' 노트를 보시면 됩니다!

# end_index의 기본값을 None으로 설정한 후, 함수 내에서 len(some_list) - 1로 바꾼 이유가 궁금하실 것입니다. 파라미터를 받을 때 파이썬은 some_list의 존재를 모르기 때문에, 정의를 이렇게:

# def binary_search(element, some_list, start_index = 0, end_index = len(some_list) - 1):
# 쓰면 이런 오류 메시지가 나옵니다:

# NameError: name 'some_list' is not defined
# 이 때문에 먼저 None으로 설정한 후, 함수 안에서 end_index의 값이 특별히 설정되지 않았을 경우에는 end_index를 len(some_list) - 1로 바꾸어주는 것입니다.

# 반드시 재귀(recursion)의 개념을 사용하셔야 합니다. 이진 탐색 개념이 꽤 어려우니, 천천히 고민해보시기 바랍니다!

# 평소 재귀 문제를 풀 때처럼 Base Case와 Recursive Case를 생각하시는 것이 핵심입니다!

# 템플릿 (Template)
# def binary_search(element, some_list, start_index = 0, end_index = None):
#     if end_index == None:
#         end_index = len(some_list) - 1

#     # 코드를 작성하세요.

# print(binary_search(2, [2, 3, 5, 7, 11]))
# print(binary_search(0, [2, 3, 5, 7, 11]))
# print(binary_search(5, [2, 3, 5, 7, 11]))
# print(binary_search(3, [2, 3, 5, 7, 11]))
# print(binary_search(11, [2, 3, 5, 7, 11]))
# 0
# None
# 2
# 1
# 4
# <주의> 'if 원소 in 리스트'의 'in' 키워드 또는 'if 원소 not in 리스트'의 'not in' 키워드는 사용하면 안됩니다. 왜냐하면 'in' 키워드는 탐색 알고리즘 자체의 결과를 불러오기 때문에, 해당 키워드를 사용하지 않고 알고리즘을 직접 구현하셔야 합니다.
def binary_search(element, some_list, start_index = 0, end_index = None):
    if end_index == None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.
    mid = (start_index + end_index) // 2
    # print(mid)
    if start_index > end_index:
        return None

    elif element == some_list[mid]:
        return mid
    elif element < some_list[mid]:
        return binary_search(element, some_list, start_index, mid - 1)
    else:
        return binary_search(element, some_list, mid + 1, end_index)

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))