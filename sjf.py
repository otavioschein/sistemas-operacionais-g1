class objArray:
    def __init__(self, name, startTime, fullTimeProcess, array):
        self.name = name
        self.startTime = startTime
        self.fullTimeProcess = fullTimeProcess
        self.array = array

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

def appendProcess(queue, count, aptQueue):
    for i in queue:
        if count == i.startTime:
            if i not in (aptQueue):
                aptQueue.append(i)
    return aptQueue

def printChart(queue):
    for i in queue:
        print('Process ', i.name, end=': ')
        for j in i.array:
            print(j, end="")
        print()

def executionSJF(dataArray, executingProcess): # where the magic happens
    readyArray = [] # array of completed processes
    aptQueue = []
    totalFullTimeProcesses = dataArray[0].startTime
    count = 0
    timeExecution = 0
    for x in dataArray: # to get empty spaces in the chart, at the beggining of the process
        for y in range(x.startTime):
            x.array.append(" ")
    for k in dataArray:
        totalFullTimeProcesses += k.fullTimeProcess
    print(totalFullTimeProcesses)    
    while count < totalFullTimeProcesses:
        aptQueue = appendProcess(dataArray, count, aptQueue)
        aptQueue = bubbleSortByFullTimeProcess(aptQueue) 
        try:
            timeExecution = aptQueue[0].fullTimeProcess + count
            executingProcess = aptQueue[0] 
            del aptQueue[0] # that process is not needed anymore in this queue
            while count < timeExecution:
                executingProcess.array.append("=") # symbol that a process is executing
                for l in aptQueue:
                    l.array.append("-") # symbol that a process is apt but not executing
                count += 1
                aptQueue = appendProcess(dataArray, count, aptQueue)
            readyArray.append(executingProcess)
            aptQueue = bubbleSortByFullTimeProcess(aptQueue)
        except:
            count += 1
    printChart(readyArray)

def getInput(amount): # get the main inputs, name, start time, full time and put in an array
    processArray = []
    sumOfTime = 0
    for i in range(amount):
        name = str(input('Name of the process: '))
        startTime = int(input('Time of insertion: '))
        fullTimeProcess = int(input('Duration of the process: '))
        sumOfTime += fullTimeProcess
        if sumOfTime > 80:
            print("You've reached the maximum time of duration! The last process will be killed.")
            return processArray
        array = []
        process = objArray(name, startTime, fullTimeProcess, array)
        processArray.append(process)
        print()
    return processArray

def main(): # Does a loop to get the right number of processes, calls the functions to get the inputs, sort the main array and finally, executes the algorithm.
    amountProcesses = 11
    executingProcess = objArray('', 0, 0, [])
    print('Welcome to the SJF non preemptive!')
    while amountProcesses > 10:
        amountProcesses = int(input('How many processes will it be? 10 processes is the maximum: '))
    dataArray = getInput(amountProcesses)
    newArray = bubbleSortByStartTime(dataArray)
    executionSJF(newArray, executingProcess)

if __name__ == "__main__":
    main()
