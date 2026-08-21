def solution(my_string):
    return sorted([my_string[i::] for i in range(len(my_string))])
     
    #for i in range(len(my_string)):
    #    a.append(my_string[i::])
    #return sorted(a)
    
    
    # answer = []
    # return answer