'''
def indexing(x, node):  
    if node > N : 
        return

    if grade[node] == 0: # 비어 있는 자리라면, 
        grade[node] = x # 그 자리에 x값을 할당 
        return

    if x < grade[node]: # 만약 더 작다면 
        indexing(x, node*2) # 왼쪽 자식 노드 탐색 
    elif x > grade[node]: # 크다면 
        indexing(x, node*2+1) # 오른쪽 자식 노드 탐색 

N = int(input()) # 2명씩 추가될건데, 몇 번 추가될건가 
grade = [0, 500] + [0] * (2*N) 
# 전체 추가할 tree 제시, 0번 인덱스 제외, 1번 초기화 2N개의 원소를 새로 받을 거니까 

for _ in range(N): 
    a, b = map(int , input().split())

    # 하나씩 끝 노드에 추가한다. 1번 노드별로 작으면 왼쪽 , 크면 오른쪽에 추가하면서 
    indexing(a, 1)
    indexing(b, 1)
    # [생각이 안 난다] 단순히 작다고 끝, 크다고 끝이 아니라 중간에 바꿔주기도 해야 하는데 흠 


    # 1번 노드를 출력하면 그 중간값이 나올 것 
    print(grade) 
'''

# heapq 사용 -> 왼쪽은 최대힙, 오른쪽은 최소힙 
import heapq

def indexing(x): 
    if x < grade[1]: # less than root 
        heapq.heappush(less_than_grade_heapq, -x) # 최대힙 구현 
        
    if x > grade[1]: # grater than root 
        heapq.heappush(grater_than_grade_heapq, x)


N = int(input())

grade = [0, 500] 
less_than_grade_heapq = []
grater_than_grade_heapq = []

for _ in range(N): 
    a, b = map(int, input().split())
    indexing(a)
    indexing(b)

    # 더 적은 거 두개가 들어왔으면 , 최대힙 루트노드를 전체 루트노드에 할당하고, 원래 있던 루트노드는 보다 큰 최소힙에 heappush
    if len(less_than_grade_heapq) > len(grater_than_grade_heapq): 
        heapq.heappush(grater_than_grade_heapq, grade.pop())
        grade.append((-1)*heapq.heappop(less_than_grade_heapq))

    # 더 큰 거 두개가 들어오면, 최소힙 루트노드를 전체 루트노드에 할당, 원래 루트노드는 heappop 해서 최대힙에 heappush 
    if len(less_than_grade_heapq) < len(grater_than_grade_heapq): 
        heapq.heappush(less_than_grade_heapq, (-1)*grade.pop())
        grade.append(heapq.heappop(grater_than_grade_heapq))
    
    print(grade[-1])
