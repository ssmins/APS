
n, m = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
for _ in range(2): # 두 번의 공격 정보
    start, end = map(int, input().split())
    for y in range(start-1, end):
        for x in range(m):
            if matrix[y][x] == 1: # 1을 만나면
                matrix[y][x] = 0 # 한 번 바꾸고
                break # x에 대한 for 문 자체를 끝내 버림
    # 못 만나고 종료되면 .. 아무 일도 없다.
# 두 번의 공격이 다 끝나면,
cnt = 0
for y in range(n):
    for x in range(m):
        if matrix[y][x] == 1 :
            cnt += 1
print(cnt)