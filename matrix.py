# python matrix addition

first = [[1, 2, 3],
         [4, 5, 6],
         [2, 3, 4]]

second = [[2, 3, 4],
          [5, 3, 4],
          [3, 2, 4]]

def matrixAddition(first:list, second:list) -> list:
    # matrix total length
    matrixTotalLength = 0
    
    # each element total length of a matrix
    eachElementTotalLength = 0
    
    # matrix add condition check
    try:
        if len(first) == len(second):
            for item1, item2 in zip(first, second):
                if len(item1) == len(item2):
                    eachElementTotalLength = len(item1)
            matrixTotalLength = len(first)
    except:
        raise Exception("check length of each matix for addition priority is verified")
      
    # matrix addition computation
    finalMatrix = [[]for item in range(matrixTotalLength)]
    counter = 0
    for item1, item2 in zip(first, second):
        for Item1, Item2 in zip(item1, item2):
            finalMatrix[counter].append(Item1 + Item2)
        counter += 1
    # returning final matrix
    return finalMatrix

  
  first = [[1, 2, 3],
         [4, 5, 6],
         [2, 3, 4]]

second = [[2, 3, 4],
          [5, 3, 4],
          [3, 2, 4]]
result = matrixAddition(first, second)
print(result)

# output result

[[3, 5, 7], [9, 8, 10], [5, 5, 8]]
