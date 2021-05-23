#other peoples solution
def solution(participant, completion): 
  answer = '' 
  temp = 0 
  dic = {} 
  for part in participant: 
    dic[hash(part)] = part 
    temp += int(hash(part)) 
  for com in completion:
    temp -= hash(com) 
    answer = dic[temp] 
  return answer
#the dictionary will keep add the hash with the values like 
#{-4773832577558650225: 'marina'}, {-4773832577558650225: 'marina', 5526818206188338515: 'josipa'}
#and so on. no matter the location of the list the hash value will have the same value if the string values are the same
#so after adding all the hash values in the part and the subtraction of the hash val of comp
#only a single hash val of the failed participant will return
#using the dic[hash value] you can find the answer string

#soultion using the collections(source : https://wooaoe.tistory.com/71)

import collections 
def solution(p, c): 
    p.sort() 
    c.sort() 
    result = collections.Counter(p) - collections.Counter(c)
    return list(result)[0]
  
#import collections 
#lst = ['aa', 'cc', 'dd', 'aa', 'bb', 'ee'] 
#print(collections.Counter(lst))
#>>>Counter({'aa': 2, 'cc': 1, 'dd': 1, 'bb': 1, 'ee': 1})
#using the counter function, you can make a dictionary
#the result will become a form of: Counter({'vinko': 1})
#so you have to use list() for returnig into a string
