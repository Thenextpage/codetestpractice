#my first attempt solution. hidden test execution time exceeded. 

def almostIncreasingSequence(sequence):
    count=0
    for i in range(len(sequence)):
        list=sequence[:i]+sequence[i+1:]
        if sorted(list)==list:
            for j in range(len(list)-1):
                if list[j]==list[j+1]:
                    count-=1
                    break
            count+=1
    if count>0:
        return True
    else:
        return False


#one of upvoted solutions

def almostIncreasingSequence(sequence):
  f1 = sum([1 for a, b in zip(sequence[:-1], sequence[1:]) if a>=b ]) <= 1     
  f2 = sum([1 for a, c in zip(sequence[:-2], sequence[2:]) if a>=c ]) <= 1    
  return f1 and f2
