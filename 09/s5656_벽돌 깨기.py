''''''






'''
# 라이브 강사님 코드

# N번 쏠 수 있고,
# 자료구조랑 알고리즘을 같이 보면서 생각해야 한다.
# 자료구조 - 2차원리스트
# 상하좌우 - 델타배열 + 파워
# 최대한 많은 벽돌을 제거하려면 - 완전 탐색 -> N번 각 열마다 모두 떨어뜨려봐야 한다.
# N이 크지 않아 시간복잡도는 낮을 수 있다
# 1~W 열에 쏘고, 그 다음은 1~N 에 쏜다 -> 재귀, DFS, 순열 ..
# 코드가 실행되고 다시 돌아갈 때, '원본' 이차원 리스트 정보가 같이 넘어가고, '복구'된다.
# 더 좋은 방법 없을까 ? -> 복사본을 수정하고 다음으로 전달하는 게 복구하는 데 낫다.
# copy_arr = arr(원본) -> 원본 자체가 바뀌어서 안 된다. 값만 가져가는 식으로
# copy_arr = [row[:] for row in arr]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def shoot(level, remains, now_arr):
    global min_blocks

    # 기저조건
    # 구슬을 모두 발사했거나 남은 벽돌이 0이면
    if level == N or remains == 0 :
        # 최소값 갱신
        min_blocks = min(min_blocks, remains)
        return

    # 한 줄씩 쏘기
    for col in range(W):
        # 방법 1)
        # col 위치에 쏘기 전 상태를 복사
        # '원본' 리스트의 col 위치에 구슬 쏘기 - append()과 유사
        # level + 1 번 상태로 이동 (다음 재귀 호출) - 재귀호출
        # col 위치에 쏘기 전 상태로 복구 - pop()과 유사

        # 방법 2) < 복구작업 시간을 줄이기 위함 >
        # col 위치에 쏘기 전 상태를 복사
        # '복사한' 리스트의 col 위치에 구슬 쏘기
        # level + 1 번 상태로 이동 (다음 재귀 호출) - col 위치에 쏘고 난 상태를 함께 전달

        copy_arr = [row[:] for row in now_arr]

        # col 위치에 구슬 쏘기
        # 구슬을 쏘는 열에서 가장 위에 있는 벽돌 찾기
        row = -1 # 벽돌 없다 가정
        for r in range(H):
            if copy_arr[r][col] : # r 위치에 벽돌이 있다면
                row = r # 가장 위로 row 초기화
                break
        if row == -1: # 벽돌이 없는 열이면 다음 열로 넘어가기
            continue

        # 연쇄적으로 벽돌 깨지는 걸 구현
        # 행, 열, 숫자(파워) 정보가 포함돼야 하겠다 .
        lst = [(row, col, copy_arr[row][col])] # 앞으로 깨져야 할 벽돌들을 저장
        now_remains = remains - 1
        copy_arr[row][col] = 0

        while lst: # 후보군이 남아있을 때까지 반복
            r, c, p = lst.pop()
            for k in range(1, p): # power만큼 퍼지면서 깨진다.
                for i in range(4): # 상하좌우
                    nr = r + dy[i]*k # row
                    nc = c + dx[i]*k # column

                    if nr < 0 or nr >= H or nc <0 or nc >= W: # 범위 계산
                        continue

                    if copy_arr[nr][nc] == 0: # 벽돌이 없다면 통과
                        continue

                    lst.append((nr, nc, copy_arr[nr][nc])) # 다음 벽돌 추가
                    copy_arr[nr][nc] = 0 # 현재 자리는 깨지고
                    now_remains -= 1 # 남은 벽돌 수 감소

        # 후보군이 다 깨졌으면, 빈칸 메꾸기를 해야지
        for c in range(W): # 전체 열들을 확인
            idx = H - 1 # 벽돌이 위치할 index
            for r in range(H-1, -1, -1):
                if copy_arr[r][c]: # 벽돌이 있으면 무조건 swap 하도록
                    # idx 와 r이 같아도, 바꾼다.
                    # 의미없는 교환일지라도 가독성을 위해 아래와 같이 구현한다.
                    copy_arr[r][c] , copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                    idx -= 1

        shoot(level + 1, now_remains, copy_arr)



# 벽돌 깨트리기 구현
    # 벽돌 중력으로 떨어진 것 구현


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())

    # 1. 최소 벽돌
    # - 몇 개 남았을까 계산해야 한다. -> 이차원 리스트를 순회하며 매번 계산하면 너무 느려 !
    # - 남은 벽돌 수 저장하는 것으로 해결됨
    # 2. 현재 벽돌이 다 깨지면(남은 벽돌이 없다면) 더 이상 진행할 필요 X
    # - 현재 남은 벽돌 수를 같이 저장하면 좋을 것 같다.
    # 3. N번 구슬을 쏘자
    # - 시작점 : 0번, 하나도 안 깨진 벽돌 수
    # - 끝점 : N번 쐈을 때 or 벽돌이 다 깨지면

    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = float('inf')
    blocks = 0
    # 현재 벽돌 수 계산
    for row in arr:
        for el in row:
            if el: # 0보다 크면 벽돌이 있는 것
                blocks += 1

    shoot(0, blocks, arr)

    print(f'#{tc} {min_blocks}')
'''