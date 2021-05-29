#my solution

def solution(priorities, location):
    answer = 0
    while True:
        print(priorities)
        if priorities[0]!=max(priorities):
            priorities.append(priorities[0])
            priorities.pop(0)
            if location==0:
                location=len(priorities)-1
            else:
                location -=1
        else:
            answer+=1
            if location==0:
                break
            priorities.pop(0)
            location-=1
    return answer
