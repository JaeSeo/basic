Base Case
리스트가 정렬되어 있으므로, 재귀 함수를 통해 함수가 호출되는 과정에서 start_index가 end_index보다 클 경우에는 원소가 포함되어있지 않다는 이야기입니다. 따라서 이 경우에 None을 리턴해주면 됩니다.

Recursive Case
element가 some_list[midpoint]와 일치한다면, 그 인덱스를 리턴하고 종료합니다.
element가 some_list[midpoint]보다 작다면, 탐색 범위의 후반부는 제외시켜도 됩니다. 따라서 end_index를 midpoint - 1로 업데이트해줍니다. 그 후 binary_search(element, some_list, start_index, end_index)를 리턴해주어 재귀적으로 문제를 해결합니다.
element가 some_list[midpoint]보다 크다면, 탐색 범위의 전반부는 제외시켜도 됩니다. 따라서 start_index를 midpoint + 1로 업데이트해줍니다. 그 후 binary_search(element, some_list, start_index, end_index)를 리턴해주어 재귀적으로 문제를 해결합니다.
모범 답안
def binary_search(element, some_list, start_index = 0, end_index = None):
    if end_index == None:
        end_index = len(some_list) - 1

    if start_index > end_index:
        return None

    midpoint = (start_index + end_index) // 2

    if element == some_list[midpoint]:
        return midpoint
    elif element < some_list[midpoint]:
        end_index = midpoint - 1
        return binary_search(element, some_list, start_index, end_index)
    else:
        start_index = midpoint + 1
        return binary_search(element, some_list, start_index, end_index)


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
0
None
2
1
4