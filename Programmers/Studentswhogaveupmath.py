#my solution attempt

def solution(answers):
    
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    sc=[0,0,0,0]
    def longans(m):
        return m*((len(answers)//len(m))+1)
    for i in range(len(answers)-1):
        if answers(i) == longans(a)[i]:
            sc[1]+=1
        if answers(i) == longans(b)[i]:
            sc[2]+=1
        if answers(i) == longans(b)[i]:
            sc[3]+=1
    maxval = max(sc)
    answer=[i for i, j in enumerate(a) if j == m]
            
            
        
    return answer
    
print(solution(answers))
