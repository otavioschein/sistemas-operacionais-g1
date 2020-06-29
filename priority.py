class Process:
    __lastId = 1

    def __init__(self, duration, insertTime, priority):
        self.duration = duration
        self.insertTime = insertTime
        self.priority = priority
        self.id = Process.__lastId
        self.chart = ""
        Process.__lastId += 1

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
                        self.queue[i].chart += "_"

            if max != -1:
                self.queue[max].chart = self.queue[max].chart[:-1]
                self.queue[max].chart += "@"
                self.queue[max].duration -= 1

        except IndexError:
            print()
            exit()

def order(procs):
    ordArray = []
    for i in range(len(procs)):
        smallest = 0
        for j in range(1, len(procs) ):
            if procs[j].insertTime < procs[smallest].insertTime:
                smallest = j
        ordArray.append(procs.pop(smallest))
    return ordArray

def ganttPriority(procs):
    totalDuration = procs.getQueue()[0].insertTime
    for proc in procs.getQueue():
        totalDuration += proc.duration
    print(totalDuration)
    for i in range(totalDuration):
        procs.setChar(i)

    for proc in procs.getQueue():
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
    priorityProcs = PriorityFifo(newProcs)
    ganttPriority(priorityProcs)

if __name__ == "__main__":
    main()
