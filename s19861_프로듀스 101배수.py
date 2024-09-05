''''''
# 논리적 부족함
# x % 101 == 0 인 경우는, x가 101의 배수일 때도 그렇지만, x가 0일 때도, x가 음수로 101의 배수일 때도 유효하다.
# 나누기, 특히 나머지 연산을 할 때 0이거나, 음수일 경우도 유의하며 계산하자

def operator_decision(lst):
    result = arr[0]  # 맨 첫 값을 저장해 두고,
    printresult = []
    printresult.append(arr[0])
    for i in range(len(lst)):
        if lst[i] == 0:  # *
            result *= arr[i + 1]
            printresult.append('*')
            printresult.append(arr[i + 1])
        if lst[i] == 1:  # +
            result += arr[i + 1]
            printresult.append('+')
            printresult.append(arr[i + 1])
        if lst[i] == 2:  # -
            result -= arr[i + 1]
            printresult.append('-')
            printresult.append(arr[i + 1])
    if result % 101 == 0 and result > 0 :
        for item in printresult:
            print(item, sep='', end='')
        print()
        # print(*printresult, sep='')
        return


def make_permutation(x):
    if x == N - 1:  # 필요한 연산자의 개수는 (N-1)개
        operator_decision(permutation)
        # print(permutation)
        return

    # 중복 가능한 연산자
    for i in range(3):  # 적용 가능한 연산자의 개수는 3개 # (0 : *), (1 : +), (2 : -)
        permutation.append(i)
        make_permutation(x + 1)
        permutation.pop()


N = int(input())
arr = list(map(int, input().split()))

permutation = []
make_permutation(0)


'''
# 강사님 코드
# 프로듀스 101배수
def calculate(idx, result, ex):
    # idx : 현재 처리중인 숫자의 인덱스, result : 현재까지 계산 결과, ex : 수식 문자열
    if idx == N - 1: # 모든 숫자를 다 사용했을 때(마지막 숫자까지 처리 했을 때)
        if result == 0:
            return
        # 100배수일 경우 수식 출력하고 return
        elif result % 101 == 0:
            print(ex)
            return
        # 101 배수가 아닐경우
        return
    # 곱하기 연산 수행 재귀 호출
    calculate(idx + 1, result * nums[idx + 1], ex + "*" + str(nums[idx + 1]))
    # 더하기 연산 수행 재귀 호출
    calculate(idx + 1, result + nums[idx + 1], ex + "+" + str(nums[idx + 1]))
    # 빼기 연산 수행 재귀호출
    calculate(idx + 1, result - nums[idx + 1], ex + "-" + str(nums[idx + 1]))

N = int(input())
nums = list(map(int, input().split()))
calculate(0, nums[0], str(nums[0]))
'''

'''
# 수한이 코드 
def find_101(nums, index, expr, val, results):
    if index == len(nums):
        if val != 0 and val % 101 == 0:
            results.append(expr)
        return

    next_num = nums[index]
    
    find_101(nums, index + 1, f"{expr}*{next_num}", val * next_num, results)
    find_101(nums, index + 1, f"{expr}+{next_num}", val + next_num, results)
    find_101(nums, index + 1, f"{expr}-{next_num}", val - next_num, results)

N = int(input())
nums = list(map(int, input().split()))

results = []
expr = str(nums[0])
value = nums[0]

find_101(nums, 1, expr, value, results)

for i in results:
    print(i)
'''