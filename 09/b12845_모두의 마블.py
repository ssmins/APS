# 시간 제한 1초
# 점수들이 주어졌을 때, 합치고 합쳐

'''
5
40 10 10 30 10
'''

N = int(input())
level = list(map(int, input().split()))

gold = max(level)*(N-1) + sum(level)-max(level)
print(gold)