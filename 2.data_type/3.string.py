# 문자열을 만드는 방법
'Do you want to take cs101?'
"Do you want to learn python?"
'코드잇'
"유재석"
# 문자열을 만드는 방법이 다양한 이유
# 문자열 내에 ' 또는 "를 포함시키고 싶을 때에는, 서로 다른 인용부호를 사용해야 합니다.

# 사례 1
print('I'm excited to learn python!') # 틀린 예
# 위의 코드를 실행하면 'I'만 문자열로 인식되어 '문법 오류(Syntax Error)'가 나오는데요. 이럴 때에는 아래와 같이 "를 사용해야 합니다.

print("I'm excited to learn python!") # 맞는 예
# 사례 2
print("Steve Jobs says, "Everyone should learn CS."") # 틀린 예
# 위의 코드를 실행하면 역시 "Steve Jobs says, "만 문자열로 인식되어 오류가 나오는데요. 이럴 때는 아래와 같이 '를 사용해야 합니다.

print('Steve Jobs says, "Everyone should learn CS."') # 맞는 예
# 덧셈을 이용해 문자열 합치기
# 숫자형에서의 +는 왼쪽의 수와 오른쪽의 수를 '수학적으로 더하라'는 의미입니다. 하지만 문자열에서의 +는 왼쪽의 문자열과 오른쪽의 문자열을 '이어 연결하라'는 의미입니다.

print("Hello, " + "World!")

language = "파이썬"
print("우리가 배울것은 " + language + "!")

print("3" + "5")
Hello, World!
우리가 배울것은 파이썬!
35
# 곱셈을 이용해 문자열 반복하기
# 숫자형에서의 *는 왼쪽의 수와 오른쪽의 수를 '수학적으로 곱하라'는 의미입니다. 하지만 문자열에서의 *는 왼쪽의 문자열을 오른쪽의 수만큼 '반복하라'는 의미입니다.

fly = "날아라! "
print("떴다떴다 비행기!")
print(fly * 2)
떴다떴다 비행기!
날아라! 날아라!