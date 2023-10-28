from utils.substitutionDP import DPTable
import matplotlib.pyplot as plt




# Create tree structure
a = "TGGAATTCTCGGGTGCCAAGGAACTCCAGTCACACAGTGATCTCGTATGCCGTCTTCTGCTTG"
PERCENT = 10
LIMIT = 100000
table = DPTable(PERCENT/100, a)
lines = open("data\\s_3_sequence_1M.txt").read().splitlines()
if LIMIT == -1 or LIMIT > len(lines):
    LIMIT = len(lines)

lengthSum = 0

lengthList = []
lenList = []

lineLength = len(lines[1])
for i in range(lineLength+1):
    lengthList.append(0)


i = 0
print()
for line in lines[:LIMIT]:
    col = table.GASolve(line)
    matchString = table.getCommonString()
    #print(matchString)
    lengthSum += len(matchString)
    lengthList[len(matchString)] += 1
    lenList.append(lineLength - len(matchString))
    i += 1
    if i % (LIMIT/10) == 0:
        print(str(i) + " of " + str(LIMIT))

#lengthList = [length/len(lines) for length in lengthList]
print("Sequences found: " + str((LIMIT-lengthList[0])))
print("Sequence lengths after adapter match removal:")
for length in range(len(lengthList)):
    if length != 0 and lengthList[length] != 0:
        print("Length: " + str(lineLength - length) + ", num: " + str(lengthList[length]))
print(lengthList)


plt.hist(lenList, bins=range(-0, 52))
plt.xlabel("Sequence length in nucleotides")
plt.ylabel("Frequency count")
plt.savefig("task2\\GA" + str(PERCENT) + "seqLengths.png")
plt.show()
