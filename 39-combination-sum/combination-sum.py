class Solution(object):

    def solve(self,index,total,subset,nums,target,res):
        if total == target:
            res.append(subset[:])
            return
        elif total > target:
            return
        if index >= len(nums):
            return 
        
        sum = total + nums[index]
        subset.append(nums[index])
        self.solve(index,sum,subset,nums,target,res)
        sum = total
        subset.pop()
        self.solve(index+1,sum,subset,nums,target,res)
        
    def combinationSum(self, candidates, target):
        res = []
        self.solve(0,0,[],candidates,target,res)
        return res
       
        