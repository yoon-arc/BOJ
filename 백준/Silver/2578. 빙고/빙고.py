#세로, 가로, 대각선이 지우지는 경우 한 줄 완성, 선 세대부터 빙고. 
#적어도 15번째부터 검사하기
bingo = [list(map(int, input().split())) for _ in range(5)]
commands = [list(map(int, input().split())) for _ in range(5)]

#빙고 검사 함수
def check_bingo_h():
    total = 0
    for h in range(5):
        if all(bingo[h][y] == 'x' for y in range(5)):  # 한 행이 모두 'x'인지 체크
            total += 1
    return total

def check_bingo_y():
    total = 0
    for y in range(5):
        if all(bingo[x][y] == 'x' for x in range(5)):  # 한 열이 모두 'x'인지 체크
            total += 1
    return total

def check_bingo_d1():
    # 대각선 왼쪽에서 오른쪽
    if all(bingo[i][i] == 'x' for i in range(5)):
        return 1
    return 0

def check_bingo_d2():
    # 대각선 오른쪽에서 왼쪽
    if all(bingo[i][4-i] == 'x' for i in range(5)):
        return 1
    return 0

total_count = 0
bingo_count = 0
found_bingo = False

for line in range(5):
    for command in range(5):
        c = commands[line][command]
        
    #검사하기
        for i in range(5):
            for j in range(5):
                if bingo[i][j] == c:
                    bingo[i][j] = 'x'
                    
        # 15번째부터 검사하기
        total_count += 1
        if total_count >= 12:
            bingo_count = check_bingo_h() + check_bingo_y() + check_bingo_d1() + check_bingo_d2()

            # 3개 이상의 빙고가 발생
            if bingo_count >= 3 and not found_bingo:
                print(line * 5 + command + 1)
                found_bingo = True  # 빙고가 발생했음을 표시하고 이후에는 출력하지 않음
                exit()