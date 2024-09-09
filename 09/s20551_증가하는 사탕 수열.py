''''''


T = int(input())
for testcase in range(1, T+1):
    a, b, c = map(int, input().split())
    result = 0

    # 조건에 애초에 맞지 않는다면
    if a < 1 or b < 2 or c < 3:
        print(f'#{testcase}', -1)
        continue

    # 여기서는 C를 먼저 비교하고, 다른 것들이 C보다 -1, -2일 수 있게 조정해줘야 한다.
    # 순증가하기만 하면 돼
    # 순증가하지 않는 경우는 뭐가 있을까
    # a >= b 일 경우, a >= c일 경우, b >= c일 경우
    # 3가지 경우로 하지 말고, (1) b < c 이게 만들어놓고, (2) a < b 이게 만들어놓는 두 번만 하자

    if b >= c:
        result += b-(c-1)
        b = c-1

    if a >= b:
        result += a-(b-1)
        a = b-1

    print(f'#{testcase} {result}')



'''
# 라이브 강사님 코드
# N <= 3000
# 완전 탐색 -> 3000^3 개의 경우의 수 -> backtracking, greedy, DP 로는 안되겠구나 판단해야 !
# 뒤에서부터 하나 적은 만큼 먹으면 되겠구나

T = int(input())
for testcase in range(1, T+1):
    # 반복문으로 구현할 필요 없으면, 굳이 리스트를 쓸 필요 없다.
    # box = list(map(int, input().split()))
    A, B, C = map(int, input().split())

    if B < 2 and C < 3: # A < B < C 구조를 만들 수 없는 케이스 처리
        print(f'{testcase} -1')
        continue

    eat = 0 # 먹은 사탕 개수
    # B가 C 이상일 때, B = C - 1 이라면 최소 개수
    if B >= C:
        eat += B - (C -1) # 차이만큼 먹기
        B = C - 1 # 설계가 간단한 경우는 이런 디테일때문에 변수값이 변할 수 있다.
        # A가 B 이상일 때, A = B - 1 이라면 최소 개수
    if A >= B :
        eat += A - (B - 1)
        A = B - 1

    print(f'#{testcase} {eat}')

# 자료구조 시간복잡도, 정렬 시간복잡도 O(NlogN) 정도는 외워두면 좋겠다
'''

'''
# 1차 시기 - <시간 초과> 
def dfs(x, count):
    global min_count

    # [가지치기]
    if candy[0] < 1 or candy[1] < 2 or candy[2] < 3:
        return

    # [가지치기]
    if count > min_count:
        return

    if x == 3:  # 3개의 상자
        if candy[1] - candy[0] != 1 or candy[2] - candy[1] != 1:
            return
        if count < min_count:
            min_count = count
        return

    for i in range(candy[x]):
        candy[x] -= i
        dfs(x + 1, count + i)  # 재귀를 쓸 때 함수 호출 시 변수 초기화 되는지 확인 !
        candy[x] += i


T = int(input())
for testcase in range(1, T + 1):
    candy = list(map(int, input().split()))
    min_count = float('inf')
    count = 0
    dfs(0, 0)
    if min_count == float('inf'):
        min_count = -1
    print(f'#{testcase} {min_count}')
'''

'''
# DFS 어느 정도 커지면 '값 할당'하게 설정
# 어느 정도면 그냥 할당으로 알 수 있을까 ?
# ex) 117, 533, 1876 - > 117, 118, 119 만드는 게 최선
# ex)
def dfs(x, count):
    global min_count
 
    # [가지치기] 애초에 안 될 때
    if candy[0] < 1 or candy[1] < 2 or candy[2] < 3:
        return
 
    # # [가지치기] 차례대로 클 때
    if 0 < candy[0] < candy[1] < candy[2] :
        A = candy[1] - (candy[0] + 1)
        B = candy[2] - (candy[0] + 2)
        if count + A + B < min_count:
            min_count = count + A + B
        return
 
    if count > min_count:
        return
 
    if x == 3:
        if candy[1] - candy[0] != 1 or candy[2] - candy[0] != 2:
            return
        if count < min_count:
            min_count = count
        return
 
    for i in range(candy[x]):
        candy[x] -= i
        dfs(x+1, count + i)
        candy[x] += i
 
 
T = int(input())
for testcase in range(1, T+1):
    candy = list(map(int, input().split()))
    min_count = float('inf')
    count = 0
    dfs(0, 0)
    if min_count == float('inf'):
        min_count = -1
    print(f'#{testcase} {min_count}')
'''


