#my first solution
def solution(board, moves):
    bucket=[0]
    answer=0
    for m in moves:
        print(m)
        for i in range(len(board)):
            if board[i][m-1] !=0:
                if bucket[len(bucket)-1]==board[i][m-1]:
                    del bucket[len(bucket)-1]
                    answer+=1
                else:
                    bucket.append(board[i][m-1])
                board[i][m-1]=0
                break
    return(answer*2).py
  
  #other popular solution
  def solution(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2     
                break

    return answer
