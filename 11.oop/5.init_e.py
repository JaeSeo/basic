정의되어 있지 않은 인스턴스 변수를 사용하면 오류가 나오기 때문에 꼭 모든 인스턴스 변수를 정의해야 합니다. 그래서 저번 과제로 모든 인스턴스 변수를 초기값으로 설정해주는 initialize 메소드를 써봤습니다.

class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

# 샘플 유저 생성
user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")
그런데 보시다시피 매번 User 인스턴스를 생성하는 줄을 하나 쓰고, 초기값을 설정해주기 위해서 initialize 메소드를 호출하는 줄을 하나 썼습니다. 뭔가 좀 번거롭죠?

__init__ 매직 메소드
다행히 파이썬은 인스턴스 생성과 초기값 설정을 한번에 해결할 수 있도록 __init__이라는 특별한 메소드를 쓸 수 있게 해줍니다.

원래 써놓은 initialize 메소드의 이름만 __init__으로 바꾸겠습니다.

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
__init__ 메소드를 정의해놓으면 이제 유저 생성과 초기값 설정을 이렇게 깔끔하게 할 수 있습니다:

# 깔끔한 유저 생성 및 초기값 설정
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")
여기서 일어나는 일은 3가지입니다. 첫번째 유저 생성을 예로 들면:

메모리가 할당되고 User 인스턴스가 생성됩니다.
__init__ 메소드가 호출됩니다. 파라미터 self로는 생성된 인스턴스가 넘어가고 name, email, password로는 "Young", "young@codeit.kr", "123456"이 각각 넘어갑니다. 이 경우 인스턴스 변수들의 초기값이 모두 설정되는 거죠.
만들어진 User 인스턴스가 리턴돼서 변수 user1에 저장됩니다.
앞으로는 인스턴스 변수가 있는 클래스에는 무조건 __init__ 메소드를 써주시고, __init__ 메소드에 모든 인스턴스 변수의 초기값을 지정해주세요!