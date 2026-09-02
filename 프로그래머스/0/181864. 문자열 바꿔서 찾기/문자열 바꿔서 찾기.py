def solution(myString, pat):
    a = ''
    for i in myString:
        if i == "A":
            a += "B"
        else:
            a += "A"
    if pat in a:
        return 1
    else:
        return 0
    
    
    # answer = 0
    # return answer