#my solution attempt

def solution(answers):
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    sc=[0,0,0,0]
    
    def longans(m):
        return m*((len(answers)//len(m))+1)
    
    for i in range(len(answers)):
        if answers[i] == longans(a)[i]:
            sc[1]+=1
        if answers[i] == longans(b)[i]:
            sc[2]+=1
        if answers[i] == longans(c)[i]:
            sc[3]+=1
    maxval = max(sc)
    answer=[i for i, j in enumerate(sc) if j == maxval]
    return answer

#popular solution
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
