''''''
# M명의 조카가 있고, N개의 과자가 있을 때,
# 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 구하라
# 막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있지만 과자를 하나로 합칠 순 없다.
# 과자의 길이는 양의 정수여야 한다.

M, N = map(int, input().split()) # N, M <= 1,000,000 , 시간 제한 1초, -> O(N^2는 안 돼)
lst = list(map(int, input().split()))
# 합칠 수 없고, 자를 수만 있다.
if M <= N : # 조카보다 막대과자의 수가 더 많을 땐, 내림차순으로 정렬하고, M번째의 값만 출력하면 될 텐데
    lst.sort() # O(N)
    print(lst[-M])
    # 의문 1) 시간복잡도가 이게 되는 걸까 ?
    # 의문 2) 그렇지만 긴 막대를 잘라서 줄 수 있다면 -> 
else: # 조카 수보다 막대과자의 수가 더 적을 땐. ->

    # 과자 나눠주기
    # 모든 조카에게 같은 길이의 막대 과자를 나눠줘야 한다.
    # M명의 조카, N개의 과자 , 조카에게 줄 수 있는 막대 과자의 최대 길이
    # 과자를 쪼갤 순 있지만, 과자를 합칠 순 없다.

    def check(start, end, level):
        # 넘어가다 마지막까지 왔다면
        if start == end:
            return cookies[end] // M

        # 다음 단계로 넘길 수 있는 기준은 ?
        # ex. 3 3 ; 10 19 22 (o, 11)
        # ex. 4 4 ; 10 20 25 33 (o, 11)
        elif (cookies[start] + 1) * (level + 2) < cookies[end]:
            return check(start + 1, end, level + 1)

            # 다음 단계로 넘어갈 수 없을 때
        # ex. 3 3 ; 10 19 20 (x, 10)
        # ex. 4 3 ; 20 25 33 (x, 16)
        else:
            if level == 0:
                return cookies[start]
            else:
                return max(cookies[start - 1], cookies[end] // (level + 1))


        # elif cookies[start] >= cookies[end]//(level+2):
        #     if sum(cookies[start:])//M > cookies[start+1]:
        #         return cookies[start+1]
        #     else:
        #         return sum(cookies[start:])//M
        # else:
        #     return check(start+1, end, level+1)



    M, N = map(int, input().split())
    cookies = list(map(int, input().split()))
    if M > N and sum(cookies) < M:
        print(0)
    else:
        # 뒤에서 M번째 길이 보고, 제일 큰 거를 M보다 더 큰 조각으로 나눌 수 없으면 M이 최대,
        start_idx = N - M
        end_idx = N - 1
        result = check(start_idx, end_idx, 0)
        print(result)
