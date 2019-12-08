# 학점 계산기
# 성적표를 기다리는 학생들을 위해서 학점 계산기를 만들려고 합니다.

# 절대 평가 방식으로 총 점수가 90점 이상이면 A를, 80점 이상 90점 미만이면 B를, 70점 이상 80점 미만이면 C를, 60점 이상 70점 미만이면 D를, 60점 미만이면 F를 부과하는 수업입니다.

# 성적이 A일 경우 "You get an A"를, B일 경우 "You get a B"를, C일 경우 "You get a C"를, D일 경우 "You get a D"를, F일 경우 "You fail"을 출력하는 함수를 쓰세요.

# def print_grade(midterm, final):
#     total = midterm + final
#     # 코드를 쓰세요.

# # 테스트
# print_grade(40, 45)
# print_grade(20, 35)
# print_grade(30, 32)
# print_grade(50, 45)
# You get a B
# You fail
# You get a D
# You get an A

def print_grade(midterm, final):
    total = midterm + final
    
    if total >= 90:
        print('You get an A.')
    elif total >= 80:
        print('You get a B.')
    elif total >= 70:
        print('You get a C.')
    elif total >= 60:
        print('You get a D.')
    else:
        print('You get a F.')

print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)