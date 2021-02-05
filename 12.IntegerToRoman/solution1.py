class Solution:
    def intToRoman(self, num: int) -> str:
        reminder = num
        pos = 1
        rtnStr = ""
        while reminder>0:
            digit = reminder % 10
            reminder = int(reminder/10)
            if pos == 1:
                if digit < 4:
                    rtnStr = "I"*digit
                elif digit == 4:
                    rtnStr = "IV"
                elif digit == 5:
                    rtnStr = "V"
                elif digit >5 and digit<9:
                    rtnStr = "V"+"I"*(digit-5)
                elif digit ==9:
                    rtnStr = "IX"
            elif pos == 2:
                if digit < 4:
                    rtnStr = "X"*digit+rtnStr
                elif digit == 4:
                    rtnStr = "XL"+rtnStr
                elif digit == 5:
                    rtnStr = "L"+rtnStr
                elif digit >5 and digit<9:
                    rtnStr = "L"+"X"*(digit-5)+rtnStr
                elif digit ==9:
                    rtnStr = "XC"+rtnStr               
            elif pos == 3:
                if digit < 4:
                    rtnStr = "C"*digit+rtnStr
                elif digit == 4:
                    rtnStr = "CD"+rtnStr
                elif digit == 5:
                    rtnStr = "D"+rtnStr
                elif digit >5 and digit<9:
                    rtnStr = "D"+"C"*(digit-5)+rtnStr
                elif digit ==9:
                    rtnStr = "CM"+rtnStr                
            elif pos == 4:
                rtnStr = "M"*digit+rtnStr
            pos += 1
        return rtnStr
