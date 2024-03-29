이전 섹션들에서는 정수, 문자열, 리스트 등 파이썬에 기본적으로 있는 자료형들로 프로그램을 짰습니다. 그런데 페이스북같은 SNS를 만들려면 '유저'는 어떻게 표현해야 할까요? '유저'는 이름, 이메일, 비밀번호, 생년월일, 친구목록 등 구성이 굉장히 복잡합니다. 문자열 하나로도 표현할 수 없고, 리스트로도 표현할 수 없습니다.

파이썬같은 객체 지향 프로그래밍 언어가 이럴 때 유용해집니다. 기존의 자료형들로 표현하기 어려운 것들은 우리가 새로운 자료형을 만들어서 표현할 수 있습니다. SNS를 위해서는 '유저'라는 새로운 자료형을 만들면 되겠죠?

파이썬에서 새로운 자료형을 만들려면 '클래스'라는 것을 써야합니다. 클래스는 어떤 자료형에 대한 설명서라고 생각할 수 있습니다. 한번 직접 '유저'를 표현할 수 있는 자료형을 만들어봅시다.
*예를 들어 list난 string 모두 파이썬 개발자들이 각각 list, string class를 미리 만들어 놨고 그에 따라 생성되는 값들임.
*string + string 할 수 있는 것도 string 클래스에 해당 연산이 가능하도록 설정되어 있기 때문.

클래스 정의
*클래스란 자료형을 정의하는 틀 또는 설명서라고 이해하면 됨. 클래스를 통해 특정 자료형이 어떻게 표현되고 연산되며 어떤 함수를 사용할 수 있는지를 정의하게 됨.

일단 클래스의 정의 안에는 pass만 써두겠습니다. pass는 그냥 다른 내용은 쓰지 않겠다고 표시하는 명령어입니다.

class User:
    pass

# User값들 생성
user1 = User()
user2 = User()

# 파이썬의 기본 자료형
print(type(7))
print(type(3.14))
print(type("hello"))
print(type([1, 2, 3, 4, 5]))

# 우리가 만든 자료형
print(type(user1))
print(type(user2))
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
<class '__main__.User'>
<class '__main__.User'>
<class '__main__.User'>라고 나와있는 것을 확인할 수 있습니다. 1이 int 클래스의 값이고 "hello"는 str 클래스의 값입니다. 비슷한 개념으로 user1과 user2는 우리가 실행한 파일(main 파일)에 정의되어 있는 User 클래스의 값이란 뜻입니다.

인스턴스
*인스턴스란 특정 메모리 값에 저장 된 특정 클래스 값
class User:
    pass

user1 = User()
user2 = User()

print(user1 == user2)
False
분명 user1과 user2는 똑같이 User()를 써서 생성하였는데 왜 False가 출력될까요?

User()를 호출하면 메모리의 특정 공간에 새로운 User 값이 생성되고, 그 메모리 주소가 리턴돼서 user1과 user2에 저장됩니다. 그런데 User()를 호출할때마다 새로운 메모리 공간에 값을 생성하기 때문에 user1과 user2는 엄밀히 따지면 다른 값, 또는 다른 인스턴스입니다. 따라서 user1 == user2는 False가 나오는 것입니다!