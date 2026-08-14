class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result  = ""
        hash_map = {}

        for ch in s :
            hash_map[ch] = hash_map.get(ch,0) +1

        for ch, freq in sorted(hash_map.items(),key = lambda x : x[1],reverse = True):
            result += ch*freq
        return result
    
        