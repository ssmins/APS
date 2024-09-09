''''''



def dfs(level, value):
    global min_result, max_result

    if level == N-1: # [0]을 이미 썼고, N-1까지만 써도 되니까, level : N -2 에서 할 일을 다 하고, N-1이면 할 일이 없다
        max_result = max(max_result, value)
        min_result = min(min_result, value)
        # print(max_result, min_result)
        return

    # 재귀에서 DFS를 하고 싶다면 , 재귀함수 호출 후에 원 상태와 같게 복구해줘야 한다.

    if operator[0]: # '+'가 남아 있다면
        operator[0] -= 1
        dfs(level+1, value + numbers[level+1])
        operator[0] += 1

    if operator[1]: # '-'가 남아 있다면
        operator[1] -= 1
        dfs(level+1, value - numbers[level+1])
        operator[1] += 1

    if operator[2] : # '*'가 남아 있다면
        operator[2] -= 1
        dfs(level+1, value * numbers[level+1])
        operator[2] += 1

    if operator[3]: # '//'가 남아 있다면
        operator[3] -= 1
        if value < 0 :
            dfs(level+1, abs(value) // numbers[level+1] * (-1)) # 음수 나눗셈
            operator[3] += 1
        else:
            dfs(level+1, value // numbers[level+1])
            operator[3] += 1

T = int(input())
for testcase in range(1, T+1):
    N = int(input()) # numbers의 개수 : N
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    result = numbers[0]
    max_result = -1e9
    min_result = 1e9

    dfs(0, numbers[0]) # level과 연산결과값을 받아 이동

    print(f'#{testcase} {max_result - min_result}')


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