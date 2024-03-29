# for문으로 구구단
# 예전에 했던 구구단 프로그램을 이번에는 while문 대신 for문을 써서 만들어보세요. 아래와 같이 출력되어야 합니다.

# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# .
# .
# .
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81

for i in range(10):
    for j in range(10):
        print("%d * %d = %d" % (i, j, i * j))

# 해설
# 제어문 섹션의 마지막 과제였던 '구구단 만들기' 생각나시나요? 그 과제에서는 while문을 사용했었는데, for 문을 쓰면 훨씬 간결하게 프로그램을 작성할 수 있습니다.

# # 앞자리 (1단부터 9단까지)
# for i in range(1, 10):
#     # 뒷자리
#     for j in range(1, 10):
#         print("%d * %d = %d" % (i, j, i * j))