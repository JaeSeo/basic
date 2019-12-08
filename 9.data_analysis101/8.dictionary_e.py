사전(dictionary)은 순서가 없는 key-value 쌍의 집합입니다.

사전 만들기
비어있는 사전을 만들고 type 함수를 써서 어떤 자료형인지 출력해봅시다.

dict1 = {}
print(type(dict1))
<class 'dict'>
key가 정수인 경우
앞서 만든 dict1에 key-value 쌍을 몇개 추가해봅시다.

dict1[5] = 25
dict1[2] = 4
dict1[3] = 9

print(dict1)
{2: 4, 3: 9, 5: 25}
보시다시피 dict1에는 key가 2고 value가 4인 쌍, key가 3이고 value가 9인 쌍, 그리고 key가 5고 value가 25인 쌍이 생겼습니다.

value를 받아오기 위해서 리스트 인덱싱을 하듯이 key를 대괄호 안에 넣어주면 됩니다.

print(dict1[5])
print(dict1[2])
25
4
그럼 key가 정수형인 사전과 그냥 리스트의 차이점은 뭘까요? 리스트는 인덱스 0부터 시작하고 순서대로 채워지지만 사전은 순서가 없기때문에 0부터 시작하지 않고 아무 값들을 쓸 수 있습니다.

key가 정수가 아닌 경우
사전이 리스트와 가장 다른 점은 key가 정수뿐만 아니라 아무 자료형이나 될 수 있다는 것입니다.

family = {}
family['mom'] = 'grace'
family['dad'] = 'chris'
family['son'] = 'young'
family['daughter'] = 'kay'
이 경우 family 사전의 key는 문자열입니다. 값을 받아오기 위해서는 그냥 아래처럼 하면 됩니다.

print(family['dad'])
print(family['daughter'])
chris
kay