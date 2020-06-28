def bubbleSortByStartTime(dataArray):
    n = len(dataArray)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if dataArray[j].startTime > dataArray[j+1].startTime:
                dataArray[j], dataArray[j+1] = dataArray[j+1], dataArray[j]
    return dataArray

def appendProcess(queue, count, aptQueue):
    for i in queue:
        if count == i.startTime:
            if i not in (aptQueue):
                aptQueue.append(i)
    return aptQueue    

def executionRoundRobin(dataArray, quantum, executingProcess):
    aptQueue = []
    count = 0
    done = False
    timeExecution = 0
    totalFullTimeProcesses = dataArray[0].startTime
    for i in dataArray:
        totalFullTimeProcesses += i.fullTimeProcess
    print(totalFullTimeProcesses)
    while count < totalFullTimeProcesses:
        done = False
        aptQueue = appendProcess(dataArray, count, aptQueue)
        timeExecution = count + quantum
        executingProcess = aptQueue[0]
        del aptQueue[0]
        while count < timeExecution and not done:
            print('Process executing: ', executingProcess.name)
            count += 1
            executingProcess.fullTimeProcess -= 1
            aptQueue = appendProcess(dataArray, count, aptQueue)
            if executingProcess.fullTimeProcess == 0:
                done = True
        if not done:
            aptQueue.append(executingProcess)
            

class objArray:
    def __init__(self, id, name, startTime, fullTimeProcess):
        self.id = id
        self.name = name
        self.startTime = startTime
        self.fullTimeProcess = fullTimeProcess

dataArray = []

dataArray.append(objArray(1, 'A', 0, 4))
dataArray.append(objArray(3, 'B', 5, 2))
dataArray.append(objArray(2, 'C', 2, 3))
dataArray.append(objArray(4, 'D', 0, 5))

executingProcess = objArray(0, '', 0, 0)

#dataArray.append(objArray(1, 'A', 2, 6))
#dataArray.append(objArray(3, 'B', 0, 5))
#dataArray.append(objArray(2, 'C', 1, 2))
#dataArray.append(objArray(4, 'D', 3, 4))

quantum = 3

newArray = bubbleSortByStartTime(dataArray)
executionRoundRobin(newArray, quantum, executingProcess)