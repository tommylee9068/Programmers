def solution(todo_list, finished):
    answer = []
    for a ,b in enumerate(finished):
        if b == False:
            answer.append(todo_list[a])
    return answer
    
    
    # answer = []
    # return answer