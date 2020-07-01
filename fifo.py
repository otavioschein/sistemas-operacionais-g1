class Process:
    __lastId = 1

    def __init__(self, duration, insertTime):
        self.duration = duration
        self.insertTime = insertTime
        self.id = Process.__lastId
        self.chart = ""
        Process.__lastId += 1

def order(procs):
    ordArray = []
    for i in range(len(procs)):
        smallest = 0
        for j in range(1, len(procs) ):
            if procs[j].insertTime < procs[smallest].insertTime:
                smallest = j
        ordArray.append(procs.pop(smallest))
    return ordArray

def ganttFifo(procs):
    waitTime = procs[0].insertTime
    print("")
    for proc in procs:
        print("Process ", proc.id, end=": ")
        for i in range(proc.insertTime):
            print(" ", end="")
        for i in range(waitTime - proc.insertTime):
            print("-", end="")
        for i in range(proc.duration):
            print("=", end="")
        print(" ")
        waitTime += proc.duration

def getInput(amount):
    procArray = [] 
    sumOfTime = 0
    for i in range(amount):
        print("Process ", i)
        duration = int(input("Duration: "))
        insertTime = int(input("Time of Insertion: "))
        sumOfTime += duration
        print(" ")
        if sumOfTime > 80:
            print("You've reached the maximum time of duration! The last process will be killed.")
            return procArray
        p = Process(duration, insertTime) 
        procArray.append(p)
    return procArray

def main():
    amountProcesses = 11
    print('Welcome to the FIFO algorithm!')
    while amountProcesses > 10:
        amountProcesses = int(input('How many processes will it be? 10 processes is the maximum: '))
    processes = getInput(amountProcesses)
    newProcs = order(processes)
    ganttFifo(newProcs)

if __name__ == "__main__":
    main()
