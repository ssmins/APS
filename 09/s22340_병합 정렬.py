
# 이 문제에서 할 일
# 1. 주어진 arr을 정렬하기, -> mergesorted_lst
# 2. 정렬된 arr의 N//2 인덱스 원소 출력하기,
# 3. 오른쪽 원소가 먼저 복사되는 경우의 수 구하기 - count


# 나눈 걸 합치기 -> 합치면서 정렬
# 양 쪽의 리스트를 받아서 , 그걸 하나의 리스트로 합칠 거야
def merge(left, right):
    # 합치고, 정렬한 결과값을 담은 리스트 초기화. 이걸 리턴할거야
    mergesorted_lst = []
    global count # 오른쪽 원소가 먼저 복사되는 경우의 수 구하기

    # left, right 리스트를 받아 최소값부터 앞에 둘거야.
    l, r = 0, 0  # l : left의 인덱스, r : right의 인덱스
    while l <= len(left) -1 and r <= len(right) -1: # l이 끝까지 도달하거나
        if left[l] <= right[r]:  # 맨 앞의 것들을 비교하는데 -> 둘이 같을 때 왼쪽 걸 먼저 빼 줘야. 오른쪽이 남는 경우를 count 하지 않는다.
            mergesorted_lst.append(left[l])
            l += 1
        elif left[l] > right[r]:
            mergesorted_lst.append(right[r])
            r += 1

    # r이 len(arr)에 도달해서 while 문이 끝났을 경우 ?
    if r == len(right): # r == len(right)-1 이 아닌 이유 : r == len(right)에도 하나 넣고, r+=1 이 되기 때문에 !
        count += 1

    mergesorted_lst.extend(left[l:])
    mergesorted_lst.extend(right[r:])

    return mergesorted_lst


# 나누기 함수
def merge_sort(arr):
    # 재귀하면서 받은 arr의 길이가 1 이하라면,
    if len(arr) <= 1:
        return arr

    # 1개 이상의 arr을 받았다면, 정렬해야지

    # 일단 mid를 지정하고
    mid = len(arr) // 2 # index

    # 왼쪽 절반(arr[:mid]), 오른쪽 절반(arr[mid:])을 또 나누자
    # -> arr[mid]를 분리할 필요 없다. 2개의 리스트를 볼 거니까
    # 나눠서 뭐할건데 ? 다시 나누고 나누다 다 나눠지면 나중에 합치면서 연산할겨
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 재귀함수가 다 뽑히고 나서 재귀의 가장 깊숙한 곳까지 가면 ? 뭐할건데
    # 합치면서 정렬하고, 합치면서 정렬된 걸 또 합치면서 정렬하고 .. 그렇게 전체 arr이 될 때까지
    return merge(left, right)


T = int(input())
for testcase in range(1, T+1):
    N = int(input()) # 주어질 정수열의 길이
    arr = list(map(int, input().split())) # 병합 정렬할 정수열
    count = 0 # 문제 조건에 필요한 변수

    sarr = merge_sort(arr)
    print(f'#{testcase} {sarr[N//2]} {count}')

