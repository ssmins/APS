
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = list(input())
    max_count = 1

    for i in range(1, N-1): # 0번 인덱스, N-1번 인덱스 모두 감안하지 않겠다.
        count = 1 # 어떤 인덱스에서 출발할 때 count 초기화
        for k in range(1, N//2 + 1): # 그 인덱스에서 뻗어나갈 수 있는 최대 범위 : N//2
            if 0 <= i-k and i+k <= N-1: # i-k 인덱스는 최대 0까지 될 수 있고, i+k 인덱스는 N-1 인덱스까지
                if arr[i-k] == arr[i+k]:
                    count += 2
                else:
                    break

        if count > max_count:
            max_count = count

    print(f'#{testcase} {max_count}')

'''
3
3
100
5
10101
10
1011011110
'''