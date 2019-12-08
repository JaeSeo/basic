family라는 사전이 있습니다.

family = {}
family['mom'] = 'grace'
family['dad'] = 'chris'
family['son'] = 'young'
family['daughter'] = 'kay'
사전의 key 모두 받아오기
여기서 key들만 모두 받으려면 keys 메소드를 쓰면 됩니다.

print(family.keys())
dict_keys(['son', 'daughter', 'mom', 'dad'])
family에 어떤 key가 있는지 확인하려면 이렇게 하면 됩니다:

print('son' in family.keys())
print('uncle' in family.keys())
True
False
그리고 family의 key들을 리스트로 쓰고 싶으면 list 함수로 형 변환을 하면 됩니다.

family_keys = list(family.keys())
print(family_keys)
print(type(family_keys))
['dad', 'daughter', 'mom', 'son']
<class 'list'>
사전의 value 모두 받아오기
value들을 모두 받기 위해서 values 메소드를 쓰면 됩니다.

print(family.values())
dict_values(['young', 'chris', 'kay', 'grace'])
family에 어떤 value가 있는지 확인하려면 이렇게 하면 됩니다:

print('grace' in family.values())
print('yoonsoo' in family.values())
True
False
그리고 family의 value들을 리스트로 쓰고 싶으면 list 함수로 형 변환을 하면 됩니다.

family_values = list(family.values())
print(family_values)
print(type(family_values))
['young', 'chris', 'kay', 'grace']
<class 'list'>