def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i] == True:
            for a in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for b in range(arr[i]):
                answer = answer[:-1:]
    return answer