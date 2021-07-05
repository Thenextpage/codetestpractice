#first try

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
import itertools

def solution(user_id, banned_id):
    candidate = []
    for i in banned_id:
        can = []
        for j in user_id:
            count = 0
            for x in range(min(len(j)-1,len(i)-1)):
                if i[x] == j[x] or i[x] == '*':
                    count += 1
            if count == max(len(j)-1,len(i)-1):
                can.append(j)
        candidate.append(can)
    print(candidate)
    combi = list(itertools.product(*candidate))
    print(combi)
    answer=[tuple(set(tuple(set(list(com))))) for com in combi]
    answer=set(answer)
    ans=0
    for k in answer:
       if len(k) == len(banned_id):
            ans+=1
    return (ans)

print(solution(user_id, banned_id))
