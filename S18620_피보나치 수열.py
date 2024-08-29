
N = int(input()) # 피보나치 수열에서 N번째 자리의 값을 출력하겠다.
dptable = [0]*N
dptable[0] = 0
dptable[1] = 1
for i in range(2, N):
    dptable[i] = dptable[i-1] + dptable[i-2]
print(dptable[-1])
