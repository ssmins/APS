

# arr을 binary search 하면서 x를 찾을 건데,
# x가 오른쪽 구간에서도, 왼쪽 구간에서도 있을 때 찾기
def binary_search(arr, x):
    global right_site
    global left_site

    if x not in arr:
        return False

    # arr[N//2] = mid, x가 mid에 있으면 조건 충족하고 끝, 찾았다.
    if x == arr[N//2]:
        return True

    # x가 right에 있으면 right_site +=1 하고 다시 찾기,
    if x > arr[N//2]:
        right_site += 1
        binary_search(arr[N//2+1:], x)

    # x가 left에 있으면 left_side +=1 하고 다시 찾기
    if x < arr[N//2]:
        left_site += 1
        binary_search(arr[:N//2], x)


T = int(input())
for testcase in range(1, T+1):
    N, M = map(int, input().split()) # A에 속한 정수의 개수 N, B에 속한 정수의 개수 M
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count = 0
    for x in B:
        left_site = 0
        right_site = 0
        state = False
        count += binary_search(A, x)

        # if state == True:
        #     count += 1

    print(f'#{testcase} {count}')

'''
# 강사님 코드 
def binary_search(target):
    start, end = 0, n - 1
    check = 0 # 왼쪽은 1 오른쪽은 2 내가 정하겠다!!

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == target:
            return True

        elif a[mid] > target:
            # 직전에 왼쪽 방향을 검사 했다 break
            if check == 1:
                break
            check = 1 # 방향을 왼쪽으로 설정
            end = mid - 1

        else:
            if check == 2:
                break
            check = 2 # 방향을 오른쪽으로 설정
            start = mid + 1

    return False

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    result = 0
    for num in b:
        result += binary_search(num)

    print(f'#{tc} {result}')
'''