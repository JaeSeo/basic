# 하노이의 탑
# 하노이의 탑 게임 아시나요? 이 게임의 목표는 왼쪽 기둥에 있는 원판들을 모두 오른쪽 기둥으로 옮기는 것입니다. 지켜야할 규칙은 두가지입니다:
# https://upload.wikimedia.org/wikipedia/commons/6/60/Tower_of_Hanoi_4.gif 
# 한 번에 하나의 원판만 옮길 수 있다.
# 큰 원판이 작은 원판 위에 있어서는 안 된다.


# (출저: 위키피디아)

# 과제
# 하노이의 탑 게임의 해답을 출력해주는 함수 hanoi를 쓰세요. hanoi는 파라미터로 원판 수 num_disks, 게임을 시작하는 기둥 번호 start_peg, 그리고 목표로 하는 기둥 번호 end_peg를 받고, 재귀적으로 문제를 풀어 원판을 옮기는 순서를 모두 출력합니다.

# def move_disk(disk_num, start_peg, end_peg):
#     print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

# def hanoi(num_disks, start_peg, end_peg):
#     # 코드를 입력하세요.

# # 테스트 코드 (포함하여 제출해주세요)
# hanoi(3, 1, 3)
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 2번 원판을 1번 기둥에서 2번 기둥으로 이동
# 1번 원판을 3번 기둥에서 2번 기둥으로 이동
# 3번 원판을 1번 기둥에서 3번 기둥으로 이동
# 1번 원판을 2번 기둥에서 1번 기둥으로 이동
# 2번 원판을 2번 기둥에서 3번 기둥으로 이동
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 가장 작은 원판의 번호는 1번이고 가장 큰 원판의 번호는 num_disks번입니다. 그리고 왼쪽 기둥이 1번, 가운데 기둥이 2번, 오른쪽 기둥이 3번입니다.

# 원판 하나인 경우
# hanoi(1, 1, 3)
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 원판 두개인 경우
# hanoi(2, 1, 3)
# 1번 원판을 1번 기둥에서 2번 기둥으로 이동
# 2번 원판을 1번 기둥에서 3번 기둥으로 이동
# 1번 원판을 2번 기둥에서 3번 기둥으로 이동
# 원판 세개인 경우
# hanoi(3, 1, 3)
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 2번 원판을 1번 기둥에서 2번 기둥으로 이동
# 1번 원판을 3번 기둥에서 2번 기둥으로 이동
# 3번 원판을 1번 기둥에서 3번 기둥으로 이동
# 1번 원판을 2번 기둥에서 1번 기둥으로 이동
# 2번 원판을 2번 기둥에서 3번 기둥으로 이동
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 힌트
# 재귀 파트에서 가장 어려운 문제이기 때문에, 안 풀리시더라도 좌절하실 필요가 전혀 없습니다!!! 이틀, 삼일 이상 고민할 가치가 있는 문제입니다. 어떻게 재귀적으로 문제를 어떻게 풀지 잘 생각해보세요. Recursive case는 뭐고 Base case는 무엇인가요?

# 하노이의 탑은 워낙 유명한 프로그래밍 문제라 쉽게 검색해서 답을 찾을 수 있을텐데요, 제대로 공부하고 싶으시면 절대로 검색하지 말고 직접 고민해보세요.

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    temp = 0
    if start_peg + end_peg == 3:
        temp = 3
    else:
        temp = abs(start_peg - end_peg)

    if num_disks == 1:
        move_disk(num_disks, start_peg, end_peg)
    else:
        hanoi(num_disks - 1, start_peg, temp)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks - 1, temp, end_peg)

# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)

# 모범 답안
def move_disk2(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))
    
def hanoi2(num_disks, start_peg, end_peg):
    transient = 6 - end_peg - start_peg
    
    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)
        
    return hanoi(num_disks - 1, start_peg, transient), move_disk(num_disks, start_peg, end_peg), hanoi(num_disks - 1, transient, end_peg)
 
hanoi(3, 1, 3)
