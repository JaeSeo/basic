# Floor Division
# // 연산자는 나눗셈 연산 후 결과값을 내림 합니다. 즉 소수부분을 버리고 정수부분만 남겨둡니다. 이걸 floor division이라고 부릅니다.

# 아래 두 개의 결과는 같습니다. 
x = int(5 / 2)  # 5를 2로 나눈 후 정수로 변환
print(x)    

x = 5 // 2      # 5를 2로 나눈 후 소수 부분을 버림
print(x)    
2
2
# /와 //의 차이를 직접 확인해보세요.

print(7 / 4)
print(int(7 / 4))
print(7 // 4)
1.75
1
1
# 주의할 점은 소수형이 있을 경우 결과값이 소수형으로 나온다는 것입니다.

print(5.0 // 2)
print(5 // 2.0)
print(5.0 // 2.0)
2.0
2.0
2.0

# 반올림
# round는 소수형을 반올림해줍니다.

print(round(1.421, 1))      # 1.421을 소수점 1째 자리로 반올림
print(round(2.7862, 2))     # 2.7562를 소수점 2째 자리로 반올림
print(round(3.141592, 4))   # 3.141592를 소수점 4째 자리로 반올림
print(round(4.34))          # 4.34를 소수점 0번째 자리로 반올림
1.4
2.79
3.1416
4
# 줄바꿈 기호 (Newline Character)
# 문자열 내에 \n 기호는 줄을 바꾸어주는 역할을 합니다. 키보드의 엔터키와 동일한 효과입니다.

print("안녕하세요\n코드잇입니다\n여러분 모두를\n환영합니다")
# 안녕하세요
# 코드잇입니다
# 여러분 모두를
# 환영합니다