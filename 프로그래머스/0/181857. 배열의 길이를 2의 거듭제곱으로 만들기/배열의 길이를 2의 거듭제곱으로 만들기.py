def solution(arr):
    n = 1
    while n < len(arr):
        n *= 2
    # k = n * 2
    if n > len(arr):
        for i in range(n - len(arr)):
            arr.append(0)
        return arr
    else:
        return arr
    # answer = []
    # return answer