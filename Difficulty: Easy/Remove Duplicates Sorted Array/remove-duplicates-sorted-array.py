class Solution:
    def removeDuplicates(self, arr):
        n = len(arr)

        if n == 0:
            return []

        i = 0

        for j in range(1, n):
            if arr[j] != arr[i]:
                i += 1
                arr[i] = arr[j]

        return arr[:i + 1]