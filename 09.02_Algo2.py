
# 중위순회하면서 만난 것들을 code에 차례대로 저장
def inorder(node, arr):
    global code
    if node > len(arr)-1: # 인덱스를 벗어나면
        return

    inorder(node*2, arr) # 좌
    code.append(arr[node]) # 중
    inorder(node*2+1, arr) # 우


T = int(input())
for testcase in range(1, T+1):
    N = int(input()) # 문자열의 길이
    arr = list(input()) # 문자열 - 영문자와 숫자로만 구성
    result = []

    for i in arr:

        # 문자열로 들어온 문자 하나하나를 이진수로 변환
        ASCII = bin(ord(i))
        tree = [0]

        # 이진수로 변환한 각각의 값을 트리에 차례로 넣기 == 이진수 각 요소 리스트로 만들기
        for j in range(2, len(ASCII)):
            tree.append(ASCII[j])

        # 그 트리를 중위순회해서 도달한 노드의 값들을 차례로 넣을 리스트 code
        code = []

        # 문제의 조건에 맞는 함수 실행
        inorder(1, tree)

        # 함수의 결과값을 한 테스트케이스에서 함께 출력하기 위해 result에 저장
        result.append(''.join(code))

    print(f'#{testcase}', *result)

'''
3
1
A
3
ABC
5
HELLO
'''

'''
# 강사님 코드
# 문자를 ---> 아스키코드 ---> 2진수로 바꾸는 함수
def change_bin(char):
    ascii = ord(char)
    # 0b0011000 ---> 001100 ---> 00001100 ---> 0001100
    binary = bin(ascii)[2:].zfill(8)[1:]
    return binary

# 중위순회 하는 함수
def inorder(node, tree):
    if node > 7:
        return ''
    # 왼쪽자식 -> 현재노드 -> 오른쪽자식 순회
    return(inorder(node * 2, tree) + tree[node] + inorder(node * 2 + 1, tree))

# 암호화하는 함수
def encryption(char):
    # 이진수로 변환
    binary = change_bin(char)
    # tree 초기화
    tree = ['0'] * 8
    for i in range(7):
        tree[i + 1] = binary[i]
    # tree를 중위순회
    return inorder(1, tree)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    string = input()
    # string 순회 하면서 암호화
    encrypted = [encryption(char) for char in string]
    print(f'#{tc}', *encrypted)
'''