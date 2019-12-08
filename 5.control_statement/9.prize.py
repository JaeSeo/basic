# 택이의 우승상금
# 1988년 쌍문동에 사는 택이는 바둑대회 우승 상금으로 5000만원을 받았습니다. 하지만 바둑 외에는 아는게 없으니, 이웃 어른들에게 이 돈으로 무엇을 해야할지 물어보기로 하였습니다.

# 은행에서 근무하는 동일 아저씨는, 은행에 돈을 맡겨서 매년 이자로 12%씩 받는 것을 추천하셨습니다. 1년 후인 1989년에는, 5000만원의 12% 이자인 600만원이 더해져 5600만원이 된다고 하면서요.

# 이 이야기를 들은 미란 아주머니는 고작 12%때문에 생돈을 은행에 넣어 놓느냐며, 얼마 전 지어진 매매가 5000만원짜리 은마아파트를 살 것을 추천하셨습니다.

# 2016년 현재 은마아파트의 매매가는 11억원입니다. while문과 if문을 사용해 1988년 은행에 5000만원을 넣었을 경우 2016년에 얼마나 있을지 계산하여, 동일 아저씨나 미란 아주머니 중 누구의 말을 듣는 것이 좋을지 판단해보세요.

# 2016년에 은행에 저축해 둔 금액이 더 크다면, *원 차이로 동일 아저씨의 말씀이 맞습니다.가 출력되게 하세요. 하지만 은마 아파트의 가격이 더 크다면, *원 차이로 미란 아주머니의 말씀이 맞습니다.가 출력되게 하세요.

# (단 이자율은 매년 12%로 같다고 가정합니다.)

INTEREST = 1.12
APARTMENT = 1100000000

amount = 50000000
year = 1988

while year < 2016:
    amount *= INTEREST
    year += 1

if amount > APARTMENT:
    print("%d원 차이로 동일 아저씨 말씀이 맞습니다." % (amount - APARTMENT))

elif amount < APARTMENT:
    print("%d원 차이로 미란 아주머니 말씀이 맞습니다." % (APARTMENT - amount))

else:
    print("같습니다")
    
