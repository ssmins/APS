''''''


dy = [-1, 1, 0, 0] # 상 하 좌 우
dx = [0, 0, -1, 1] # 상 하 좌 우

# (y, x)에서 출발해서, 몇 번 넘어갈 수 있는지 count로 셀 함수
def check(y, x):
    global count
    for i in range(4):
        sy = y + dy[i]
        sx = x + dx[i]
        if 0 <= sy < N and 0 <= sx < N and matrix[sy][sx] == matrix[y][x] + 1:
            count += 1
            check(sy, sx)

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 몇 번 재귀가 일어났는지 == 몇 번 다음 칸으로 이동할 수 있는지, 그것의 최대값을 구할 max_count
    max_count = float('-inf')

    # 최대값일 때, 시작점의 값을 min_start로 저장한다.
    min_start = float('inf')

    for y in range(N):
        for x in range(N):
            count = 1 # 처음 출발한 방부터 카운트 시작
            check(y, x)
            # 함수에서 나온 count와 max_count를 비교,
            if count > max_count: # max_count 보다 더 많이 갔을 때,
                max_count = count
                # max_count 지점일 때 start에 시작점의 값을 할당
                min_start = matrix[y][x]
            elif count == max_count: # max_count와 같은 지점만큼 갔을 때 (start 지점 초기화)
                start = matrix[y][x]
                if start < min_start:
                    min_start = start

    print(f'#{testcase} {min_start} {max_count}')



'''
# 라이브 강사님 코드

# import sys
# sys.stdin = open('input.txt', 'r')

# 접근 방법 1 - DFS

# 접근 방법 2
# 1. 전체 배열을 순회하면서 확인한다.
# 2. 인접한 방의 숫자가 현재 방보다 1 크면 -> visited[1] 체크
#      - 1이 크면 다음으로 갈 수 있다.
#   -> 다음으로 갈 수 있는 방이다 하는 정보를 저장

T = int(input())

# direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # index 에러 조심 !
    visited = [0] * (N * N + 1)

    # 전체 순회하면
    # 상하좌우에 나보다 1 크다면, visited 체크
    for i in range(N):
        for j in range(N):
            for k in range(4):
                # ny, nx는 다음 좌표
                ny = i + dy[k]
                nx = j + dx[k]

                # 범위 체크
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue
                # if 0 < ny <= N and 0 < nx <= N:

                # 내 옆이 나보다 1 크다면, 나는 다음으로 갈 수 있는 방이다.
                if arr[ny][nx] == arr[i][j] + 1:
                    visited[arr[i][j]] = 1
                    break
                    # 이미 체크된 순간 다른 방향은 볼 필요 없음
                    # 왜? 동일한 숫자가 없기 때문에 (!!)

    cnt = max_cnt = start = 0

    for i in range(N * N -1, -1, -1): # 앞에서부터 하면 실수 가능성 높은 문제 !
        if visited[i]:
            cnt += 1
        else :
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1 # 뒤에서부터 출발
            cnt = 0 # cnt 초기화

    print(f'#{tc} {start} {max_cnt + 1}')
'''

'''
2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2
'''

'''
#1 1 2 
#2 3 3 
'''