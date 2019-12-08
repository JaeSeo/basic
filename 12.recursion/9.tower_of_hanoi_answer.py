문제 풀이 방식
난이도 0
일단 가장 쉬운 경우는 원판이 하나도 없을 때입니다. 아무것도 안 해도 게임이 끝납니다.

(힌트: 이게 base case겠죠?)

난이도 1
원판이 1개밖에 없는 경우도 쉽죠? 1번 기둥에서 3번 기둥으로 옮기면 끝납니다.



난이도 2
원판이 2개인 경우는 조금 더 생각을 해야합니다. 1번 원판을 1번 기둥에서 2번 기둥으로 옮기고, 2번 원판을 1번 기둥에서 3번 기둥으로 옮기고, 1번 원판을 2번 기둥에서 3번 기둥으로 옮기면 됩니다.



난이도 3
이제 원판 3개인 경우입니다.



일단 3번 원판이 3번 기둥에 가야하는데, 그러기 위해서는 1, 2번 원판이 2번 기둥에 가있어야겠죠? 그런데 원판 두개를 옮기는 것은 이미 '난이도 2'에서 했습니다. 그냥 그대로 따라하면 됩니다.

이걸 프로그래밍 방식으로 생각하면 hanoi 함수를 재귀적으로 호출한다고 얘기할 수 있습니다. 그렇게 원판 2개를 옮겼다고 가정합시다.



이제 원하던대로 3번 원판을 3번 기둥으로 옮기면 됩니다.



마지막으로 2번 기둥에 있는 원판 두개를 3번 기둥으로 옮겨야 하는데, 이것도 '난이도 2'에서 한 것과 똑같이 하면 됩니다. 또 hanoi 함수를 부르는 셈이죠.



난이도 4
원판 4개인 경우도 원판 3개인 경우랑 똑같이 생각할 수 있습니다.



4번 원판을 3번 기둥으로 옮기기 위해서 그 위에 원판 3개를 먼저 2번 기둥으로 옮겨야 합니다. 원판 3개를 옮기는 것은 '난이도 3'에서 한 방식 그대로 하면 됩니다.



그리고 나서 4번 원판을 3번 기둥으로 옮기고...



다시 '난이도 3'의 방식대로 원판 3개를 3번 기둥으로 옮기면 끝납니다.



정리
시작하는 기둥을 start_peg, 목표 기둥을 end_peg, 그리고 나머지 기둥을 other_peg라고 부릅시다. 그러면 문제 풀이 방식을 이렇게 정리할 수 있습니다:

가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동
가장 큰 원판을 start_peg에서 end_peg로 이동
나머지 원판들을 other_peg에서 end_peg로 이동
코드 쓰기
이제 이 위의 문제 풀이 개념들을 코드에 반영해야 합니다. 현재까지 주어진 코드입니다:

def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
Base Case
맨 처음에 '난이도 0'에서 말했듯이 원판이 없을 때가 base case입니다. 원판이 없으면 아무것도 할 필요 없기 때문에 return을 써서 그냥 함수 실행을 끝내주면 됩니다.

def hanoi(num_disks, start_peg, end_peg):
    # base case
    if num_disks == 0:
        return
Recursive Case
자동으로 원판이 하나 이상일때는 recursive case입니다. 아까 정리한 문제 풀이 방식을 코드로 옮겨봅시다.

일단 start_peg와 end_peg가 주어졌을 때 other_peg는 어떻게 구할까요? 1번 기둥, 2번 기둥, 3번 기둥이 있기 때문에 start_peg + end_peg + other_peg는 항상 6입니다. 따라서 other_peg는 이렇게 정의할 수 있겠네요:

other_peg = 6 - start_peg - end_peg
먼저 가장 큰 원판을 제외하고 나머지 원판들을 start_peg에서 other_peg로 이동해야 합니다. 이건 원판 num_disks - 1개가 있는 하노이의 탑 문제랑 똑같죠?

hanoi(num_disks - 1, start_peg, other_peg)
이제 가장 큰 원판을 start_peg에서 end_peg로 이동해야 하는데, 가장 큰 원판의 번호는 num_disks이기 때문에 이렇게 쓸 수 있습니다:

move_disk(num_disks, start_peg, end_peg)
마지막으로 나머지 원판들을 other_peg에서 end_peg로 이동하면 끝납니다.

hanoi(num_disks - 1, other_peg, end_peg)
모범 답안
def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

def hanoi(num_disks, start_peg = 1, end_peg = 3):
    if num_disks == 0:
        return
    else:
        other_peg = 6 - start_peg - end_peg
        hanoi(num_disks - 1, start_peg, other_peg)
        move_disk(num_disks, start_peg, end_peg)
        hanoi(num_disks - 1, other_peg, end_peg)

hanoi(3, 1, 3)