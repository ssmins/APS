# 도시를 여행 가능한지 -> 같은 그룹인지 확인

import sys
input = sys.stdin.readline

def find(x):
    if boss[x] == x:
        return x
    boss[x] = find(boss[x]) # 최적화
    return find(boss[x])

def union(x, y):
    if find(x) == find(y):
        return
    boss[find(x)] = find(y)

N = int(input()) # 도시들의 수
boss = [i for i in range(N+1)] # 인덱스 에러 방지용
M = int(input()) # 여행 계획에 있는 도시들의 수
adjmatrix = [list(map(int, input().split())) for _ in range(N)]
for j in range(N):
    for i in range(j+1, N):
        if adjmatrix[j][i]:
            union(j, i)
question = list(map(int, input().split()))
result = 'YES'
for i in range(M-1):
    if find(question[i]-1) != find(question[i+1]-1):
        result = 'NO'
        break
print(result)