# 팔린드롬
# "토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 팔린드롬(palindrome)이라고 부릅니다. 문자열 word가 팔린드롬인지 확인하는 함수 is_palindrome를 쓰세요. is_palindrome은 word가 팔린드롬이면 True를, 팔린드롬이 아니면 False를 리턴합니다.

# def is_palindrome(word):
#     # 코드를 입력하세요.

# print(is_palindrome("racecar"))
# print(is_palindrome("stars"))
# print(is_palindrome("토마토"))
# print(is_palindrome("kayak"))
# print(is_palindrome("hello"))
# "racecar"과 "토마토"는 거꾸로 읽어도 똑같기 때문에 True가 출력되어야 하고, "hello"는 거꾸로 읽으면 "olleh"가 되기 때문에 False가 나와야합니다.

# True
# False
# True
# True
# False

# 내 답안
# def is_palindrome(word):
#     word_list = list(word)
#     for left_index in range(len(word_list) // 2):
#         right_index = len(word_list) - left_index - 1
#         temp = word_list[left_index]
#         word_list[left_index] = word_list[right_index]
#         word_list[right_index] = temp

#     changed_word = ("").join(word_list)
#     if word == changed_word:
#         return True
#     else:
#         return False

# print(is_palindrome("racecar"))
# print(is_palindrome("stars"))
# print(is_palindrome("토마토"))
# print(is_palindrome("kayak"))
# print(is_palindrome("hello"))


# 해설
# 팔린드롬이 되기 위해서는 대칭되는 모든 글자 쌍이 일치해야 합니다. 단 한 쌍이라도 일치하지 않으면 나머지는 더 이상 볼 필요도 없는거죠.

def is_palindrome(word):
    for left in range(len(word) // 2):
        # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False

    # for문에서 나왔다면 모든 쌍이 일치
    return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))