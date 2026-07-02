class Solution:
    def countFactors(self, n):
        res = []
        
        for i in range(1, n//2 +1):
            if n % i == 0:
                res.append(i)
                
                
        return len(res) +1
        
        
        