def solution(my_string):
    arr = []
    for x in my_string:
        if x < 'A':
            arr.append(int(x))
    return sum(arr)

