"""
Given n weights and a list of bags that can contains n weights, put n weights into bags (capacity w)
to get the best of total value in knapsack
"""

"""
Solution

In solving this problem there are two cases we need to consider which are 
    - If we can find a optimal subsystem to solve this
    - If there are other but no optimal subsystem to solve this.

This two cases would lead to
    - When target is smaller than a bag => find an optimal subsystem for the suitable bag
    - When target is equal or bigger => find an optimla subsystem for the suitable bag and
      compare with a solution of putting a portion of weights into the current bags and find the rest of weights
      in optimal subsystem

@TimeComplexity O(2^n)
"""

def knapsack_function(index, weights, values, target):
    """

    @index length of bags
    @weights weights of bags consecutively
    @values values of bags consecutivley
    @taget  total target of weights need to be put
    """

    if index <= -1 or target <= 0:
        total_values = 0
        return total_values

    if weights[index] > target:
        total_values = knapsack_function(index-1, weights, values, target)
    else:
        optimal_values = knapsack_function(index-1, weights, values, target)
        unoptimal_values = values[index] + knapsack_function(index-1, weights, values, target-weights[index])
        total_values = max(optimal_values, unoptimal_values)
    
    return total_values

"""
Test Scenario

Target  10
Weights [5, 4, 3, 2, 6]
values  [7, 9, 4, 2 , 10]
Index   4 
return  19
"""
print ("total_values from knapsacks solution", knapsack_function(4, [5,4,3,2,6], [7, 9,4,2,10], 10))
