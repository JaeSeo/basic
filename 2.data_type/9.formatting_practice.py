# 문자열 포맷팅 연습
# 주어진 코드에서 wage는 1시간에 얼마 버는지를 나타내는 값이고, exchange_rate는 1달러를 한국 돈으로 바꾸면 얼마인지 나타내는 값입니다. 이 경우, 1시간 동안 번 금액은 wage * 1의 결과값인 5달러이고, 이 금액을 한국 돈으로 환전하면 wage * 1 * exchange_rate의 결과값인 5710.8원이 되는거죠.

# 문자열 포맷팅의 개념을 이용하여 아래의 문장들을 출력하세요.

# 1시간에 5달러 벌었습니다.
# 5시간에 25달러 벌었습니다.
# 1시간에 5710.8원 벌었습니다.
# 5시간에 28554.0원 벌었습니다.
# 주어진 변수와 문자열 포맷팅을 반드시 이용하셔야 합니다. 그리고 원화 금액은 소수점 첫째 자리까지만 출력되어야 합니다.

# <주의> 자동 채점 과제이기 때문에, 문제의

wage = 5                  # 시급 (1시간에 5달러)
exchange_rate = 1142.16   # 환율 (1달러에 1142.16원)

# "1시간에 5달러 벌었습니다." 출력
print("%d시간에 %d%s 벌었습니다." % (1, wage * 1, "달러"))

# "5시간에 25달러 벌었습니다." 출력
print("%d시간에 %d%s 벌었습니다." % (5, wage * 5, "달러"))

# "1시간에 5710.8원 벌었습니다." 출력
print("%d시간에 %.1f%s 벌었습니다." % (1, wage * exchange_rate * 1, "원"))

# "5시간에 28554.0원 벌었습니다." 출력
print("%d시간에 %.1f%s 벌었습니다." % (5, wage * exchange_rate * 5, "원"))
