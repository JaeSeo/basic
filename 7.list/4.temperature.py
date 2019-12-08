# 온도 단위 바꾸기
# 화씨 온도(°F)를 섭씨 온도(°C)로 바꾸어주는 프로그램을 만들려고 합니다.

# 섭씨와 화씨의 관계식은 다음과 같습니다: °C = (°F - 32) x 5 / 9

# 아래의 코드에 이어서 정수형 fahrenheit을 파라미터로 받는 fahrenheit_to_celsius 함수를 써보세요. fahrenheit_to_celsius는 화씨 온도 fahrenheit를 섭씨 온도로 바꿔서 리턴합니다.

# # 화씨 온도에서 섭씨 온도로 바꿔주는 함수
# def fahrenheit_to_celsius(fahrenheit):
#     # 코드를 입력하세요.

# # 테스트용 온도 리스트
# sample_temperature_list = [40, 15, 32, 64, -4, 11]

# # 화씨 온도 출력
# print("화씨 온도 리스트: " + str(sample_temperature_list))

# # 리스트의 값들을 화씨에서 섭씨로 변환
# # 코드를 입력하세요.

# # 섭씨 온도 출력
# print("섭씨 온도 리스트: " + str(sample_temperature_list))
# 실행했을 때 아래처럼 출력되어야 합니다.

# 화씨 온도 리스트: [40, 15, 32, 64, -4, 11]
# 섭씨 온도 리스트: [4.44, -9.44, 0.0, 17.78, -20.0, -11.67]


##
# 화씨 온도에서 섭씨 온도로 바꿔주는 함수
def fahrenheit_to_celsius(fahrenheit):
    # 코드를 입력하세요.
    i = 0
    while i < len(fahrenheit):
        fahrenheit[i] = round((fahrenheit[i] - 32) * 5 / 9, 2)
        i += 1

# 테스트용 온도 리스트
sample_temperature_list = [40, 15, 32, 64, -4, 11]


# 화씨 온도 출력
print("화씨 온도 리스트: " + str(sample_temperature_list))

# 리스트의 값들을 화씨에서 섭씨로 변환
# 코드를 입력하세요.
fahrenheit_to_celsius(sample_temperature_list)

# 섭씨 온도 출력
print("섭씨 온도 리스트: " + str(sample_temperature_list))