class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = s
        maxLen = 0
        while len(subs)>0:
            length = self.onepass(subs)
            if maxLen < length:
                maxLen = length
            subs = subs[1:]
        return maxLen
    
    def onepass(self, s: str) -> int:
        wc = {}
        len = 0
        for char in s:
            if char in wc:
                break
            else:
                wc[char] = 1
                len += 1
        return len
