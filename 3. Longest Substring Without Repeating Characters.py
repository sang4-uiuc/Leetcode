# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        start = maxLength = 0
        # a dictionary with keys being the character, and value being the index
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
#                 If it's in there and the start index is <= that index, update start
# to the last seen duplicate's index+1. This will put the start index at just
# past the current value's last seen duplicate. This allows us to have the
# longest possible substring that does not contain duplicates.
                start = usedChar[s[i]] + 1
            else:
#                 If it's not in the usedChars map, we can calculate the longest substring
# seen so far. Just take the current index minus the start index. If that
# value is longer than maxLength, set maxLength to it.
                maxLength = max(maxLength, i - start + 1)
                # Finally, update the usedChars map to contain the current value that we just
                # finished processing.
            usedChar[s[i]] = i

        return maxLength