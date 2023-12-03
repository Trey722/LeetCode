

def turnArray_Dict(nums):
    dictionary = {x: x in nums for x in nums}

    return dictionary 


def getIndexDict(nums):
    findIndex = {}
    for i in range(len(nums)):
        findIndex[nums[i]] = i 
        
    return findIndex
        


def sums(nums, target):
    table = turnArray_Dict(nums)
    findIndex = getIndexDict(nums)
    
    
    for i in range(len(nums)):
        searchNum = target - nums[i]
        if (table.get(searchNum) == True):
            if (i == findIndex[searchNum]): # This is added to make sure that you don't get the same index twice
                continue
            return [i, findIndex[searchNum]]
        
        
    return -1 




    

    
    
    




