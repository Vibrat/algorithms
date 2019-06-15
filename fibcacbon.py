// Dynamic Programming
cache = {}

def fibc_function(index):
    """
    Calculate ficacbon values

    @important feature DP (Dynamic programming)
    @TimeComplexity O(N)
    @SpaceComplexity O(N)
    """
    if index <= 2:
        return index
    
    if index in cache:
        return cache[index]
    else:
        cache[index] = fibc_function(index-1) + fibc_function(index-2)
        return cache[index]
