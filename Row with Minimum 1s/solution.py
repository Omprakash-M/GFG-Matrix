class Solution:
    def minRow(self,a):
        lowest=999
        index=0
        for x in mat:
            lcount=0
            for i in x:
                if i==1:
                    lcount+=1
            if lcount<lowest:
                lowest=lcount
                index=a.index(x)
        return index+1
