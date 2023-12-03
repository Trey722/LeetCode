

def turnArray_Dict(nums):
    return {num: index for index, num in enumerate(nums)}




def sums(nums, target):
    
    findIndex = turnArray_Dict(nums)
    
    
    for i in range(len(nums)):
        searchNum = target - nums[i]
        if (findIndex.get(searchNum) != None):
            if (i == findIndex[searchNum]): 
                continue
            return [i, findIndex[searchNum]]
        
        
    return -1 


array = [1, 2, 3, 4]

findIndex = {num: index for index, num in enumerate(array)}


print(findIndex[3])

    

    
    
    




