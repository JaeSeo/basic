주어진 코드입니다.

# sns의 유저
class User:
    # 초기값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # 자기 소개 (이름, 이메일)
    def introduce(self):
        # 코드를 입력하세요.

    # 자기 소개 두번
    def introduce_twice(self):
        # 코드를 입력하세요.
introduce 메소드
# 테스트
user1 = User("Young", "young@codeit.kr", "123456")
user1.introduce()
여기서 user1.introduce()는 User.introduce(user1)과 동일합니다. 따라서 introduce 메소드에서 self.name은 "Young"이고 self.email은 "young@codeit.kr"입니다.

이 개념을 이용해서 introduce 메소드를 쓰면 됩니다.

def introduce(self):
    print("My name is %s" % self.name)
    print("My email address is %s" % self.email)
introduce_twice 메소드
introduce_twice 메소드도 물론 introduce 메소드처럼 이렇게 쓸 수 있습니다:

def introduce_twice(self):
    print("My name is %s" % self.name)
    print("My email address is %s" % self.email)
    print("My name is %s" % self.name)
    print("My email address is %s" % self.email)
하지만 이미 써놓은 코드를 또 쓰는 것은 프로그래머로서 다시 생각해봐야할 일이죠? 그래서 과제에서 introduce_twice 메소드에는 print를 쓰면 안 된다고 했습니다.

어떻게 고쳐볼 수 있을까요?

user1.introduce_twice()는 User.introduce_twice(user1)과 같습니다. 파라미터 self로 user1이 넘어간다는 뜻이죠. 그렇다면 이 코드는 어떤가요?

def introduce_twice(self):
    self.introduce()
    self.introduce()
self는 user1과 같기 때문에 self.introduce()는 user1.introduce()와 동일합니다. 그래서 그냥 self.introduce()를 두번 호출해주면 됩니다!

모범 답안
정리된 모범 답안입니다:

# sns의 유저
class User:
    # 초기값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # 자기 소개 (이름, 이메일)
    def introduce(self):
        print("My name is %s" % self.name)
        print("My email address is %s" % self.email)

    # 자기 소개 두번
    def introduce_twice(self):
        self.introduce()
        self.introduce()