class Solution:
    def longestCommonPrefix(self, arr):
        
        # code here
        if len(arr)==0:
            return ""
        result = ""
        base = arr[0]
        for i in range(0,len(base)):
            for word in arr[1:]:
                if i == len(word) or word[i] != base[i]:
                    return result
            
            result += base[i]
        return result
            
