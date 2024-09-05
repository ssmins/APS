
T, n = map(int, input().split())
coin_list = sorted(map(int, input().split()), reverse=True)
dptable = [T] * (T+1) # T 인덱스까지 필요하니까
# 해당 가격까지 가는 데 최소한으로 필요한 동전 갯수를 저장할 dptable
for x in coin_list:
    dptable[x] = 1

for i in range(len(dptable)): # 0부터 T까지의 인덱스를 가진 dptable 안에서 돌 것
    for j in coin_list:
        if i > j and dptable[i-j] != 0 :
            dptable[i] = min(dptable[i], 1 + dptable[i-j])

print(dptable[T])

'''
for i in range(n):
    while T >= coin_list[i]:
        T -= coin_list[i]
        count[i] += 1

if T == 0 and sum(count) >= 1 :
    print(sum(count))
else:
    print('impossible')
'''
# 수환 찬스
# 가치가 정해져 있으니까, 최대 가치만큼의 길이를 가진 dptable을 만들고 거기다가 최적해를 집어넣으면서 dp로 풀기
