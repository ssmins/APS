
def myorder(node): 
    if node > N: 
        return 

    myorder(node*2)
    myorder(node*2+1)
    tree[node//2] += tree[node] 

T = int(input())
for testcase in range(1, T+1): 
    N, M, L = map(int, input().split())
    tree = [0] * (N+1) # N번 인덱스까지 살려서 사용하려고 

    for _ in range(M): 
        idx, value = map(int, input().split())
        tree[idx] = value

    myorder(1)
    print(f'#{testcase} {tree[L]}')