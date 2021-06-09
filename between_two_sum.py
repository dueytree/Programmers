# 두 정수 사이의 합
# programmers.co.kr/learn/courses/30/lessons/12912

# a와 b의 크기에 대해 조건문을 사용하고 반복문을 통해 합을 구한다.

def solution(a, b):
    answer = 0
    if a == b:
        return a
    elif a < b:
        for i in range(a, b + 1):
            answer += i
    elif a > b:
        for i in range(b, a + 1):
            answer += i
    return answer

def test_solution():
    assert solution(3, 5) == 12
    assert solution(3, 3) == 3
    assert solution(5, 3) == 12