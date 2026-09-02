def solution(myString):
    a = sorted(myString.split('x'))
    b = []
    for i in range(len(a)):
        if a[i] != "":
            b.append(a[i])
    return b
    
    
 
