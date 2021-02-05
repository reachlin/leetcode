class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        rtnstr = ""
        l = len(s)
        for i in range(0,l):
            #print("i:", i)
            if maxlen/2>l-i:
                break
            seed = 0
            while i+seed<l and s[i]==s[i+seed]:
                seed += 1
                if maxlen<seed:
                    maxlen=seed
                    rtnstr=s[i:i+seed]
            step = 0
            while i-step>=0 and i+seed+step<l+1:
                #print(seed)
                #print(i-step, i+seed+step)
                checkstr = s[i-step:i+seed+step]
                #print(checkstr)
                if self.isStringPalindrome(checkstr):
                    if maxlen<len(checkstr):
                        maxlen=len(checkstr)
                        rtnstr=checkstr
                elif step>2:
                    break
                elif len(checkstr)<maxlen:
                    break
                step+=1
        return rtnstr
    
    def isStringPalindrome(self, s: str) -> bool:
        length = len(s)
        if length<=1:
            return True
        rtn = True
        for i in range(length):
            j = length - i - 1
            if j>i:
                if s[i]!=s[j]:
                    rtn = False
                    break
        return rtn
