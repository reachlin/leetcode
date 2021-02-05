import math

class Solution:
    def myAtoi(self, s: str) -> int:
        negative = False
        capped = False
        state = 0
        rtnNum = 0
        maxInt = math.pow(2,31)
        for i in range(len(s)):
            if state==0:
                # init state
                if s[i]==' ':
                    continue
                if s[i]=='+':
                    state=1
                    continue
                if s[i]=='-':
                    negative = True
                    state=1
                    continue
                if s[i]>='0' and s[i]<='9':
                    state=1
                    rtnNum = int(s[i])
                else:
                    break
            elif state==1:
                if s[i]>='0' and s[i]<='9':
                    rtnNum = rtnNum*10+int(s[i])
                    if rtnNum>=maxInt:
                        capped = True
                        break
                else:
                    break
        if capped:
            if negative:
                rtnNum = 0-maxInt
            else:
                rtnNum = maxInt -1
        else:
            if negative:
                rtnNum = 0-rtnNum
        return int(rtnNum)
