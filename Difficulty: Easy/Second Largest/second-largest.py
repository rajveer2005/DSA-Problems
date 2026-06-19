class Solution:
    def getSecondLargest(self, arr):
        largest = float("-inf")
        s_largest = float("-inf")
        n = len(arr)

        for i in range(0, n):
            if arr[i] > largest:
                s_largest = largest
                largest = arr[i]
            elif arr[i] > s_largest and arr[i] != largest:
                s_largest = arr[i]

        if s_largest == float("-inf"):
            return -1

        return s_largest