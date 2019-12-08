함수 헤더(header) 작성
class User:
    # initialize 메소드를 여기 쓰세요
    # def initialize...

# 테스트
user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")
여기서 user1.initialize("Young", "young@codeit.kr", "123456")을 호출하면 User 클래스의 initialize 메소드가 실행되고 첫번째 파라미터로 인스턴스 user1이 넘어가게 됩니다. 그리고 "Young", "young@codeit.kr", "123456" 이 순서대로 2~4번째 파라미터로 넘어가게 됩니다.

따라서 아래 두 줄은 같다고 볼 수 있습니다:

user1.initialize("Young", "young@codeit.kr", "123456")
User.initialize(user1, "Young", "young@codeit.kr", "123456")
위의 두 줄 중 두번째 줄을 보니까 initialize는 파라미터로 4개의 값을 받아야겠죠? 저번 강의에서 말했듯이 첫번째로는 인스턴스로 self를 받고, 그 다음 문자열 name, 문자열 email, 문자열 password를 받으면 됩니다.

initialize 메소드의 헤더("header") 부분은 아래와 같이 쓸 수 있습니다:

class User:
    def initialize(self, name, email, password):
        pass
여기서 self는 user1, user2와 같은 인스턴스를 받기 때문에 인스턴스 변수 user1.name, user2.name에 각각 어떤 값을 지정하고 싶으면 self.name에 지정하면 됩니다.

class User:
    def initialize(self, name, email, password):
        self.name = name

user1.initialize("Young", "young@codeit.kr", "123456")
함수 바디(body) 작성
이렇게 쓰면 user1이 self로 넘어가고, "Young"이 name으로 넘어갑니다. 따라서 self.name = name은 user1.name = "Young"과 같은거죠.

똑같은 개념으로 initialize 메소드에서 '이메일'과 '비밀번호'에 해당하는 인스턴스 변수의 초기값도 설정해주려면 이렇게 하면 됩니다:

class User:
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
테스트
제대로 작동하는지 테스트를 해보려면:

# 샘플 유저 생성
user1 = User()
user1.initialize("Young", "young@codeit.kr", "123456")

user2 = User()
user2.initialize("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User()
user3.initialize("Taeho", "taeho@codeit.kr", "123abc")

user4 = User()
user4.initialize("Lisa", "lisa@codeit.kr", "abc123")

# 유저 정보 출력
print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)
Young young@codeit.kr 123456
Yoonsoo yoonsoo@codeit.kr abcdef
Taeho taeho@codeit.kr 123abc
Lisa lisa@codeit.kr abc123