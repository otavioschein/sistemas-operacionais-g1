class objArray:
    def __init__(self, name, startTime, fullTimeProcess, array):
        self.name = name
        self.startTime = startTime
        self.fullTimeProcess = fullTimeProcess
        self.array = array

def bubbleSortByStartTime(dataArray):
    n = len(dataArray)
    for i in range(n-1):
        for j in range(0, n - i - 1):
            if dataArray[j].startTime > dataArray[j + 1].startTime:
                dataArray[j], dataArray[j + 1] = dataArray[j + 1], dataArray[j]
    return dataArray

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

def executionRoundRobin(dataArray, quantum, executingProcess): # where the magic happens
    readyArray = [] # array of completed processes
    aptQueue = [] 
    count = 0
    done = False # represents a completed process
    timeExecution = 0
    totalFullTimeProcesses = dataArray[0].startTime
    for x in dataArray: # to get empty spaces in the chart, at the beggining of the process
        for y in range(x.startTime):
            x.array.append(" ")
    for i in dataArray: # get a number of the sum of all processes's duration
        totalFullTimeProcesses += i.fullTimeProcess
    print(totalFullTimeProcesses)
    while count < totalFullTimeProcesses: 
        done = False
        aptQueue = appendProcess(dataArray, count, aptQueue)
        try:
            timeExecution = count + quantum # simulate a quantum
            executingProcess = aptQueue[0]
            del aptQueue[0]
            while count < timeExecution and not done:
                executingProcess.array.append("=") # symbol that a process is executing
                for l in aptQueue:
                    l.array.append("-") # symbol that a process is apt but not executing
                count += 1
                executingProcess.fullTimeProcess -= 1
                aptQueue = appendProcess(dataArray, count, aptQueue)
                if executingProcess.fullTimeProcess == 0:
                    done = True
                    readyArray.append(executingProcess)
            if not done:
                aptQueue.append(executingProcess)
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
        array = []
        sumOfTime += fullTimeProcess
        if sumOfTime > 80:
            print("You've reached the maximum time of duration! The last process will be killed.") 
            return processArray
        process = objArray(name, startTime, fullTimeProcess, array)
        processArray.append(process)
        print()
    return processArray

def main(): # Does a loop to get the right number of processes, calls the functions to get the inputs, sort the main array and finally, executes the algorithm.
    amountProcesses = 11
    executingProcess = objArray('', 0, 0, [])
    print('Welcome to the Round-Robin!')
    while amountProcesses > 10:
        amountProcesses = int(input('How many processes will it be? 10 processes is the maximum: '))
    quantum = int(input('Inform the quantum: '))
    dataArray = getInput(amountProcesses)
    newArray = bubbleSortByStartTime(dataArray)
    executionRoundRobin(newArray, quantum, executingProcess)

if __name__ == "__main__":
    main()
