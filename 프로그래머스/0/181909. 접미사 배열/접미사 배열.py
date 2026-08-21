def solution(my_string):
    a = []
    for i in range(len(my_string)):
        a.append(my_string[i::])
    return sorted(a)
    
    
    # answer = []
    # return answer