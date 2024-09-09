''''''



# 1) 각 인원을 뽑을 수도 있고, 안 뽑을 수도 있다.
# 2) {3, 3, 4, 7}과 {3, 7, 4, 3}은 같다.
# 결론) 부분집합이구나 -> 비트연산


'''
# 라이브 강사님 코드 

# 시작점 : 0번 점원, 탑의 높이는 0부터 시작
# 끝점(기저조건) : N명의 점원을 탑에 쌓을지 말지 고려 완료

# 명시된 조건 : 모든 점원을 쌓았는데 B 이하인 경우를 고려하지 않았다. 
# - 문제조건에 이게 없으면 B 이하인 answer도 따로 만들어줘야 한다. 

T = int(input())

def recur(cnt, sum_height):
    global answer

    # [가지치기 주의] 기저조건 아래에 둘지, 위에 둘지 확인해봐야 한다.
    # [가지치기] 이미 탑의 높이가 B 이상이면, 더 이상 확인할 필요 X
    if sum_height >= B:
        # B 이상의 탑 중 가장 낮은 것이 정답
        answer = min(answer, sum_height)
        return

    # 탑을 쌓는 데 모든 점원을 고려했는가 ?
    if cnt == N:
        return

    # cnt 번 점원을 탑에 쌓는다
    recur(cnt + 1 , sum_height + heights[cnt])

    # cnt 번 점원을 탑에 쌓지 않는다
    recur(cnt + 1, sum_height)

for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    answer = 1e9 # 1억 , 29억? 29e9 # 점원들을 쌓은 탑 중 B에 가까운 높이 저장
    recur(0, 0)
    print(f'#{tc} {answer - B}')
'''