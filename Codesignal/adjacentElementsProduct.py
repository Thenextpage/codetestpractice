#printing the largest product of 2 adjacent array elements

#my first solution

def adjacentElementsProduct(inputArray):
    A=[]
    for i in range(len(inputArray)-1):
        product=inputArray[i+1]*inputArray[i]
        print (product)
        A.append(product)
    return(max(A))a
    
#others solution (code by salevin)

def adjacentElementsProduct(inputArray):
   return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])

