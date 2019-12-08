# 단어장 만들기
# 영어 강사 Coy가 학생들의 영어 단어 암기를 위해 단어장 프로그램을 만들려고 합니다. 이 프로그램은 콘솔로 영어 단어와 한국어 뜻을 받고, vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리합니다.

# 프로그램을 실행하면 영어 단어와 한국어 뜻을 입력할 수 있습니다. 단어-뜻을 입력할 때마다 vocabulary.txt에 단어가 정리됩니다. 프로그램을 끝내려면, 알파벳 q를 입력하면 됩니다.

# 영어 단어를 입력하세요: 
# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요: 
# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요: 고양이
# 영어 단어를 입력하세요:
# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요: 고양이
# 영어 단어를 입력하세요: apple
# 한국어 뜻을 입력하세요:
# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요: 고양이
# 영어 단어를 입력하세요: apple
# 한국어 뜻을 입력하세요: 사과
# 영어 단어를 입력하세요: 
# 이런식으로 단어를 8개 입력했다고 가정합시다.

# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요: 고양이
# 영어 단어를 입력하세요: apple
# 한국어 뜻을 입력하세요: 사과
# 영어 단어를 입력하세요: church
# 한국어 뜻을 입력하세요: 교회
# 영어 단어를 입력하세요: temple
# 한국어 뜻을 입력하세요: 절
# 영어 단어를 입력하세요: wallet
# 한국어 뜻을 입력하세요: 지갑
# 영어 단어를 입력하세요: backpack
# 한국어 뜻을 입력하세요: 책가방
# 영어 단어를 입력하세요: soap
# 한국어 뜻을 입력하세요: 비누
# 영어 단어를 입력하세요: bicycle
# 한국어 뜻을 입력하세요: 자전거
# 영어 단어를 입력하세요: q
# 알파벳 q를 입력함으로써 프로그램을 종료하면 vocabulary.txt에 다음과 같이 단어들이 정리되어 있어야 합니다.

# cat: 고양이
# apple: 사과
# church: 교회
# temple: 절
# wallet: 지갑
# backpack: 책가방
# soap: 비누
# bicycle: 자전거

# word_book = ''
# while True:
#     english = input('영어 단어를 입력하세요: ')
#     if english == 'q':
#         break
#     korean = input('한국어 뜻을 입력하세요: ')
#     word = english + ': ' + korean + '\n'
#     word_book += word

# word_file = open('vocabulary.txt', 'w', encoding = 'utf-8')
# word_file.write(word_book)
# word_file   .close()

word_file = open('9.data_analysis101/vocabulary.txt', 'w', encoding = 'utf-8')

while True:
    english = input('영어 단어를 입력하세요: ')
    if english == 'q':
        break
    korean = input('한국어 뜻을 입력하세요: ')
    if korean == 'q':
        break    
    # word = english + ': ' + korean + '\n'
    # word_file.write(word)
    word_file.write("%s: %s\n" % (english, korean))

word_file.close()