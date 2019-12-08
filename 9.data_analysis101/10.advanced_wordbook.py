# 고급 단어장
# 학생들이 저번에 만든 단어장 퀴즈 프로그램은 늘 순서가 같아서 재미가 없다고 합니다. 이번에는 randint 함수와 사전(dictionary)을 이용해서 vocabulary.txt의 단어들을 랜덤한 순서로 테스트하는 프로그램을 써보세요.

# 같은 단어를 여러번 물어봐도 괜찮고, 프로그램은 알파벳 q를 입력할 때까지 실행됩니다.

# 교회: church
# 맞았습니다!

# 사과: apple
# 맞았습니다!

# 자전거: bicycle
# 맞았습니다!

# 지갑: wallet
# 맞았습니다!

# 교회: church
# 맞았습니다!

# 절: tample
# 틀렸습니다. 정답은 temple입니다.

# 비누: soap
# 맞았습니다!

# 고양이: dog
# 틀렸습니다. 정답은 cat입니다.

# 자전거: q

from random import randint

# 파일 열기
word_file = open('9.data_analysis101/vocabulary.txt', 'r', encoding = 'utf-8')

# 사전 생성
word_dict = {}

for word_line in word_file:
    # 정보 정리
    data = word_line.strip().split(':')
    english = data[0]
    korean = data[1]

    word_dict[english] = korean

while True:
    # 키 값 리스트 생성
    key_list = list(word_dict.keys())
    
    # 무작위 수
    random_index = randint(0, len(key_list) - 1)
    random_key = key_list[random_index]
    
    # 유저 입력 값 받기
    english_input = input("%s: " % word_dict[random_key])

    # 정답 확인
    if english_input == random_key:
        print("맞았습니다!")
    elif english_input == 'q':
        break
    else:
        print("아쉽습니다. 정답은 %s입니다." % random_key)
