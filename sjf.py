def bubbleSortByStartTime(dataArray):
    n = len(dataArray)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if dataArray[j].startTime > dataArray[j+1].startTime:
                dataArray[j], dataArray[j+1] = dataArray[j+1], dataArray[j]
    return dataArray

def bubbleSortByFullTimeProcess(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j].fullTimeProcess > array[j+1].fullTimeProcess:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def executionSJF(dataArray):
    readyQueue = []
    totalFullTimeProcesses = dataArray[0].startTime
    count = 0
    timeExecution = 0
    for k in dataArray:
        totalFullTimeProcesses += k.fullTimeProcess
    print(totalFullTimeProcesses)    
    while count < totalFullTimeProcesses:
        for i in dataArray:
            if count == i.startTime:
                readyQueue.append(i)
        readyQueue = bubbleSortByFullTimeProcess(readyQueue)        
        timeExecution = readyQueue[0].fullTimeProcess + count
        while count < timeExecution:
            print('Process executing: ', readyQueue[0].name)
            count += 1
            for j in dataArray:
                if count == j.startTime:
                    readyQueue.append(j)
        del readyQueue[0]
        readyQueue = bubbleSortByFullTimeProcess(readyQueue)


class objArray:
    def __init__(self, id, name, startTime, fullTimeProcess):
        self.id = id
        self.name = name
        self.startTime = startTime
        self.fullTimeProcess = fullTimeProcess

dataArray = []

#dataArray.append(objArray(1, 'A', 0, 4))
#dataArray.append(objArray(3, 'B', 5, 2))
#dataArray.append(objArray(2, 'C', 2, 3))
#dataArray.append(objArray(4, 'D', 0, 5))

dataArray.append(objArray(1, 'A', 2, 6))
dataArray.append(objArray(3, 'B', 0, 5))
dataArray.append(objArray(2, 'C', 1, 2))
dataArray.append(objArray(4, 'D', 3, 4))

newArray = bubbleSortByStartTime(dataArray)
executionSJF(newArray)