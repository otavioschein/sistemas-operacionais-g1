class Process:
    __lastId = 1

    def __init__(self, duration, insertTime, name = 1):
        self.duration = duration
        self.insertTime = insertTime
        self.id = Process.__lastId
        self.array = []
        if name == 1: Process.__lastId += 1

class ProcPriority(Process):
    def __init__(self, duration, insertTime, priority):
        Process.__init__(self, duration, insertTime)
        self.priority = priority
        self.chart = ""

def order(procs):
    ordArray = []
    for i in range(len(procs)):
        smallest = 0
        for j in range(1, len(procs) ):
            if procs[j].insertTime < procs[smallest].insertTime:
                smallest = j
        ordArray.append(procs.pop(smallest))
    return ordArray

# sjf and round-robin
def appendProcess(queue, count, aptQueue):
    for i in queue:
        if count == i.insertTime:
            if i not in (aptQueue):
                aptQueue.append(i)
    return aptQueue
# SJF and round-robin
def printChart(queue):
    print()
    for i in queue:
        print('Process ', i.id, end=':|')
        for j in i.array:
            print(j, end="")
        print()

# get input for all the algorithms
def getInput(amount, option):
    procArray = [] 
    sumOfTime = 0
    for i in range(amount):
        print("")
        print("Process ", i + 1)
        duration = int(input("Duration: "))
        insertTime = int(input("Time of Insertion: "))
        sumOfTime += duration
        if sumOfTime > 80:
            print(" ")
            print("You've reached the maximum time of duration! The last process will be killed.")
            return procArray
        if option in [1, 3, 4]:
            p = Process(duration, insertTime)
        elif option == 2:
            priority = int(input("Priority: "))
            p = ProcPriority(duration, insertTime, priority) 

        procArray.append(p)
    return procArray

# FIFO
def ganttFifo(procs):
    waitTime = procs[0].insertTime
    print("")
    for proc in procs:
        print("Process ", proc.id, end=":|")
        for i in range(proc.insertTime):
            print(" ", end="")
        for i in range(waitTime - proc.insertTime):
            print("-", end="")
        for i in range(proc.duration):
            print("=", end="")
        print(" ")
        waitTime += proc.duration

# PRIORITY FIFO
class PriorityFifo:
    def __init__(self, fifo):
        self.queue = fifo 

    def getQueue(self):
        return self.queue

    def isEmpty(self):
        for proc in self.queue:
            if proc.duration > 0: 
                return False
        return True

    def insert(self, data):
        self.queue.append(data)

    def setChar(self, currTime):
        try:
            max = -1 
            for i in range(len(self.queue)):
                if self.queue[i].duration > 0:
                    if self.queue[i].insertTime <= currTime: 
                        if max == -1: 
                            max = i
                        self.queue[i].chart += "-"

                        if self.queue[i].priority > self.queue[max].priority:
                            max = i
                    else:
                        self.queue[i].chart += " "

            if max != -1:
                self.queue[max].chart = self.queue[max].chart[:-1]
                self.queue[max].chart += "="
                self.queue[max].duration -= 1

        except IndexError:
            print()
            exit()


def ganttPriority(procs):
    totalDuration = procs.getQueue()[0].insertTime
    for proc in procs.getQueue():
        totalDuration += proc.duration
    print("")
    for i in range(totalDuration):
        procs.setChar(i)

    for proc in procs.getQueue():
        print("Process ", proc.id, ":|", proc.chart)

# SJF
def bubbleSortByDuration(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j].duration > array[j+1].duration:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def executionSJF(dataArray, executingProcess): # where the magic happens
    readyArray = [] # array of completed processes
    aptQueue = []
    totalDuration = dataArray[0].insertTime
    count = 0
    timeExecution = 0
    for x in dataArray: # to get empty spaces in the chart, at the beggining of the process
        for y in range(x.insertTime):
            x.array.append(" ")
    for k in dataArray:
        totalDuration += k.duration  
    while count < totalDuration:
        aptQueue = appendProcess(dataArray, count, aptQueue)
        aptQueue = bubbleSortByDuration(aptQueue) 
        try:
            timeExecution = aptQueue[0].duration + count
            executingProcess = aptQueue[0] 
            del aptQueue[0] # that process is not needed anymore in this queue
            while count < timeExecution:
                executingProcess.array.append("=") # symbol that a process is executing
                for l in aptQueue:
                    l.array.append("-") # symbol that a process is apt but not executing
                count += 1
                aptQueue = appendProcess(dataArray, count, aptQueue)
            readyArray.append(executingProcess)
            aptQueue = bubbleSortByDuration(aptQueue)
        except:
            count += 1
    printChart(readyArray)

# Round-Robin
def executionRoundRobin(dataArray, quantum, executingProcess): # where the magic happens
    readyArray = [] # array of completed processes
    aptQueue = [] 
    count = 0
    done = False # represents a completed process
    timeExecution = 0
    totalDuration = dataArray[0].insertTime
    for x in dataArray: # to get empty spaces in the chart, at the beggining of the process
        for y in range(x.insertTime):
            x.array.append(" ")
    for i in dataArray: # get a number of the sum of all processes's duration
        totalDuration += i.duration
    while count < totalDuration: 
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
                executingProcess.duration -= 1
                aptQueue = appendProcess(dataArray, count, aptQueue)
                if executingProcess.duration == 0:
                    done = True
                    readyArray.append(executingProcess)
            if not done:
                aptQueue.append(executingProcess)
        except:
            count += 1
    printChart(readyArray) 

# MAIN
def main():
    option = 0
    amountProcesses = 11
    gameOver = 1

    while option not in [1, 2, 3, 4]:
        option = int(input("Choose the algorithm, FIFO (1), PRIORITY FIFO (2), SJF (3), ROUND-ROBIN (4). "))
    print("")
    if option == 1:
        print('Welcome to the FIFO algorithm!')
        while amountProcesses > 10:
            amountProcesses = int(input('How many processes will it be? 10 processes is the maximum: '))
        processes = getInput(amountProcesses, option)
        newProcs = order(processes)
        ganttFifo(newProcs)
    elif option == 2:
        print('Welcome to the Priority FIFO algorithm!')
        while amountProcesses > 10:
            amountProcesses = int(input('How many processes will it be? 10 processes is the maximum: '))
        processes = getInput(amountProcesses, option)
        newProcs = order(processes)
        priorityProcs = PriorityFifo(newProcs)
        ganttPriority(priorityProcs)
    elif option == 3:
        executingProcess = Process(0, 0, 0)
        print('Welcome to the SJF non preemptive algorithm!')
        while amountProcesses > 10:
            amountProcesses = int(input('How many processes will it be? 10 processes is the maximum: '))
        dataArray = getInput(amountProcesses, option)
        newArray = order(dataArray)
        executionSJF(newArray, executingProcess)
    elif option == 4:
        executingProcess = Process(0, 0, 0)
        print('Welcome to the Round-Robin algorithm!')
        while amountProcesses > 10:
            amountProcesses = int(input('How many processes will it be? 10 processes is the maximum: '))
        quantum = int(input('Inform the quantum: '))
        dataArray = getInput(amountProcesses, option)
        newArray = order(dataArray)
        executionRoundRobin(newArray, quantum, executingProcess)

    print("")
        

if __name__ == "__main__":
    main()
