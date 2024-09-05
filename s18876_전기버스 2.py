''''''
# 전기버스 2

# 백트래킹
# 각 정점별로 충전을 하는지 / 안 하는지에 따라 충전된 양과, 충전 횟수를 추가
# 그 중에서 가장 적은 충전 횟수로 끝 노드에 도달한 경우를 출력
# 가지치기로 min보다 큰 값이 count되면 return

# 한 이진수 덩어리가 주어졌을 때, 이 경우에 문제의 조건을 만족하는지 확인하는 함수.
def check(x):
    count = 0
    charge = charge_volume[0] - 1 # 맨 처음 곳에서 배터리 받아서 출발, 다음 지점 도착을 전제로 해서 (-1)
    global min_count

    for i in range(1, N-1): # charge_volume 리스트를 순회하면서 값 추가, 두 번째 위치부터
        if x & 0x1: # 충전하기로 했다면

            # 충전한다면, count +=1 해주고, 그 지점에서의 충전량 +=1 해주기
            if charge == 0: # 그런데 해당 지점에 도착했을 때 연료가 0이면 의미 없어.
                count = float('inf') # 종료되어도 최소 count값에 영향 x
                break # for 문 아예 종료
            count += 1 # 충전횟수 추가
            charge += charge_volume[i]

        x >>= 1
        charge -= 1 # 다음 지점으로 가는 데 드는 연료
        if charge < 0: # 다음 지점으로 갈 연료가 남아 있어야 마지막 인덱스에 닿는다.
            break

    if count < min_count:
        min_count = count

T = int(input())
for testcase in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    charge_volume = lst[1:]

    min_count = float('inf')
    for x in range(1<<(N-2)): # 시작점 제외(N-1), 종착점 제외(N-2), 충전소가 있는 위치에서 충전한다/충전하지 않는다 두 가지가 있는 부분집합을 만든다.
        # 만들어진 4자리 이진수 1011 덩어리가 x,
        check(x)

    print(f'#{testcase} {min_count}')

    # 레벨에 따라 나올 수 있는 부분집합의 수 -> N 만큼의 자리에서 충전한다/하지않는다.




'''
# DP?
# 각 정점별로 최소 충전량, 충전횟수 각각 dptable에 저장
# 이 노드에 도착할 때 최대값은 이거일 수밖에 없다 지정

T = int(input())
for testcase in range(1, T+1):
    lst = list(map(int, input().split()))
    N = lst[0]
    charge_volume = lst[1:]

    # 각 지점에 도달할 때 최소 충전 횟수를 저장
    dp_count = [0] * N
    dp_count[1] = 1

    # 각 지점에 도달할 때 최소 잔여 충전량을 저장
    dp_volume = [0] * N
    dp_volume[1] = charge_volume[1]

    for i in range(N):

# DP 도전 후 패배후기
# 한 지점에서의 충전 횟수와 충전 횟수를 바탕으로 한 충전량이 정해지고 그것이 최적해임이 확실할 수 있으면,
# 다음 지점을 탐색할 때 그 지점에서의 연산 없이 최적해만 가지고 가서 다음 지점의 해를 결정하는 게 DP인데,
# 여기서는 한 지점에서의 최적해가 다음 지점의 최적해와 연결이 안 될 수가 있어서 DP로는 단순히 풀기가 좀 어려울 것 같다.
'''