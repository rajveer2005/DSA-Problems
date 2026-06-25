class Solution:
    # Complete the below function
    def twoSum(self,arr, target):
        # Your code here
        n = len(arr)
        hashmap = {}
        for i in range(0,n):
            remaining = target-arr[i]
            
            if remaining in hashmap:
                return [remaining,arr[i]]
            hashmap[arr[i]] = i
            
            
        return []