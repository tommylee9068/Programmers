def solution(a, b):
    if a > b :
        sum1 = 0 
        for i in range(b, a+1):
            sum1 += i
        return sum1

    elif a < b:
        sum2 = 0
        for i in range(a, b+1):
            sum2 += i
        return sum2
    
    else:
        return a
    
    
    
    
    # answer = 0
    # return answer