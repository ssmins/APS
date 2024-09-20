import heapq
 

def divide_2(idx): 
    global count
    if idx == 1 : 
        return 
    count += heap[(idx)//2 - 1] 
    divide_2(idx//2) 

T = int(input())
for testcase in range(1, T+1): 
    heap = []
    N = int(input())
    arr = list(map(int, input().split()))

    for i in arr: 
        heapq.heappush(heap, i)
    print(heap)

    count = 0 
    divide_2(N)
    print(f'#{testcase} {count}')