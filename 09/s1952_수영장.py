''''''



def dfs(month, sum_price): # month : level
    global min_price

    # 기저조건
    if month > 12 : # 12월 넘어가면
        if sum_price < min_price:
            min_price = sum_price
        return

    dfs(month + 1, sum_price + price[0] * plan[month-1]) # 1일권
    dfs(month + 1, sum_price + price[1]) # 1개월권
    dfs(month + 3, sum_price + price[2]) # 3개월권

T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_price = price[-1] # 1년 이용권 사용하는 게 최대 비용이라 치면

    dfs(1, 0)
    print(f'#{tc} {min_price}')


# 강사님 코드

# 모든 경우의 수에서 > 최소 비용 구하기
# 12개월 -> 완전탐색 (재귀호출)
# 완전탐색 : 1일, 1달, 3달, 1년 이용권을 각각 사용했을 때마다 재귀호출
# 기저조건에 도달하면 결과 출력하고 return
# 기저조건 : 12월이 넘어가면 최소 비용 갱신하고 return

# 수영장
# 모든 경우의 수에서 ---> 최소 비용 구하기
# 12개월 12중첩 for문? ---> 완전탐색(재귀호출)
# 완전탐색 : 1일, 1달, 3달, 1년 이용권을 각각 사용했을때마다 재귀호출
# 기저조건에 도달하면(정점노드에 도달하면) 결과 출력하고 return
# 기저조건 : 12월이 넘어가면 최소 비용 갱신하고 return

def solve(month, sum_v):
    global = result
    # 기저조건
    if month > 12:  # 12월 넘어가면
        # 최소 비용 갱신
        return

    # 1일 이용권 사용 항상 month + 1(다음달로 이동), 일 수 * 1일 이용권 가격
    solve(month + 1, sum_v + (cost[0] * plans[month]))
    # 1달 이용권 사용 재귀호출

    # 3달 이용권 사용 재귀호출

    # 1년 이용권 사용 재귀호출


T = int(input())
for tc in range(1, T + 1):
    cost = list(map(int, input().split()))  # 1일, 1달, 3달, 1년 순서
    plans = input()  # 월별 이용 계획 입력(인덱스를 1부터 시작하기 위해서 0번 인덱스를 추가)
    result = float('inf')
    # 함수호출(1 월부터, 초기비용 0원)
    print(f'#{tc} {result}')

'''
# 라이브 강사님 코드 
# 접근 방법 1 
# 시작점 : 1월 / 누적금액 : 0원
# 끝점 : 12월 / 누적금액 : n원
def dfs(month, sum_cost):
    global ans
    # 기저조건 : 12월까지 모두 보았는가 ?
    if month > 12:
        ans = min(ans, sum_cost)
        return

    # 1일권으로 모두 구매한 경우 (다음 재귀에서 다음 달을 확인해야 한다)
    dfs(month + 1 , sum_cost + (days[month] * cost[0])
    # 1개월권으로 모두 구매한 경우 (다음 재귀에서 다음 달을 확인해야 한다)
    dfs(month + 1 , sum_cost + cost[1])
    # 3개월권으로 모두 구매한 경우 (다음 재귀에서 3달 후를 확인)
    dfs(month + 3 , sum_cost + cost[2])
    # 1년권으로 구매한 경우 (다음 재귀에서 12달 후를 확인 - X)
    dfs(month + 12 , sum_cost + cost[3])
    # tree 형태로 접근하면 쉽다


T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    # 인덱스가 헷갈린다면, 맨 앞에 빈 값 추가해주면 된다.
    days = [0] + list(map(int, input().split()))
    ans = 1e9 # 최소값 구할거니까
    dfs(1, 0) # 1월부터 시작, 시작금액 0원
    print(f'#{tc} {ans}')
'''

'''
# 접근 방법 2
# 3월 기준으로 생각한다면, 2월까지의 최소 금액 + 본인의 금액 중 최소금액
# 이전의 최소 금액들을 활용해서 내 최소금액을 구할 수 있다. -> DP 활용하기
# DP 가능한지 여부 확인
# 1. 작은 문제로 분할 가능해야 한다.
    # 전체 문제의 합 = 각 달까지의 최소 금액들이 쌓여서 완성
    # 각 달까지의 최소 금액 문제로 생각하면 된다.
# 2. 뒤에 결과를 구할 때 앞에서 구했던 결과가 변하면 안 된다.

T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))
    dp = [0] * 13 # 1월 ~ 12월 최소 금액들 저장
    dp[1] = min(days[0]*cost[0], cost[1])

    for i in range(1, 13):
        # 현재 달의 최소 비용 계산
        # 이전 달 + 1일권 구입 / 이전 달 + 1달권 구입 / 3달 전에 3달권 구입한 경우 중 최소

        if i < 3:
            dp[i] = min(dp[i-1] + days[i]*cost[0], dp[i-1] + cost[1])

        # index 오류를 피하기 위해, 3월 이후 계산을 따로 작성
        if i >= 3:
            dp[i] = min(dp[i] , dp[i - 3] + cost[2])

    # 12월까지 계산 결과 vs 1년권
    result = min(dp[12], cost[3])

    print(f'#{tc} {result}')
'''