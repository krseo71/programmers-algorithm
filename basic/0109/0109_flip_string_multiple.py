# 문자열 my_string과 이차원 정수 배열 queries가 매개변수로 주어집니다.
# queries의 원소는 [s, e] 형태로, my_string의 인덱스 s부터 인덱스 e까지를 뒤집으라는 의미입니다.
# my_string에 queries의 명령을 순서대로 처리한 후의 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, queries):
    s = [*my_string]
    print(s)
    for i, j in queries:
        my_string = my_string[:i] + my_string[i:j+1][::-1] + my_string[j+1:]
    return my_string



    # return my_string

solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]])