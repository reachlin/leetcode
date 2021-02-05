class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        rtnList = []
        if length<3:
            return rtnList
        sNums = sorted(nums)
        numsDict = {}
        for i in range(length):
            if sNums[i] in numsDict:
                numsDict[sNums[i]].append(i)
            else:
                numsDict[sNums[i]] = [i]
        #print(numsDict)
        p = length -1
        n1 = 0
        while p>n1 and sNums[p] >= 0:
            #print(n1, sNums[n1], p, sNums[p])
            if p<length-1 and sNums[p]==sNums[p+1]:
                n1 = 0
                p -= 1
                continue
            if n1+1>=p:
                n1 = 0
                p -= 1
                continue
            if sNums[n1]+sNums[n1+1]+sNums[p]>0:
                n1 = 0
                p -= 1
                continue
            twoSum = int(0 - (sNums[p]+sNums[n1]))
            if twoSum < sNums[n1]:
                # can' t find smaller neg
                n1 = 0
                p -= 1
            else:
                check = False
                if twoSum in numsDict:
                    check = any(item<p for item in numsDict[twoSum])
                if n1+1<p and check:
                    #sNums[n1+1:p]:
                    if [sNums[p], twoSum, sNums[n1]] not in rtnList:
                        rtnList.append([sNums[p], twoSum, sNums[n1]])
                    n1 += 1
                else:
                    n1 += 1
        return rtnList        
