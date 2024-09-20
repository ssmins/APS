
matrix = [[0, 0, 1, 0, 1, 1],
          [1, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 1, 0],
          [1, 0, 0, 0, 0, 0],
          [1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

A, B = map(int, input().split()) # A에서 B까지 갈 수 있는 최소 경로 수
A -= 1
B -= 1 # 인덱스 맞추기
used = [0] * 6
min_level = float('inf')

def dfs(level, node, end):
    # 몇 회만에(level) end 노드에 도달할 수 있는지 출력
    global min_level

    if node == end:
        min_level = min(level, min_level)

    for i in range(6): # 노드 수
        if matrix[node][i] == 0: # 갈 수 없는 곳이라면 X
            continue
        if used[i] == 1: # 이미 간 곳이라면 X
            continue
        used[i] = 1
        dfs(level+1, i, end)
        # used[i] = 0

dfs(0, A, B)
if min_level == float('inf'):
    min_level = 0
print(min_level)


