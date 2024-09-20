''''''
M, N = map(int, input().split()) # 열의 개수 M개, 열의 개수 N개
Map = [list(input()) for _ in range(N)]

for y in range(N):
    for x in range(M):
        # 해당 점을 기준으로 양 옆이 자기와 다른 지점인가?
        # 그 지점에서 8*8 했을 때, 잘못 칠해진 값이 가장 적은 지점을 고르고, 그 때의 값을 출력한다.
    