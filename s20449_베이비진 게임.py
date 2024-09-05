
# 베이비진 게임

def is_run(lst):
    global state
    # 어떤 리스트를 받고, 그 안의 원소들로 run 규칙을 만족시킬 수 있나?
    for i in range(len(lst)):
        for j in range(len(lst)):
            for l in range(len(lst)):
                if i != j and i != l and j != l:
                    if lst[i] +1 == lst[j] and lst[i] +2 == lst[l]:
                        state = True

def is_triplet(lst):
    global state
    # 어떤 리스트를 받고, 그 안의 원소들로 triplet 규칙을 만족시킬 수 있나?
    for i in range(len(lst)):
        for j in range(len(lst)):
            for l in range(len(lst)):
                if i != j and i != l and j != l:
                    if lst[i] == lst[j] and lst[i] == lst[l]:
                        state = True

T = int(input())
for testcase in range(1, T+1):
    arr = list(map(int, input().split()))
    a = []
    b = []

    # 각 사람에게 어떤 카드가 주어지는지
    for i in range(len(arr)//2):
        a.append(arr[2*i])
        b.append(arr[2*i+1])

    # 카드가 주어지고, run이나 triplet이 되는지 확인하기
    result = 0
    state = False
    for j in range(3, len(arr)//2 + 1): # 3장 모였을 때부터(idx : 2),  len(arr)//2 인덱스까지 봐야 하니까.
        is_run(a[:j])
        is_triplet(a[:j])
        if state == True:
            result = 1
            break

        is_run(b[:j])
        is_triplet(b[:j])
        if state == True:
            result = 2
            break

    print(f'#{testcase} {result}')

'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
'''

'''
#1 0
#2 1
#3 2
'''

'''
10
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
1 5 5 2 5 3 2 9 8 0 1 3
5 0 5 7 9 3 2 3 1 4 1 6
9 8 4 2 9 4 3 8 7 9 7 7
7 6 3 8 4 8 5 8 2 3 9 4
2 2 5 2 8 3 6 2 7 8 0 6
1 3 5 4 1 2 0 9 0 7 4 1
5 4 5 0 7 6 9 9 4 3 5 2
'''

'''
#1 0
#2 1
#3 2
#4 0
#5 0
#6 2
#7 1
#8 2
#9 2
#10 1
'''

# a = [0, 1, 2, 3, 4, 5, 6]
# print(a[:2]) # [0, 1]
