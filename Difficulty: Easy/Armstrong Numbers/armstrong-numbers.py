class Solution:
    def armstrongNumber (self, n):
        # code here 
        total  = 0
        num = n
        nod = len(str(n))
        while num > 0:
            LD= num % 10
            
            total = total + (LD **nod)
            
            num = num // 10
            
        return total == n