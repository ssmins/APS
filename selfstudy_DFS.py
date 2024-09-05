
# stack : 후입선출 -> 최근에 들어간 걸 먼저 꺼낸다

# DFS : 깊이 우선 탐색
# - 깊은 곳까지 가서 탐색하고,
# - 더 이상 깊이 들어갈 곳 없을때 옆에 갈 수 있는 노드 있나? 탐색
# 넘어갈 때마다 if used[index] == 0 : used[index] = 1 , stack.append(index)
# 더 이상 갈 곳 없을 때 되돌아가기 stack.pop()
# 옆 지점 탐색 if used[index + 1] == 0 : used[index] = 1, stack.append(index)

def DFS(start, N): # start : 현재 시점의 node, N : 전체 정점 개수
    visited = [0] * (N+1) # 이미 방문한 노드 표시하기 위한 배열
    stack = [] # 경로 저장할 스택
    # 이 자리에 방문해서 어떤 작업을 할지 ex. print(start)
    visited[start] = 1 # 출발 시점에 visited 배열에 기록
    node = start
    while True:
        for nodes in close[node]: # 단방향 연결된 리스트가 담겨 있는 리스트 close
            if visited[nodes] == 0: # 방문하지 않았던 곳이어야,
                # 방문
                visited[nodes] = 1
                stack.append(nodes)

