''''''

''' 
# 순열로 풀기 -> 시간 초과 
# 문제 함수, 최소값 구하기
def for_minimum(lst):
    global min_sum
    my_sum = 0
    for i in range(N):
        my_sum += matrix[i][lst[i]]
    if my_sum < min_sum:
        min_sum = my_sum

# 순열 만들기
def make_permutation(x):
    if x == N :
        for_minimum(path)
        return
    for i in range(3):
        if not path or path[-1] != i:
            path.append(i)
            make_permutation(x+1)
            path.pop()

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
# used = [False] * (N+1)
path = []
min_sum = float('inf')
make_permutation(0)
print(min_sum)
'''

# DP로 풀기
# DP를 활용한 풀이
def coloring():
    dpmatrix = [[0]*3 for _ in range(N)]
    dpmatrix[0] = matrix[0]
    for i in range(1, N):
        dpmatrix[i][0] = matrix[i][0] + min(dpmatrix[i-1][1], dpmatrix[i-1][2])
        dpmatrix[i][1] = matrix[i][1] + min(dpmatrix[i-1][0], dpmatrix[i-1][2])
        dpmatrix[i][2] = matrix[i][2] + min(dpmatrix[i-1][0], dpmatrix[i-1][1])
    return min(dpmatrix[N-1])

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(coloring())
