
def find(x):
    if prevent_duplicated[x] == x:
        return x
    else:
        prevent_duplicated[x] = find(prevent_duplicated[x]) # 경로 압축
        return find(prevent_duplicated[x])

def union(x, y):
    global result
    if find(x) == find(y):
        result = 'WARNING'
        return
    prevent_duplicated[find(y)] = find(x)

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
prevent_duplicated = [i for i in range(N)] # 인덱스 0 부터 받기
result = 'STABLE'
for i in range(N):
    for j in range(i+1, N):
        if matrix[i][j] == 1:
            union(i, j)
print(result)