import numpy as np

class ED_DP_Table:
    def __init__(self, percent, string1):
        self.s1 = string1
        self.percent = percent
        self.table = np.array([[]])
        self.s2 = ""



    def GASolve(self, string2):
        self.s2 = string2
        self.table = np.array([[0 for i in range(len(self.s2)+1)] for j in range(len(self.s1)+1)])
        
        for j in range(len(self.s2)+1):
            self.table[0][j] = 0
        for i in range(1, len(self.s1)+1):
            for j in range(0, len(self.s2)+1):

                sub_cost = self.cost(self.s1[i-1], self.s2[j-1])
                sub_prev =  self.table[i-1][j-1]

                
                add_cost = self.addRemoveCost()
                add_prev =  self.table[i][j-1]

                
                rem_cost = self.addRemoveCost()
                rem_prev =  self.table[i-1][j]

                if j != 0:
                    self.table[i][j] = max(max(sub_cost + sub_prev, add_cost + add_prev), rem_cost+ rem_prev)
                else:
                    self.table[i][j] = rem_cost+ rem_prev
                

                self.table[i][j] = max(max(sub_cost + sub_prev, add_cost + add_prev), rem_cost+ rem_prev)

        return self.table[:,-1]
    
    def getCommonString(self):
        max = -1
        for i in range(1, len(self.s1)+1):
            if self.table[i,-1] >= 0:
                max = i
        if max > -1:
            return self.rebuildString(max)
        return ""

    def rebuildString(self, start_i):
        i = start_i
        j = len(self.table[0])-1

        matchString = ""

        while i*j != 0:

            if self.table[i][j] == self.cost(self.s1[i-1], self.s2[j-1]) + self.table[i-1][j-1]:
                matchString = self.s2[j-1] + matchString
                i -= 1
                j -= 1
                continue
            
            if self.table[i][j] == self.table[i-1][j] + self.addRemoveCost():
                if matchString != "":
                    matchString = "_" + matchString
                i -= 1
                continue

            if self.table[i][j] == self.table[i][j-1] + self.addRemoveCost():
                matchString = self.s2[i-1] + matchString
                j -= 1
                continue
        return matchString
    
    def getErrorLocations(self):
        max = -1
        for i in range(1, len(self.s1)+1):
            if self.table[i,-1] >= 0:
                max = i
        if max > -1:
            i = max
            j = len(self.table[0])-1

            matchString = ""
            
            myList = []
            while i*j != 0:

                if self.table[i][j] == self.cost(self.s1[i-1], self.s2[j-1]) + self.table[i-1][j-1]:
                    if self.cost(self.s1[i-1], self.s2[j-1]) < 0:
                        myList.append(1)
                    else:
                        myList.append(0)
                    i -= 1
                    j -= 1
                    continue
                
                if self.table[i][j] == self.table[i-1][j] + self.addRemoveCost():
                    myList.append(2)
                    i -= 1
                    continue

                if self.table[i][j] == self.table[i][j-1] + self.addRemoveCost():
                    myList.append(3)
                    j -= 1
                    continue
            myList.reverse()
            return myList
        return []

    def getSequenceString(self):
        max = -1
        for i in range(1, len(self.s1)+1):
            if self.table[i,-1] >= 0:
                max = i
        if max > -1:
            return self.s2[:max]
        return ""


            


        


    def addRemoveCost(self):
        return 1 - (1/self.percent)

    def cost(self, c1, c2):
        if c1 == c2:
            return 1
        return 1 - (1/self.percent)

    


