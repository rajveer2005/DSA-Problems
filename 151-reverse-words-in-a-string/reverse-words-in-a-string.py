class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # words = s.split()
        # words.reverse()
        # result = " ".join(words)
        # return result
    # class Solution:
    # def reverseWords(self, s: str) -> str:
        words = s.split()          # Step 1: Split string into words, removes extra spaces
        res = []

        # Step 2: Traverse words in reverse order
        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])
            if i != 0:             # Add a space between words
                res.append(" ")

        # Step 3: Join characters into final string
        return "".join(res)
        