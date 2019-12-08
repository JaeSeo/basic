# 변수는 정보를 저장하고 쓸 수 있게 해주는 '이름표'같은 개념입니다. 변수는 왜 추상화의 한 종류일까요? 한 번 변수를 정의하고 나서 이후에 그것을 사용할 때, 변수의 이름만 알면 되고 그 값은 알 필요가 없기 때문이죠.

# 우사인 볼트의 평균 속도 = 10.438413361 m/s

# 1초에 달릴 수 있는 거리 (m/s)
speed = 10.438413361

print(speed * 60)   # 1분(60초)동안 간 거리
print(speed * 120)  # 2분(120초)동안 간 거리
print(speed * 180)  # 3분(180초)동안 간 거리
626.3048016600001
1252.6096033200001
1878.91440498
# 변수의 기능을 제대로 알기 위하여, 지정 연산자가 하는 역할을 살펴보겠습니다.

# 지정 연산자 (Assignment Operator)
x = 2 + 1
print(x)

x = x + 1
print(x)
3
4
# 수학에서 =은, "수학적으로 같은 값을 지닌다"는 뜻입니다. 하지만 파이썬에서는 그렇지 않습니다.

# 이 기호는 지정 연산자(Assignment Operator)로서, 오른쪽에 있는 값을 왼쪽에 있는 변수에 '지정'해주는 역할을 하죠.

# 예를 들어 첫째 줄인 x = 2 + 1에서는 오른쪽에 있는 2 + 1 즉 3이, 왼쪽에 있는 변수인 x에 지정됩니다. 이에 둘째줄의 print(x)가 실행되었을 때, x가 저장하고 있는 3이 출력됩니다.

# 이제 살짝 헷갈리는 부분입니다. 셋째 줄의 x = x + 1이라는 표현은 수학적으로 성립하지 않죠? 그러나 파이썬에서는 아무런 문제가 없습니다. 오른쪽의 값이 우선 계산된 뒤에, 왼쪽의 변수에 지정되기 때문입니다. x가 현재 3으로 지정되어 있기 때문에, x = x + 1의 오른쪽 값은 4가 됩니다. 4라는 값은 왼쪽 변수인 x에 지정됩니다. 따라서 네번째 줄의 print(x)가 실행되었을 때, x가 저장하고 있는 4가 출력됩니다.