''''''
# 다른 모든 지원자와 비교했을 때 둘 다 낮은 사람 -> 제외

'''
# 아무런 고려하지 않았을 때 코드

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        a, b = map(int, input().split())
        lst.append((a, b))
    removed = [0]*N
    for i in range(N):
        for j in range(N):
            s1, s2 = lst[i]
            s11, s22 = lst[j]
            if s1 < s11 and s2 < s22 :
                removed[j] = 1
    print(N-sum(removed))

# 시간 초과
# 범위 확인 : 시간 제한 2초, T <= 20, N <= 100,000
# 위 코드 : O(N) + O(N^2) 2초 내 100억 연산 ? X
# 2초 -> 최대 6천만 번 연산. O(N) 안에서 끝내야 한다.
'''

'''
# sort() : O(NlogN) 
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        a, b = map(int, input().split())
        lst.append((a, b))
    lst.sort() # 튜플 a 기준으로 정렬
    min_b = lst[0][1]
    cnt = 1
    for i in range(N):
        if lst[i][1] < min_b:
            min_b = lst[i][1]
            cnt += 1
    print(cnt)
'''

#
# T = int(input())
# for testcase in range(1, T+1):
#     N = int(input())
#     lst = []
#     (min_a, min_b) = N, N # min_a보다 크고(a를 못 하고) , min_b보다 크면(b를 못 하면)
#     cnt = N
#     for _ in range(N):
#         a, b = map(int, input().split())
#         if
#
#         lst.append((a, b))
#         if a < min_a:
#             min_a = a
#         if b < min_b:
#             min_b = b
#     for i in range(N):
#         if lst[i][0] > min_a and lst[i][1] > min_b:
#             cnt -= 1
#     print(cnt)
'''
# 인풋을 효율적으로 받지 못해 시간 초과된 경우
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        a, b = map(int, input().split())
        lst.append((a, b))
    lst.sort()  # 튜플 a 기준으로 정렬
    min_b = lst[0][1]
    cnt = 1  # 첫 번째 사람은 무조건 선택됨
    for i in range(1, N):
        if lst[i][1] >= min_b:  # min_b보다 크거나 같으면 넘어감
            continue
        cnt += 1  # min_b보다 작은 경우에만 카운트 증가
        min_b = lst[i][1]  # min_b 갱신
    print(cnt)
'''
# 인풋을 효과적으로 받은 경우, 시간초과 X, sort를 썼음에도
import sys

input = sys.stdin.read


def process_case(data):
    index = 0
    T = int(data[index])
    index += 1
    results = []

    for _ in range(T):
        N = int(data[index])
        index += 1
        lst = []

        for _ in range(N):
            a, b = map(int, data[index].split())
            lst.append((a, b))
            index += 1

        lst.sort()  # a 기준으로 정렬
        min_b = float('inf')
        cnt = 0

        for _, b in lst:
            if b < min_b:
                cnt += 1
                min_b = b

        results.append(str(cnt))

    print("\n".join(results))


# Reading all input data at once
data = input().strip().splitlines()
process_case(data)

