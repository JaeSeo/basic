일단 주어진 코드입니다:

class User:
    # 초기값 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트
팔로우 기능
이제 "팔로우" 기능을 담당하는 follow 함수를 써야하는데요.

# 팔로우
def follow(self, another_user):
    # pass
과제에서 설명했듯이 follow 메소드에서 self의 following_list에 another_user를 추가하고, another_user의 followers_list에 self를 추가하면 됩니다.

# 팔로우
def follow(self, another_user):
    self.following_list.append(another_user)
    another_user.followers_list.append(self)
Follower 수, Following 수
이제 어떤 유저가 몇명을 '팔로우'하는지랑, 몇명이 그 유저를 '팔로우'하는지 리턴하는 함수를 써야합니다. 굉장히 쉽습니다. 그냥 self.following_list의 길이와 self.followers_list의 길이를 각각 리턴하면 됩니다.

# 몇명을 팔로우하는지 리턴
def num_following(self):
    return len(self.following_list)

# 팔로워가 몇명인지 리턴
def num_followers(self):
    return len(self.followers_list)
테스트
테스트를 해보면:

# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 테스트
user1.follow(user2)
user1.follow(user3)
user2.follow(user1)
user2.follow(user3)
user2.follow(user4)
user4.follow(user1)

print(user1.name, user1.num_followers(), user1.num_following())
print(user2.name, user2.num_followers(), user2.num_following())
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())
이렇게 나올 겁니다:

Young 2 2
Yoonsoo 1 3
Taeho 2 0
Lisa 1 1