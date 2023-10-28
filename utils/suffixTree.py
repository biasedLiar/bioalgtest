
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def createChild(self, value, needsEndNode):

        newChild = TreeNode(value)
        #if needsEndNode:
            #newChild.addEndNode()
        self.children.append(newChild)
        return newChild

    def createChildInMiddleOfString(self, value):
        newChild = TreeNode(value)

        self.children.append(TreeNode(value))
        return newChild
    
    def breakNodeInTwo(self, child, value1, value2):
        self.children.remove(child)

        newChild = self.createChild(value1, False)
        newChild.addAndFollowValue(value2)
        newChild.children.append(child)

        #print("Adding middle after " + value1)
        child.value = child.value[len(value1):]
        return


    
    def addEndNode(self):
        #print("In add endnode")
        self.createChild("$", False)



    def addAndFollowValue(self, value):
        #print("In node '" + self.value + "', value '" + value + "'")
        #print("Children are " + str([child.value for child in self.children]))
        if value == "":
            self.addEndNode()
            return
        for child in self.children:
            #print("Checking against " + child.value)
            if len(value) >= len(child.value) and child.value == value[0:len(child.value)]:
                #print("Skipping to child past " + value[:len(child.value)])
                child.addAndFollowValue(value[len(child.value):])
                return
            else:
                if value[0] == child.value[0]:
                    for i in range(1, len(value)):
                        if value[i] != child.value[i]:
                            #print(value[i] + " != " + child.value[i])
                            self.breakNodeInTwo(child, value[:i], value[i:])
                            return
                    self.breakNodeInTwo(child, value[:len(value)], value[len(value):])
                        
        #print("Creating normal child " + value)
        self.createChild(value, True)

    def createSuffixTreeFor(self, value):  
        for i in range(len(value)):
            self.addAndFollowValue(value[i:] + "$")
            #print()



    def printTree(self):
        self.printNode(0)

    def printNode(self, layers):
        if self.value != "":
            myString = "|"
            for i in range(layers - 1):
                myString += "  |"
            print(myString + "--" + self.value)
        else:
            print(self.value + "root\n|")
        for child in self.children:
            child.printNode(layers + 1)
        if self.value != "":
            print(myString)
    
    def followString(self, value):
        #print("Following string, value is " + value)
        if value == "":
            return (False, "")
        isEndNode = False
        for child in self.children:
            #print("\nChecking child\n" + child.value)
            #print("Checking value\n" + value)
            #print()
            miss = False
            if child.value[0] == "$":
                #print("Found endnode")
                isEndNode = True
            if child.value[0] == value[0]:
                for i in range(1, min(len(value), len(child.value))):
                    if child.value[i] != value[i]:
                        if child.value[i] == "$":
                            #print("Returned here")
                            #print(child.value)
                            #print(value)
                            #print(value[:i])
                            return (True, value[:i])
                        else:
                            #print("Next node")
                            miss = True
                            break
                if miss:
                    continue
                if len(child.value) == len(value) + 1 and child.value[len(value)] == "$":
                    return (True, value)
                if len(child.value) > len(value):
                    return (False, "")
                (successful, nextValue) = child.followString(value[len(child.value):])
                if successful:
                    return (True, value[:len(child.value)] + nextValue)
        #print("Failed here")
        if isEndNode:
            return (True, "")
        return (False, "")
    
                    

    
                        