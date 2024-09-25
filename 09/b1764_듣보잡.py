''''''
import time

'''
# 두 집합에서 공통되는 문자열 저장하고, 출력하기

from sys import stdin, stdout
input = stdin.readline

N, M = map(int, input().split()) # N : 듣도 , M : 보도

dd = [] # 듣도 못한 사람
for _ in range(N):
    dd.append(input())
bd = [] # 보도 못한 사람
for _ in range(M):
    bd.append(input())

ddbd = [] # 듣도 보도 못한 사람
if N >= M: # M이 더 적으면
    for i in range(M):
        if bd[i] in dd:
            ddbd.append(bd[i])
else:
    for i in range(N):
        if dd[i] in bd:
            ddbd.append(dd[i])

ddbd.sort() # O(N^2)
# print(len(ddbd))
# for j in range(len(ddbd)):
#     print(ddbd[j])
print(len(ddbd))
stdout.write(''.join(ddbd))

# sys 모듈 사용해도, 시간 초과 발생
'''

N, M = map(int, input().split()) # N : 듣도 , M : 보도

dd = [] # 듣도 못한 사람
for _ in range(N):
    dd.append(input())
bd = [] # 보도 못한 사람
for _ in range(M):
    bd.append(input())

ddbd = set() # 듣도 보도 못한 사람
for i in range(M):
    if bd[i] in dd:
        ddbd.add(bd[i])

print(len(ddbd))
for j in range(len(ddbd)):
    result = ddbd.pop()
    print(result)
    