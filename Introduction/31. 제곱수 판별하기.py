def solution(n):
    for i in range(1, n):
        if n//i == i and n%i == 0:
            return 1
    return 2