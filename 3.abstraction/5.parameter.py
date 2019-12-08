# 파라미터 연습
# 문자열 first_name(이름)과 문자열 last_name(성)을 파라미터로 받는 함수 print_full_name을 쓰세요. print_full_name은 first_name과 last_name을 다음과 같은 형태로 합쳐서 출력합니다.

# print_full_name 함수 정의
# 코드를 입력하세요.

# 테스트 코드
# print_full_name("윤수", "이")
# print_full_name("수민", "이")
# 이, 윤수
# 이, 수민

def print_full_name(first_name, last_name) :
    print("%s, %s" % (last_name, first_name))

# 테스트 코드
print_full_name("윤수", "이")
print_full_name("수민", "이")