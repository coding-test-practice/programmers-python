def solution(num_list):
    a = [x for x in num_list if x%2==0]
    return [len(a), len(num_list)-len(a)]