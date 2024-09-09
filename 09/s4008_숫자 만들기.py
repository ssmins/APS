''''''


'''
# 라이브 강사님 코드
# 음수는 어떡하지 ? 소수는 ?

def cal(num1, num2, oper_idx):
    if oper_idx == 0 :
        return num1 + num2

    if oper_idx == 1 :
        return num1 - num2

    if oper_idx == 2 :
        return num1 * num2

    if oper_idx == 3 :
        if num1 < 0 :
            return -(abs(num1) // num2)
        return num1 // num2

# 재귀 설계
# 시작점 : 첫 번째 숫자
# 끝점 : 모든 수(연산자)를 사용할 때까지
# 파라미터 : 특정 시점에서 계산된 결과값 같이 넣어주기 : total
def dfs(level, total):
    global min_result, max_result

    if level == N:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return

    # 4개의 연산자 확인
    for i in range(4):
        if opers[i] == 0 : # 남은 연산자가 없으면 통과
            continue

        opers[i] -= 1 # opers를 전역 변수처럼 쓰고 있다.
        dfs(level+1, cal(total, numbers[level], i))
        opers[i] += 1 # opers를 전역 변수처럼 쓰고 있기 때문에 원상태로 돌리는 과정이 필요

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_result = 1e9
    max_result = -1e9 # 연산 중의 값은 -1억 <= <= 1억이 보장된다.

    dfs(1, numbers[0])
    print(f'#{tc} {max_result - min_result}')
'''