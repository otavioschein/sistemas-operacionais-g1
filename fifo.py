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

def biggest (procs, currTime, currProc):
    if len(procs) == 2:
        if procs[0].priority > procs[1].priority and procs[0].insertTime >= currTime and procs[0].duration > 0:
            return procs[0]
        else:
            return procs[1]
    sub_max = biggest(procs[1:], currTime, currProc) 
    return procs[0] if procs[0].priority > sub_max.priority and procs[0].insertTime >= currTime and procs[0].duration > 0 else sub_max


def ganttPriority(procs):
    totalDuration = procs[0].insertTime
    for proc in procs:
        totalDuration += proc.duration
    print(totalDuration)
    currentProc = procs[0]
    for i in range(totalDuration):
        currentProc = biggest(procs, i, currentProc)
        for proc in procs:
            if currentProc.id == proc.id and proc.duration > 0:
                proc.chart += "@"
                proc.duration -= 1
            elif proc.insertTime >= i and proc.duration > 0:
                proc.chart += "-"
            else:
                proc.chart += " "

    for proc in procs:
        print("Process ", proc.id, proc.chart)


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
