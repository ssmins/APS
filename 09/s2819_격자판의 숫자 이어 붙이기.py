''''''

# 튜플 사용하기
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우 4방향

def make_num(level, num, y, x): # (y, x)의 값이 더해진 숫자열을 뽑을 함수
    global result

    # 기저조건
    if level == 7:
        result.add(num)
        return

    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0 or ny >= 4 or nx >= 4:
            continue
        make_num(level+1, num*10 + matrix[ny][nx], ny, nx)


T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(4)]
    result = set() # 중복이 안 되는 자료구조, {set}
    for y in range(4):
        for x in range(4):
            make_num(0, 0, y, x)

    print(f'#{tc} {len(result)}')




'''
# 강사님 코드 
# dy = [-1, 1, 0, 0] # 상 하 좌 우
# dx = [0, 0, -1, 1] # 상 하 좌 우
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


# 방향배열로 찾아가기 , 7자리 수이니까 level == 7
def dfs(level, y, x, num):

    if level == 7:
        result.add(num)
        return

    for dx, dy in dir:
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue
        dfs(level+1, ny, nx, num*10 + arr[ny][nx])


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)] # 문제 조건 : 4*4 격자판
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(1, i, j, arr[i][j])

    print(f'#{tc} {len(result)}')
'''

'''
# 라이브 강사님 코드

# 핵심 : 7번 이동을 구현하라 !

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1,]

# 함수 정의
# 시작점 : 각 좌표 , 끝점? : 문자열의 길이가 7이면 종료

def dfs(y, x, path):
    # 기저조건
    if len(path) == 7:
        result.add(path) # set 메서드
        return

    # 상하좌우 확인하며 갈 수 있으면 이동
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        dfs(ny, nx, path + arr[ny][nx]) # 문자열을 누적하면서 다음으로 이동

T = int(input())
for tc in range(1, T+1):
    # 붙여나갈 때 편하게 문자열로 받는다.
    arr = [input().split() for _ in range(4)]
    # 중복을 제거하기 위해
    result = set()

    # 모든 칸을 이동하면서
    for i in range(4):
        for j in range(4):

            # 이 함수를 돌리며 필요한 정보들? (1) 좌표, (2) 누적된 문자열
            dfs(i, j, arr[i][j])

    print(f'#{tc} {len(result)}')
'''

'''
1
1 1 1 1
1 1 1 2
1 1 2 1
1 1 1 1
'''

'''
#1 23 
'''