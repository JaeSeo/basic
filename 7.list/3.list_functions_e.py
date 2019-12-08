len 함수
len 함수는, 리스트 안의 원소 개수를 세주는 역할을 합니다.

alphabet = ["a", "b", "c", "d", "e", "f"]

print("리스트의 길이는: %d" % len(alphabet))
리스트의 길이는: 6
원소 추가하기
insert와 append를 사용하여 리스트에 원소를 추가할 수 있습니다.

numbers = []

# 마지막 위치에 5 추가
numbers.append(5)
print(numbers)

# 마지막 위치에 8 추가
numbers.append(8)
print(numbers)

# 마지막 위치에 10 추가
numbers.append(10)
print(numbers)

# 인덱스 0 자리에 0 추가
numbers.insert(0, 0)
print(numbers)

# 인덱스 3 자리에 12 추가
numbers.insert(3, 12)
print(numbers)
[5]
[5, 8]
[5, 8, 10]
[0, 5, 8, 10]
[0, 5, 8, 12, 10]
원소 빼기
del 함수를 사용함으로써 원하는 리스트의 원소를 삭제할 수 있습니다.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# 인덱스 3에 있는 값 삭제
del numbers[3]
print(numbers)

# 인덱스 4부터 마지막 값까지 삭제
del numbers[4:]
print(numbers)
[1, 2, 3, 5, 6, 7, 8]
[1, 2, 3, 5]
sorted 함수
sorted 함수는 리스트의 원소들을 오름차순으로 정렬한 새로운 리스트를 리턴해줍니다.

sorted 함수를 이용하여 [8, 6, 2, 4, 5, 7, 1, 3]이라는 리스트를 정렬한 후 출력하면, [1, 2, 3, 4, 5, 6, 7, 8]이 나옵니다.

numbers = [8, 6, 2, 4, 5, 7, 1, 3]
numbers = sorted(numbers)

print(numbers)
[1, 2, 3, 4, 5, 6, 7, 8]
리스트 연결하기
리스트들을 +로 연결할 수 있습니다.

alphabet1 = ["a", "b", "c"]
alphabet2 = ["d", "e", "f"]
alphabet = alphabet1 + alphabet2

print(alphabet)
['a', 'b', 'c', 'd', 'e', 'f']