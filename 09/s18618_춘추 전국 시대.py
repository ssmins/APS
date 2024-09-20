''''''
'''
def find(x):
    if boss[x] == x:
        return x
    return find(boss[x])

def union(x, y):
    if find(x) == find(y): return
    if find(x) < find(y):
        boss[find(y)] = find(x)
    else:
        boss[find(x)] = find(y)

def fight(x, y):
    if find(x) == find(y): return
    Team_x = 0
    Team_x_lst = []
    Team_y = 0
    Team_y_lst = []
    for i in range(len(lst)+1):
        if boss[i] == find(x):
            Team_x += lst[i-1]
            Team_x_lst.append(i)
        elif boss[i] == find(y):
            Team_y += lst[i-1]
            Team_y_lst.append(i)
    # print(f'Team_y :', Team_y)
    # print(Team_y_lst)
    # print(f'Team_x :', Team_x)
    # print(Team_x_lst)
    if Team_x > Team_y: # Team_x 승리
        for j in Team_y_lst:
            boss[j] = 0

    elif Team_x < Team_y: # Team_y 승리
        for j in Team_x_lst:
            boss[j] = 0

    else: # 무승부
        for j in Team_x_lst:
            boss[j] = 0
        for j in Team_y_lst:
            boss[j] = 0

N = int(input()) # 국가의 수
boss = [i for i in range(N+1)]
lst = list(map(int, input().split()))

T = int(input())
for _ in range(T):
    situation, c1, c2 = input().split()
    c1 = ord(c1) - 64
    c2 = ord(c2) - 64 # A 가 1 인덱스에 들어가게 하려고

    if situation == 'alliance':
        union(c1, c2)
    elif situation == 'war':
        # print(boss)
        fight(c1, c2)
        count = 0
        # print(boss)
        for i in range(len(boss)):
            if boss[i]:
                count += 1
        print(count)
'''

'''
7
10 20 30 40 50 60 70
5
alliance A C
alliance G C
alliance D B
alliance D E 
war D G

7
10 20 30 40 50 60 70
5
alliance G C
alliance A C
alliance D E
alliance D B 
war D G

'''

'''
26
10 20 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250 260 
8
alliance A F
alliance A Z 
alliance B E
alliance B Y 
alliance F U 
alliance C K 
war A B
war A K
'''

def find(x):
    if align[x] == x:
        return x
    if align[x] == 0: # 0으로 바꿔버리니까, 더 작은 값을 한다 그랬는데 그럴 필요는 없었네
        return float('inf')
    else:
        align[x] = find(align[x]) # 경로 압축, 재귀로 호출될 때마다 배열에 할당
        return find(align[x])

def union(x, y):
    if find(x) == find(y):
        return
    else:
        align[find(x)] = find(y)
        # if find(x) < find(y):
        #     # 모든 경로에다가 다 집어넣어줘야할거같은데
        #     align[find(y)] = find(x) # 더 작은 숫자에다 근본을 집어넣기
        # else:
        #     align[find(x)] = find(y)

def fight(x, y):
    if find(x) == find(y): return
    else:
        team_x = []
        team_x_sum = 0
        team_y = []
        team_y_sum = 0
        for i in range(N+1): # align 순회할거야
            if align[i] == find(x): # team X
                team_x.append(i) # 나중에 population 인덱스랑 달라
                team_x_sum += population[i-1]
            elif align[i] == find(y):
                team_y.append(i)
                team_y_sum += population[i-1]

        # print(team_x)
        # print(team_y)
        # print(team_x_sum)
        # print(team_y_sum)

        # x가 이길 경우
        if team_x_sum > team_y_sum:
            for j in team_y:
                align[j] = 0
        # y가 이길 경우
        if team_x_sum < team_y_sum:
            for j in team_x:
                align[j] = 0
        # 비길 경우 - 모두 멸망
        if team_x_sum == team_y_sum:
            for j in team_x:
                align[j] = 0
            for k in team_y:
                align[k] = 0

N = int(input())
population = list(map(int, input().split()))
align = [i for i in range(N+1)] # A 가 1부터 인덱스를 사용한다.
T = int(input())
for _ in range(T):
    situation, nationA, nationB = input().split()
    a, b = ord(nationA) - 64, ord(nationB) - 64
    if situation == 'alliance':
        union(a, b)
    elif situation == 'war':
        fight(a, b)
count = 0
for l in range(len(align)):
    if align[l]:
        count += 1
# print(align)
print(count)
