
# 타당도 구하기
def dfs(x, points):

    # 기저조건
    if x == 2: # 두 지점이 만난다면, level : 2
        for start, end in points:
            validity = (people[start] + people[end])**2
        if validity > max_validiy:
            max_val
        return

    for i in range():


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    people = list(map(int, input().split()))

    validity = 0 # 타당도

    # 사람들이 원으로 둘러싸고 있는 형태,
