# 1 <= N, M <= 1,000,000 , N != M
# 사용할 수 있는 연산은 +1, -1, *2, -10 => DFS인가 ?
# 연산 중간, 결과가 1,000,000 넘어가면 return

def dfs(level, x, end):
    global min_level

    # 가지치기
    if level > min_level: return

    # 가지치기
    if x > 1000000: return

    # 기저조건
    if x == end:
        min_level = min(level, min_level)
        return

    dfs(level+1, x+1, end)
    dfs(level+1, x-1, end)
    dfs(level+1, x*2, end)
    dfs(level+1, x-10, end)

from collections import deque

def bfs(start, end):
    global min_level
    q = deque()
    level = 0
    q.append((level, start))
    while q:
        now_level, now_x = q.popleft()
        if now_level > min_level: return
        if now_x > 1000000: return
        if now_x == end:
            min_level = min(now_level, min_level)
            return
        q.append((now_level+1, now_x+1))
        q.append((now_level+1, now_x-1))
        q.append((now_level+1, now_x*2))
        q.append((now_level+1, now_x-10))


T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split())
    min_level = float('inf')
    # dfs(0, N, M)
    bfs(N, M)
    # print(f'#{testcase} {min_level}')
    print(f'#{testcase} {min_level}')