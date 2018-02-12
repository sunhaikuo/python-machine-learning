import math
dataSet = [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'],
           [0, 1, 'no']]


# 计算熵
def calcShannonEnt(dataSet):
    size = len(dataSet)
    dataLables = {}
    # for i in range(size):
    for row in dataSet:
        # label = dataSet[i][-1]
        label = row[-1]
        dataLables[label] = dataLables.get(label, 0) + 1

    shannonEnt = 0.0
    for i in dataLables:
        val = dataLables[i]
        radio = val / size
        shannonEnt += -radio * math.log(radio, 2)
    print(shannonEnt)


calcShannonEnt(dataSet)
