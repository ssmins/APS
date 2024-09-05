''''''

# 화물 도크 == 강의 회의실 배정 문제
'''
T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    doc = [0] * (24 + 1)  # 인덱스 0 ~ 24까지

    # 중복되는 경우 있는지 doc에서 확인
    for _ in range(N):
        s, e = map(int, input().split()) # s : 작업 시작 , e : 작업 끝
        for i in range(s, e):
            doc[i] += 1

    # 구간 동안 중복되는 게 없다면, 결과에 추가하고
    for i in range(e-s): # start, end 보고 그 구간동안의 doc이 다 1이라면?
        if doc[s+i] != 1:


    print(doc)


    # 소요시간 짧은 것부터 ?


    # 빨리 시작하는 것부터?


    # 빨리 끝나는 것부터 ?
'''

'''
# 강사님 코드
# sort - lambda 함수 사용,
def doc(arr):
    # 종료 시간 기준으로 빠른 것부터 정리
    arr.sort(key = lambda x : x[1])
    end = 0 # 마지막 작업 끝난 시간
    cnt = 0 # 화물차 수

    for s, e in arr:
        # 작업 수행했을 때
        if s >= end :
            end = e
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = doc(arr)
    print(f'#{tc} {result}')
'''