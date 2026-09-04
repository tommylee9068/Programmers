def solution(strArr):
    answer = []
    counts = [0] * len(strArr)
    for s in strArr:
        counts[len(s)] += 1
    return max(counts)
        #     for i in answer:
#         a.append(answer.count(i))
#     return max(a)
    
    
    # answer = 0
    # return answer