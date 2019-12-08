# 자기 소개
# User 클래스에 introduce와 introduce_twice 메소드를 쓰세요.

# # sns의 유저
# class User:
#     # 초기값 설정
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#     # 자기 소개 (이름, 이메일)
#     def introduce(self):
#         # 코드를 입력하세요.

#     # 자기 소개 두번
#     def introduce_twice(self):
#         # 코드를 입력하세요.

# # 테스트
# user1 = User("Young", "young@codeit.kr", "123456")
# user1.introduce()
# user1.introduce_twice()
# My name is Young.
# My email address is young@codeit.kr.
# My name is Young.
# My email address is young@codeit.kr.
# My name is Young.
# My email address is young@codeit.kr.
# 위의 user1에 introduce 메소드를 호출하면,

# user1.introduce()
# 아래와 같이 출력됩니다.

# My name is Young.
# My email address is young@codeit.kr.
# 비밀번호는 당연히 말하면 안 되겠죠?

# user에 introduce_twice 메소드를 호출하면,

# user1.introduce_twice()
# 자기 소개가 두번 출력됩니다.

# My name is Young.
# My email address is young@codeit.kr.
# My name is Young.
# My email address is young@codeit.kr.
# *** 단, introduce_twice 메소드에는 print를 쓰면 안됩니다!

# sns의 유저
class User:
    # 초기값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # 자기 소개 (이름, 이메일)
    def introduce(self):
        print('My name is %s.' % self.name)
        print('My email address is %s.' % self.email)

    # 자기 소개 두번
    def introduce_twice(self):
        self.introduce()
        self.introduce()

# 테스트
user1 = User("Young", "young@codeit.kr", "123456")
user1.introduce()
user1.introduce_twice()