class Solution:
    def largest(self, arr):
        # code here
        # largest = arr[0]
        # n = len(arr)
        
        # for i in range(0,n):
        #     if arr[i] > largest:
        #         largest = arr[i]
                
        # return largest
        n = len(arr)
        # largest = arr[0]
        arr.sort()
        for i in range(0,n):
            return arr[n-1]
