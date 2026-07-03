class Solution:
    def minAnd2ndMin(self, arr):
        # code here
        n = len(arr)
        arr.sort()
        first = arr[0]
        
        for i in range(1,n):
            if arr[i] != first:
                return [first,arr[i]]
            
        
        return [-1]
        
