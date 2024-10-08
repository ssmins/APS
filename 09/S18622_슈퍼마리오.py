''''''
'''
14
1 50 1 -1 1 3 -5 1 -15 0 100 1 1 2
--------------------------------------------------------
150
'''
'''
► 입력
150
4 1 6 4 -3 -4 -2 -6 -8 -9 -9 -8 -6 -12 -4 50 4 1 2 1 6 -4 -8 5 4 3 -1 -1 -2 -3 -4 -5 -6 -7 -8 34 1 2 6 4 7 2 -3 -4 -7 -8 1 2 4 1 6 4 -3 -4 -2 -6 -8 -9 -9 -8 -6 -12 -4 50 4 1 2 1 6 -4 -8 5 4 3 -1 -1 -2 -3 -4 -5 -6 -7 -8 34 1 2 6 4 7 2 -3 -4 -7 -8 1 2 4 1 6 4 -3 -4 -2 -6 -8 -9 -9 -8 -6 -12 -4 50 4 1 2 1 6 -4 -8 5 4 3 -1 -1 -2 -3 -4 -5 -6 -7 -8 34 1 2 6 4 7 2 -3 -4 -7 -8 1 2 3 1 5 21 15 23
--------------------------------------------------------
► 정답
304
'''
'''
► 입력
9
-1 -2 -3 -4 -5 -6 -7 -8 -9
--------------------------------------------------------
► 정답
-6
'''

N = int(input())
arr = list(map(int, input().split())) + [0]
dp_arr =  [float('-inf')] * (N+1) # 도착지점까지 인덱스를 만들어놓기

# DP를 활용하려면, 해당 칸이 가질 수 있는 최적해를 만들어줘야 한다.

dp_arr[2 - 1] = arr[2 - 1]
dp_arr[7 - 1] = arr[7 - 1]  # 초기값 설정
for i in range(len(dp_arr)+7):
    if 0 <= i-2 :
        if dp_arr[i-2] != float('-inf'): # 도달하지 못한 자리 빼고 -> 진짜 최소값인
            dp_arr[i] = max(dp_arr[i], arr[i] + dp_arr[i-2])
    if 0 <= i-7 :
        if dp_arr[i-7] != float('-inf'):
            dp_arr[i] = max(dp_arr[i], arr[i] + dp_arr[i-7])
    if i == N:
        maxx = float('-inf')
        for j in range(8): # 바로 마지막 요소에 들어올 수 있는
            if dp_arr[N-j] != float('-inf'):
                if dp_arr[N-j] > maxx:
                    maxx = dp_arr[N-j]
        print(maxx)
        break



'''
# 강사님 풀이
# 튜플로 입력받겟음 (변화시키지 않을거라서)

n = int(input())
a = tuple(map(int, input().split()))
a = (0,) + a + tuple(0 for _ in range(5)) # 인덱스 맞춰 주게 앞에 0을 추가, 이후에 N을 넘어도 출력 가능하므로 범위 늘리기 

# 최대 점수 dp테이블 초기화
dp = [float('-inf')] * (n + 6)
# 시작시점 점수는 0으로
dp[0] = 0
# 처음 7칸은 2칸 점프로 도달할 수 있는 위치 ---> 점수계산
for i in range(2, 8):
    dp[i] = dp[i - 2] + a[i]
# 7번째 칸은 7칸 점프로 바로 도달
dp[7] = a[7]
# 8번째 칸부터 끝까지
for i in range(7, n + 6):
    # 7칸전에서 점프, 2칸 전에서 점프
    dp[i] = max(dp[i - 7] + a[i], dp[i - 2] + a[i])

print(max(dp[n:]))
'''
