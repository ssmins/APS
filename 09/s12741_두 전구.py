''''''

'''
# 풀이 1 
T = int(input())
result_list = []
for testcase in range(1, T+1):
    A1, A2, B1, B2 = map(int, input().split())

    result = min(B2, A2) - max(A1, B1)

    if result < 0 :
        result = 0

    result_list.append(result)

for index, value in enumerate(result_list, 1):
    print(f'#{index} {value}')
'''

# 풀이 2
T = int(input())
result_list = []
for testcase in range(1, T+1):
    result = [0] * 101  # 문제 조건
    A1, A2, B1, B2 = map(int, input().split())

    for i in range(A1, A2):
        result[i] += 1
    for j in range(B1, B2):
        result[j] += 1

    result_list.append(result.count(2))

for index, value in enumerate(result_list, 1):
    print(f'#{index} {value}')

'''
# 라이브 강사님 코드
# 테스트 케이스의 수가 50,000개.
# for loop에서 출력하면 input / output 이 번갈아가며 발생한다.
# 입력/출력에 시간을 꽤 많이 쓰는구나 ! 확인 -> 시간 초과 발생
    # 그래서? : 결과를 모았다가 한 번에 출력해야 한다.

T = int(input())
result_list = [] # 결과들을 저장할
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())

    # 나중에 켜진 전구 시간이 시작점
    start = max(A, C)
    # 먼저 꺼진 전구 시간이 끝점
    end = min(B, D)


    result = end - start
    if result <= 0 :
        result = 0

    result_list.append(result)

for index, result in enumerate(result_list):
    print(f'#{index + 1} {result}')
'''

'''
# 시간 비교

import time

# 매번 출력하는 경우
start_time = time.time()
for i in range(50000):
    print(i)
end_time = time.time()
print(f'{end_time - start_time:.4f}초')

# 결과 저장 후 한 번에 출력하는 경우
start_time = time.time()
result = []
for i in range(50000):
    result.append(i)
print(result)
end_time = time.time()
print(f'{end_time - start_time:.4f}초')

# 출력이 많으면 몰아서 하자 ! -> input/output 변환 시만 Buffer 
'''


'''
# 1차 시기 - <시간 초과> 
T = int(input())
for testcase in range(1, T + 1):
    A1, A2, B1, B2 = map(int, input().split())
    result = 0

    # 1 겹치고 A < B 일 경우
    if A1 < B2 and A2 > B1:
        if A2 < B2:
            result = A2 - B1
        else:
            result = B2 - B1

    # 2 겹치고 B < A 일 경우
    elif B1 < A2 and B2 > A1:
        if B2 < A2:
            result = B2 - A1
        else:
            result = A2 - A1

    # 안 겹칠 경우
    # if A1 > B2 or A2 < B1:
    #     result = 0

    print(f'#{testcase} {result}')
'''