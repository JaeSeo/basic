# 단어 퀴즈
# 이제 단어 암기를 위해서 학생들을 퀴즈해주는 프로그램을 만들고 싶습니다. vocabulary.txt의 첫 줄부터, 콘솔에 한국어 뜻을 알려주면 학생이 영어 단어를 입력하는 방식입니다. 맞는 답이 나오면 맞았습니다!가 출력되고 틀린 답이 나오면 아쉽습니다. 정답은 OOO입니다. 형식으로 나옵니다.

# 고양이: cat
# 맞았습니다!

# 사과: fruit
# 아쉽습니다. 정답은 apple입니다.

# 교회: church
# 맞았습니다!

# 절: tample
# 아쉽습니다. 정답은 temple입니다.

# 지갑: wallet
# 맞았습니다!

# 책가방: bag
# 아쉽습니다. 정답은 backpack입니다.

# 비누: soap
# 맞았습니다!

# 자전거: bycicle
# 아쉽습니다. 정답은 bicycle입니다.

word_file = open('9.data_analysis101/vocabulary.txt', 'r', encoding = 'utf-8')
for word_line in word_file:
    # 정보 정리
    data = word_line.strip().split(':')
    english = data[0]
    korean = data[1]

    # 유저 입력 값 받기
    english_input = input("%s: " % korean)

    # 정답 확인
    if english_input == english:
        print("맞았습니다!")
    else:
        print("아쉽습니다. 정답은 %s입니다." % english)

word_file.close()