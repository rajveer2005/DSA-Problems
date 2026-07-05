class Solution:
    def bubbleSort(self,arr):
        # code here
        n = len(arr)
        for i in range(n):
            for j in range(n-2,-1,-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1],arr[j]
        
        return arr
        