class Process:
    __lastId = 1

    def __init__(self, duration, insertTime, priority):
        self.duration = duration
        self.insertTime = insertTime
        self.priority = priority
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
    for proc in procs:
        print("Process ", proc.id, end=": ")
        for i in range(proc.insertTime):
            print(" ", end="")
        for i in range(waitTime - proc.insertTime):
            print("-", end="")
        for i in range(proc.duration):
            print("@", end="")
        print(" ")
        waitTime += proc.duration

def getInput():
    procArray = [] 
    for i in range(1, 5):
        print("Process ", i)
        duration = int(input("Duration: "))
        insertTime = int(input("Time of Insertion: "))
        priority = int(input("Priority: "))
        print(" ")
        p = Process(duration, insertTime, priority) 
        procArray.append(p)
    return procArray

def main():
    processes = getInput()
    newProcs = order(processes)
    ganttFifo(newProcs)

if __name__ == "__main__":
    main()
