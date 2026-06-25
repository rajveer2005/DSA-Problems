class Solution(object):
    def rearrangeArray(self, nums):
        pos = []
        neg = []

        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])

        for i in range(len(pos)):
            nums[2 * i] = pos[i]
            nums[2 * i + 1] = neg[i]

        return nums