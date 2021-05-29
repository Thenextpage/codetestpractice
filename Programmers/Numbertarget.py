#popular sol

def solution(numbers, target):
    if numbers == []:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return solution(numbers[1:], target+numbers[0]) + solution(numbers[1:], target-numbers[0])

    
#my similar idea code

def solution(numbers, target):
    num_len = len(numbers)
    res = 0
    def dfs(idx,cnt):
        if idx == num_len:
            if target == cnt:
                nonlocal res #use nonlocal to have outside stuff
                res += 1
                return
            else:
                return
        else:
            dfs(idx+1,cnt+numbers[idx]) # summon this until idx is numlen and go plus1 if target is same
            dfs(idx+1,cnt-numbers[idx])


    dfs(0,0)
    return res
