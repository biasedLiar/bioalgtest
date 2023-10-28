import numpy as np

class DPTable:
    def __init__(self, percent, string1):
        self.s1 = string1
        self.percent = percent
        self.table = np.array([[]])
        self.s2 = ""



    def GASolve(self, string2):
        self.s2 = string2
        self.table = np.array([[-10000 for i in range(len(self.s2)+1)] for j in range(len(self.s1)+1)])
        for i in range(len(self.s2)+1):
            self.table[0][i] = 0
        for i in range(1, len(self.s1)+1):
            for j in range(i, len(self.s2)+1):
                cost = self.cost(self.s1[i-1], self.s2[j-1])
                prev =  self.table[i-1][j-1]
                self.table[i][j] = prev + cost
        return self.table[:,-1]
    
    def getCommonString(self):
        max = -1
        for i in range(1, len(self.s1)+1):
            if self.table[i,-1] >= 0:
                max = i
        if max > -1:
            return self.s1[:max]
        return ""
    
    def getErrorLocations(self):
        max = -1
        for i in range(1, len(self.s1)+1):
            if self.table[i,-1] >= 0:
                max = i
        if max > -1:
            myList = [0 for i in range(max)]
            str1 = self.s1[:max]
            str2 = self.s2[len(self.s2) - max:]
            for i in range(max):
                if str1[i] == str2[i]:
                    myList.append(0)
                else:
                    myList.append(1)
            return myList
        return []




    def cost(self, c1, c2):
        if c1 == c2:
            return 1
        return 1 - (1/self.percent)

    


