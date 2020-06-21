import sys

NumOfProcesses = sys.argv[0]
TimeQuantum = sys.argv[1]


def FCFS(NumOfProcesses, BurstTimeList):    
    waitingTime = 0
    GanttChart = []
    for i in range(0, NumOfProcesses):
        for j in range(0, BurstTimeList[i][1]):
            GanttChart.append(BurstTimeList[i][0])
        waitingTime += BurstTimeList[i][1]*(NumOfProcesses-i-1)
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime

def SJFNonPreemptive(NumOfProcesses, BurstTimeList):
    waitingTime = 0
    GanttChart = []
    swapList = []
    for i in range(0, NumOfProcesses):
        c = i
        for j in range(i+1, NumOfProcesses):
            if BurstTimeList[j][1]<BurstTimeList[c][1]:
                c = j
        if c != i:
            swapList         = BurstTimeList[c]
            BurstTimeList[c] = BurstTimeList[i]
            BurstTimeList[i] = swapList
    return FCFS(NumOfProcesses, BurstTimeList)

def SJFPreemptive(NumOfProcesses, BurstTimeList):
    ArrivalTime = []
    ArrivalStatus = []
    waitingTime = 0
    totalTime = 0
    GanttChart = []
    for i in range(0, NumOfProcesses):
        ArrivalTime.append(BurstTimeList[i][2])
        ArrivalStatus.append(False)
        waitingTime -= (BurstTimeList[i][1]+BurstTimeList[i][2])
        totalTime += BurstTimeList[i][1]
    smallestIndex = 0
    smallestValue = totalTime
    for i in range(0, totalTime):
        smallestValue = totalTime
        for j in range(0, NumOfProcesses):
            if i == ArrivalTime[j]:
                ArrivalStatus[j] = True
        for j in range(0, NumOfProcesses):
            if ArrivalStatus[j] and BurstTimeList[j][1] < smallestValue and BurstTimeList[j][1] != 0:
                smallestValue = BurstTimeList[j][1]
                smallestIndex = j
        GanttChart.append(smallestIndex+1)
        BurstTimeList[smallestIndex][1] -= 1
        if BurstTimeList[smallestIndex][1] == 0:
            waitingTime += (i+1)
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime

def PriorityNonPreemptive(NumOfProcesses, BurstTimeList):
    swapList = []
    for i in range(0, NumOfProcesses):
        c = i
        for j in range(i+1, NumOfProcesses):
            if BurstTimeList[j][3]<BurstTimeList[c][3]:
                c = j
        if c != i:
            swapList         = BurstTimeList[c]
            BurstTimeList[c] = BurstTimeList[i]
            BurstTimeList[i] = swapList
    return FCFS(NumOfProcesses, BurstTimeList)

def PriorityPreemptive(NumOfProcesses, BurstTimeList):
    ArrivalTime = []
    ArrivalStatus = []
    waitingTime = 0
    totalTime = 0
    GanttChart = []
    for i in range(0, NumOfProcesses):
        ArrivalTime.append(BurstTimeList[i][2])
        ArrivalStatus.append(False)
        waitingTime -= (BurstTimeList[i][1]+BurstTimeList[i][2])
        totalTime += BurstTimeList[i][1]
        
    smallestIndex = 0
    smallestValue = 30
    for i in range(0, totalTime):
        smallestValue = totalTime
        for j in range(0, NumOfProcesses):
            if i == ArrivalTime[j]:
                ArrivalStatus[j] = True
        for j in range(0, NumOfProcesses):
            if ArrivalStatus[j] and BurstTimeList[j][3] < smallestValue and BurstTimeList[j][1] != 0:
                smallestValue = BurstTimeList[j][3]
                smallestIndex = j
        GanttChart.append(smallestIndex+1)
        BurstTimeList[smallestIndex][1] -= 1
        if BurstTimeList[smallestIndex][1] == 0:
            waitingTime += (i+1)
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime

def RoundRobin(NumOfProcesses, BurstTimeList, TimeQuantum):
    waitingTime = 0
    GanttChart = []
    myLen = 0
    for i in range(0, NumOfProcesses):
        waitingTime -= BurstTimeList[i][1]
    i = 0
    NumOfZeroes = 0
    while True:
        if(BurstTimeList[i][1]==0):
            i = (i+1)%NumOfProcesses
            continue
        if BurstTimeList[i][1]>TimeQuantum:
            BurstTimeList[i][1] -= TimeQuantum
            myLen += TimeQuantum
            for j in range(0, TimeQuantum):
                GanttChart.append(BurstTimeList[i][0])
        else:
            myLen += BurstTimeList[i][1]
            for j in range(0, BurstTimeList[i][1]):
                GanttChart.append(BurstTimeList[i][0])
            BurstTimeList[i][1] = 0
            NumOfZeroes += 1
            waitingTime += myLen
        if NumOfZeroes == NumOfProcesses:
            break
        i = (i+1)%NumOfProcesses
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime




def Input():

    for i in range(0, NumOfProcesses):
        newList = []
        newList.append((i+1))
        BurstTimeList.append(newList)
    ArrivalTime = []
    Priority = []
    with open('data.osproject.txt','r') as file:
        a_t = file.readline()
        a_t = a_t.strip().split('\t')
        ArrivalTime.extend(a_t)
        b_t = file.readline()
        b_t = b_t.strip().split('\t')
        for i in range(0, NumOfProcesses):
            BurstTimeList[i].append(int(b_t[i]))
        for i in range(0, NumOfProcesses):
            BurstTimeList[i].append(int(a_t[i]))
        prio = file.readline()
        prio = prio.strip().split('\t')
        Priority.extend(prio)
        for i in range(0, NumOfProcesses):
            BurstTimeList[i].append(int(prio[i]))

# def EnterBurstTime(BurstTimeList, NumOfProcesses):
#     for i in range(0, NumOfProcesses):
#         x = int(input("Enter the burst time for process "+str(i+1)+" : "))
#         BurstTimeList[i].append(x)

# def EnterArrivalTime(BurstTimeList, NumOfProcesses):
#     for i in range(0, NumOfProcesses):
#         x = int(input("Enter the arrival time for process "+str(i+1)+" : "))
#         BurstTimeList[i].append(x)

# def EnterPriority(BurstTimeList, NumOfProcesses):
#     for i in range(0, NumOfProcesses):
#         x = int(input("Enter the priority for process "+str(i+1)+" : "))
#         BurstTimeList[i].append(x)

def hrrn(BurstTimeList,NumOfProcesses):
    waitingTime = 0
    GanttChart = []
    w_t=[0,0,0,0,0]
    hrrn_l = [0,0,0,0,0]
    for i in range(0,NumOfProcesses):
        for j in range(0,NumOfProcesses):
            w_t[j] = (i-BurstTimeList[j][2])
            if(w_t[j]< 0 or BurstTimeList[j][1]==0):
                hrrn_l[j] = -2.0
            else:
                hrrn_l[j] = (w_t[j]+BurstTimeList[j][1]) / BurstTimeList[j][1]
    
    for i in range(0,NumOfProcesses):
        BurstTimeList[i].append(hrrn_l[i])
    swapList = []
    print(hrrn_l)
    for i in range(0, NumOfProcesses):
        c = i
        for j in range(i+1, NumOfProcesses):
            if BurstTimeList[j][4]>BurstTimeList[c][4]:
                c = j
        if c != i:
            swapList         = BurstTimeList[c]
            BurstTimeList[c] = BurstTimeList[i]
            BurstTimeList[i] = swapList
    for i in range(0, NumOfProcesses):
        for j in range(0, BurstTimeList[i][1]):
            GanttChart.append(BurstTimeList[i][0])
    waitingTime += BurstTimeList[i][1]*(NumOfProcesses-i-1)
    waitingTime /= NumOfProcesses
    return GanttChart, waitingTime
def GanttOutput(GanttChart):
    firstLine = "|"
    aboveLine = "_"
    underLine = "‾"
    secondLine = "0"
    for i in range(0, len(GanttChart)):
        firstLine = firstLine + "P" + str(GanttChart[i]) + "|"
        if i<10:
            secondLine = secondLine + "  " + str((i+1))
        else:
            secondLine = secondLine + " " + str((i+1))
    for i in range(1, len(firstLine)):
        underLine += "‾"
        aboveLine += "_"
    return aboveLine + "\n" + firstLine + "\n" + underLine + "\n" + secondLine

BurstTimeList = []
Input()
with open('op.txt','w') as file:
    GanttChart, waitingTime = FCFS(NumOfProcesses, BurstTimeList)
    GanttChart = ' '.join(map(str, GanttChart))
    file.write(GanttChart+"\n")
    file.write(str(waitingTime)+"\n")
    GanttChart, waitingTime = SJFNonPreemptive(NumOfProcesses, BurstTimeList)
    GanttChart = ' '.join(map(str, GanttChart))
    file.write(GanttChart+"\n")
    file.write(str(waitingTime)+"\n")
    GanttChart, waitingTime = SJFPreemptive(NumOfProcesses, BurstTimeList)
    GanttChart = ' '.join(map(str, GanttChart))
    file.write(GanttChart+"\n")
    file.write(str(waitingTime)+"\n")
    BurstTimeList = []
    Input()
    GanttChart, waitingTime = PriorityNonPreemptive(NumOfProcesses, BurstTimeList)
    GanttChart = ' '.join(map(str, GanttChart))
    file.write(GanttChart+"\n")
    file.write(str(waitingTime)+"\n")
    BurstTimeList = []
    Input()
    GanttChart, waitingTime = PriorityPreemptive(NumOfProcesses, BurstTimeList)
    GanttChart = ' '.join(map(str, GanttChart))
    file.write(GanttChart+"\n")
    file.write(str(waitingTime)+"\n")
    BurstTimeList = []
    Input()
    GanttChart, waitingTime = RoundRobin(NumOfProcesses, BurstTimeList, TimeQuantum)
    GanttChart = ' '.join(map(str, GanttChart))
    file.write(GanttChart+"\n")
    file.write(str(waitingTime)+"\n")
    BurstTimeList = []
    Input()
    GanttChart, waitingTime = hrrn(BurstTimeList,NumOfProcesses)
    # print(GanttOutput(GanttChart))
    GanttChart = ' '.join(map(str, GanttChart))
    file.write(GanttChart+"\n")
    file.write(str(waitingTime)+"\n")
