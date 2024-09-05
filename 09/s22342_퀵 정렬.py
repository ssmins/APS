

# 퀵 정렬로 N개의 주어진 정수 정렬, 그 리스트의 N//2 인덱스 값을 출력하기

def quick_sort(arr):
    # quick sort는 어떤 pivot 값을 정하고, 그 값보다 작은 값, 큰 값을 나누는 정렬

    if len(arr) <= 1:
        return arr

    # pivot 값을 항상 리스트 맨 앞에 있는 값으로 하기로 결정
    pivot = arr[0]
    # pivot 값보다 작은 값들 나열
    lessthan = [x for x in arr if x < pivot]
    samefor = [x for x in arr if x == pivot]
    betterthan = [x for x in arr if x > pivot]

    return quick_sort(lessthan) + samefor + quick_sort(betterthan)


T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    quicksorted_list = quick_sort(lst)
    print(f'#{testcase} {quicksorted_list[N//2]}')