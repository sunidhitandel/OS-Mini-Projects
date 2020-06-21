import sys

class Queue:
    def __init__(self, quantum, priority):
        self.quantum = quantum
        self.priority = priority
        self.pro = []
    def isEmpty(self):
        return self.pro == []

    def enqueue(self, pro):
        self.pro.insert(pro.at,pro)

    def dequeue(self):
        return self.pro.pop(0)

    def size(self):
        return len(self.pro)

    def peek(self):
        if self.size()!=0:
            return self.pro[-1]
        return False
class process:
    def __init__(self,at,bt,prio,pid):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.prio = prio
        self.wt = None

    def complition(self,tat):
        self.tat = tat
    def initialization(self,wt):
        self.wt = wt



queues = [ Queue(i*10, i) for i in [5,10,15]]




TimeQuantum = int(sys.argv[2])
ArrivalTime = []
BurstTimeList = []

waitingTime = 0
GanttChart = []
Priority = []
n = int(sys.argv[1])
pro = []
def Input():
    with open('data.osproject.txt','r') as file:
        a_t = file.readline()
        a_t = a_t.strip().split('\t')
        ArrivalTime.extend(a_t)
        b_t = file.readline()
        b_t = b_t.strip().split('\t')
        BurstTimeList.extend(b_t)
        prio = file.readline()
        prio = prio.strip().split('\t')
        Priority.extend(prio)
total_t =0
min_t = 10000
Input()
for i in range(n):
    at = int(ArrivalTime[i])
    if(at<min_t):
        min_t =at
    BurstTimeList[i] = int(BurstTimeList[i])
    Priority[i] = int(Priority[i])
    total_t = BurstTimeList[i] + total_t 
    pro.append(process(at,BurstTimeList[i],Priority[i],i+1))
pro.sort(key=lambda x: x.at)
for p in pro:
    if (p.prio>=1) and (p.prio<5):
        queues[0].enqueue(p)
    elif (p.prio>=5) and (p.prio<10):
        queues[1].enqueue(p)
    else:
        queues[2].enqueue(p)
# queues[0].pro.sort(key=lambda x: x.at)
# queues[1].pro.sort(key=lambda x: x.at)
# queues[2].pro.sort(key=lambda x: x.at)
# for i in range(len(queues[0].pro)):
#     print(f"{queues[0].pro[i].at}  at {queues[0].pro[i].bt} : bt ")
# for i in range(len(queues[1].pro)):
#     print(f"{queues[1].pro[i].at}  at {queues[1].pro[i].bt} : bt ")
# for i in range(len(queues[2].pro)):
#     print(f"{queues[0].pro[i].at}  at {queues[0].pro[i].bt} : bt ")
i,j,k=0,0,0
slot = []
for t in range(0,total_t):

    if(not(queues[0].isEmpty()) and queues[0].pro[0].at <= t):
        if(queues[0].pro[0].wt == None):
            queues[0].pro[0].initialization(t)
        for x in range(queues[0].quantum):
            t+=1
            slot.append(queues[0].pro[0].pid)
            queues[0].pro[0].bt -=1
            if(queues[0].pro[0].bt == 0):
                queues[1].pro[0].complition(t)
                break
        if (queues[0].pro[0].bt != 0):
            queues[0].enqueue(pro[i])
        queues[0].dequeue()
        for i in range(len(queues[0].pro)):
            print(f"{queues[0].pro[i].at}  at {queues[0].pro[i].bt} : bt ")

    elif(not(queues[1].isEmpty()) and queues[1].pro[0].at <= t):
        if(queues[1].pro[0].wt == None):
            queues[1].pro[0].initialization(t)
        slot.append(queues[1].pro[0].pid)
        queues[1].pro[0].bt -=1
        if(queues[1].pro[0].bt == 0):
            queues[1].pro[0].complition(t)
            queues[1].dequeue()

    else:
        slot.append("-")
with open('op.txt','a') as file:
    slot = ' '.join(map(str, slot))
    file.write(slot+"\n")
    file.write(str(waitingTime)+"\n")
