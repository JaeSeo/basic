# 변수 연습
# name(이름), nationality(국적), phone_number(핸드폰 번호)라는 변수를 만들고, 여러분에게 알맞은 정보들을 지정하세요. 변수와 문자열 포맷팅을 이용하여 아래와 같이 출력되게 하세요.

# Hi, my name is Codeit. I'm from Korea.
# My phone number is 010-1234-5678.
# 저는 이 경우 name을 문자열 "Codeit"으로, nationality를 문자열 "Korea"로, 그리고 phone_number를 문자열 "010-1234-5678"로 지정해줬습니다. 각각의 정보들은 여러분에 알맞게 수정하시면 됩니다.

name = "Codeit"
nationality = "Korea"
phone_number = "010-1234-5678"

print("Hi, my name is %s. I'm from %s.\nMy phone number is %s." % (name, nationality, phone_number))