class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        n = len(arr)
        for i in range(0,n):
            hashset = set()
            for j in range(i+1,n):
                third = target -(arr[i]+arr[j])
                if third in hashset:
                    return True
                    
                hashset.add(arr[j])
            
        return False