class Solution:
    def convert(self, s: str, numRows: int) -> str:
        outstr = {}
        row = 0
        col = 0
        direction = 0 # 0 down, 1 up
        for i in range(len(s)):
            print(direction, row, col)
            if direction == 0: # down 0
                if row < numRows:
                    nrow = row
                    ncol = col
                    row += 1
                else:
                    direction = 1
                    row = numRows -2
                    col += 1
                    if row<0:
                        row = 0
                    nrow = row
                    ncol = col
                    row -=1
                    if row<0:
                        row = 1
                        direction = 0
                    col +=1
            else: # up 1
                if row >=0:
                    nrow = row
                    ncol = col
                    row -= 1
                    if row<0:
                        row=1
                        direction=0
                    col +=1
                else:
                    direction = 0
                    row = 1
                    col -= 1
                    nrow = row
                    ncol = col
                    row +=1
                    
            print(direction, nrow, ncol, s[i], row, col)
            if nrow in outstr:
                outstr[nrow]+=s[i]
            else:
                outstr[nrow]=s[i]
        rtnstr = ""
        for i in range(len(outstr)):
            if outstr[i] != "":
               rtnstr+=outstr[i]
        return rtnstr
