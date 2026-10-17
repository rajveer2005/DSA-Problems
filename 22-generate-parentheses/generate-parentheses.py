class Solution(object):

    def solve(self,index,total,brac,res):
        if index >= len(brac):
            if total == 0:
                res.append("".join(brac))
            return

        if total > len(brac) // 2:
            return 

        if total < 0:
            return

        brac[index] =  "("
        sum = total + 1
        self.solve(index+1,total+1,brac,res)

        brac[index] = ")"
        sum = total -1 
        self.solve(index+1,total-1,brac,res)

    def generateParenthesis(self, n):
        brac = [""] * (n * 2)
        res = []
        self.solve(0,0,brac,res)
        return res
 

        