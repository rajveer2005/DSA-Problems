class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        
        sort_s = sorted(s)
        sort_t = sorted(t)

        if sort_s == sort_t:
            return True
        return False
        