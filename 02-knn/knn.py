import numpy as np
import operator as op
import os


# 计算给定点，使用knn后，属于哪个类
def classify0(inX, dataset, labels, k):
    # 取数据集共有多少行
    size = dataset.shape[0]
    # 把inX复制成size次
    diffMat = np.tile(inX, (size, 1)) - dataset
    sqDiffMat = diffMat**2
    # 用sum加和，都生成1xn的矩阵，axis=1表示x轴，axis=0表示y轴
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    # argsort， 默认从小到大排序，返回的是排好序的数组下标
    # [ 1.48660687  1.41421356  0.          0.1       ]
    # [2 3 1 0]
    sortedDistancies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistancies[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    # 参数1：数据集、参数2：按哪一列排序、参数3：升降序
    sortedClassCount = sorted(
        classCount.items(), key=op.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def classify(inX, dataset, labels, k):
    size = dataset.shape[0]
    inX = np.tile(inX, (size, 1))
    diff = inX - dataset
    diff = diff**2
    distance = np.sum(diff, axis=1)
    distance = distance**0.5
    sortedIndex = np.argsort(distance)
    times = {}
    for i in range(k):
        index = sortedIndex[i]
        value = labels[index]
        # print(times[value] times.get(value, 0) + 1)
        # if times.get(value) is None:
        #     times[value] = 0
        times[value] = times.get(value, 0) + 1
    # 按第二列排序
    times = sorted(times.items(), key=op.itemgetter(1), reverse=True)
    return times[0][0]


# classify([1, 1], [[1, 2], [3, 4], [5, 6]], ['A', 'C', 'C'], 3)

# 调用
# cate = classify0([1, 1], dataset, labels, 3)


# 把.txt文件转成矩阵，1列：飞行里程、2列：游戏时间占比、3列：冰淇淋公升数
def file2matrix(filename):
    fr = open(filename)
    lineArr = fr.readlines()
    lineNum = len(lineArr)
    mat = np.zeros((lineNum, 3))
    index = 0
    classLabel = []
    for line in lineArr:
        line = line.strip()
        formatLine = line.split('\t')
        mat[index, :] = formatLine[0:3]
        classLabel.append(np.int(formatLine[-1]))
        index += 1
    return mat, classLabel


# 调用
# mat, label = file2matrix('datingTestSet.txt')


# 把大的数值转换成0-1之间的数
# 把所有的值都转成0-1之间的数，公式为：newVal = (oldVal - min)/(max - min)
def autoNorm(dataset):
    arr = dataset
    minVal = np.min(arr, axis=0)
    maxVal = np.max(arr, axis=0)
    ranges = maxVal - minVal
    normDataset = np.zeros(arr.shape)
    m = arr.shape[0]
    normDataset = arr - np.tile(minVal, (m, 1))
    normDataset = normDataset / np.tile(ranges, (m, 1))
    return normDataset, ranges, minVal


# 调用
# dataset, ranges, minVal = autoNorm(mat)


def datingClassTest():
    mat, labels = file2matrix('datingTestSet2.txt')
    normDS, ranges, minVal = autoNorm(mat)
    count = 100
    diff = 0
    for i in range(count):
        label = classify0(normDS[i, :], normDS, labels, 3)
        if (label != labels[i]):
            diff += 1
    print(diff / count)


# 调用
# datingClassTest()


def img2vector(path, filename):
    fr = open(path + filename)
    lines = fr.readlines()
    count = len(lines)
    returnArr = np.array([])
    for i in range(count):
        line = lines[i]
        line = line.strip()
        # 整体把string转成int
        arr = list(map(int, line))
        # arr = list(line)
        returnArr = np.append(returnArr, arr)
    return returnArr


def handwritingClassTest():
    trainPath = './Ch02/digits/trainingDigits/'
    list = os.listdir(trainPath)
    size = len(list)
    labels = np.array([])
    mats = np.zeros((size, 1024))
    for i in range(size):
        fileName = list[i]
        # 设置label
        fileLabel = fileName.split('_')[0]
        labels = np.append(labels, fileLabel)
        # labels[i, 0] = fileLabel
        # if labels.get(fileLabel) is None:
        #     labels[fileLabel] = 0
        # labels[fileLabel] += 1
        # 设置矩阵
        mat = img2vector(trainPath, fileName)
        mats[i, :] = mat

    testPath = './Ch02/digits/testDigits/'
    mat = img2vector(testPath, '7_80.txt')
    result = classify(mat, mats, labels, 3)
    print(result)


handwritingClassTest()
