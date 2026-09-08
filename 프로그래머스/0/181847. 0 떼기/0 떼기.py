def solution(n_str):
    if n_str[0] != '0':
        return n_str
    else:
        i = 0
        while i >= 0:
            if n_str[i] == '0':
                i += 1
            else:
                n_str[i] != '0'
                break
        return n_str[i::]
    
    
    # answer = ''
    # return answer