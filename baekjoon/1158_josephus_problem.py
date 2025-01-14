# 요세푸스 문제는 다음과 같다.
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

def solution(n, k):
    arr = [i for i in range(1, n + 1)] # 1부터 n까지의 숫자를 리스트로 생성 (*리스트 컴프리헨션)
    index = k-1 # 처음 제거할 사람의 인덱스
    answer = [] # 제거된 순서를 저장할 리스트
    while arr:
        a = arr.pop(index) # 현재 인덱스의 사람을 제거
        answer.append(a) # 제거된 사람을 결과 리스트에 추가

        if len(arr) != 0: # 남아 있는 사람이 있다면
            index = (index + (k-1)) % len(arr) # 다음 제거할 인덱스를 계산
    print("<", ", ".join(map(str, answer)), ">", sep="")

n, k = map(int, input().split())
solution(n, k)


