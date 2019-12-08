# 리스트 인덱싱 연습
# greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
# greetings의 원소를 모두 출력해주는 프로그램을 작성해보세요. while문과 리스트의 개념을 활용하시면 됩니다. 아래의 내용이 콘솔에 출력되게 하세요.

# 안녕
# 니하오
# 곤니찌와
# 올라
# 싸와디캅
# 헬로
# 봉주르

i = 0
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]
while i < 7:
    print(greetings[i])
    i += 1

# *print 잘바꿈 자동으로 되는 이유
# print가 갖고 있는 기본값. 만약 쭉 쓰고 싶다면 print(greetings[i], end=" ") 와 같이 쓰면 됨. print함수 파라미터가 end="\n" 로 되어 있다보니 생기게 됨.