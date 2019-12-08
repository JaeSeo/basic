# 거스름돈 계산기
# 현명하게 거스름돈을 계산해주는 프로그램을 만드려고 합니다. 예를 들어 33,000원짜리 물건을 사기 위해 100,000원을 냈다면, 50,000원 1장, 10,000원 1장, 5,000원 1장, 1,000원 2장과 같이 '가장 적은 수'의 지폐를 거슬러 주는 방식입니다.

# payment(지불한 금액)와 cost(가격)라는 파라미터 두개를 필요로 하는 함수 calculate_change를 쓰세요. 이 함수는 거스름돈을 위해 50,000원짜리와 10,000원짜리, 5,000원짜리, 1,000원짜리가 각각 몇 장 필요한지 출력해주는 역할을 합니다.

# 아래의 코드에 이어서 깔끔하게 프로그램을 작성해보세요.

# payment, cost 파라미터의 값은 1,000의 배수라고 가정합시다.

# def calculate_change(payment, cost):
#     # 코드를 작성하세요.

# # 테스트
# calculate_change(100000, 33000)
# print()
# calculate_change(500000, 378000)
# 함수를 쓰고 프로그램을 실행하면 아래와 같은 결과값이 콘솔에 출력되어야 합니다.

# 50000원 지폐: 1장
# 10000원 지폐: 1장
# 5000원 지폐: 1장
# 1000원 지폐: 2장

# 50000원 지폐: 2장
# 10000원 지폐: 2장
# 5000원 지폐: 0장
# 1000원 지폐: 2장

def calculate_change(payment, cost):
    residue_total = payment - cost
    
    residue_50000 = residue_total / 50000
    residue_sub1 = residue_total - 50000 * int(residue_50000)
    
    residue_10000 = residue_sub1 / 10000
    residue_sub2 = residue_sub1 - 10000 * int(residue_10000)
    
    residue_5000 = residue_sub2 / 5000
    residue_sub3 = residue_sub2 - 5000 * int(residue_5000)
    
    residue_1000 = residue_sub3 / 1000
    residue_sub4 = residue_sub3 - 1000 * int(residue_1000)
    
    print("50000원 지폐: %d장" % (residue_50000))
    print("10000원 지폐: %d장" % (residue_10000))
    print("5000원 지폐: %d장" % (residue_5000))
    print("1000원 지폐: %d장" % (residue_1000))

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)