def solution(my_string, queries):
    for s, e in queries:
        if s != 0:
            my_string = my_string[0:s] + my_string[s:e+1][::-1] + my_string[e+1::]
        elif s == 0:
            my_string = my_string[s:e+1][::-1] + my_string[e+1::]
    return my_string
    
    
    # answer = ''
    # return answer