from tkinter import *
from tkinter.ttk import Notebook
import subprocess
import os
import time




root = Tk()
root.geometry('600x900')
root.title("Process Scheduling Algorithms")


frame2 = Frame(root)
frame2.pack(fill="both")

tableayout = Notebook(frame2)


#tab1 
tab1 = Frame(tableayout)
tab1.pack(fill="both")
prio = []
arr_t = []
b_t = []
def Compute():
    with open('data.osproject.txt','w') as file:
        for _ in arr_t:
            file.write(_.get()+"\t")
        file.write("\n")
        for _ in b_t:
            file.write(_.get()+"\t")
        file.write("\n")
        for _ in prio:
            file.write(_.get()+"\t")
        file.write("\n")

    def GanttOutput(GanttChart):
        firstLine = "|"
        aboveLine = "_"
        underLine = "‾"
        for i in range(0, len(GanttChart)):
            firstLine = firstLine + "P" + str(GanttChart[i]) + "|"

        for i in range(1, len(firstLine)):
            underLine += "‾"
            aboveLine += "_"
        return aboveLine + "\n" + firstLine + "\n" + underLine + "\n" 
    subprocess.call([sys.executable, 'os_project.py','4','6'])
    time.sleep(2)
    subprocess.call([sys.executable, 'MLQS.py','4','6'])
    time.sleep(2)
    Output = ""
    with open('op.txt','r') as f:
        l1 = ['FCFS','SJF',"SRTF", 'PRIORITY','PRIORITY_PREMPTIVE','ROUND_ROBIN','MULTILEVEL_QUEUE_SCHEDULING','HRRN']
        for i in range(7):
            s1 = f.readline()
            s1 = s1.strip().split(' ')
            if i!=6:
                Output = Output + l1[i] + "\n"+ GanttOutput(s1)+"\t\t\t\tWAITING_TIME : "+ f.readline()+"\n"
            else:
                Output = Output + l1[i] + "\n"+ GanttOutput(s1)

    X = Label(root, text=Output)
    X.pack()




for row in range(5):
    for column in range(4):
        if row== 0:
            if column == 0:
                label = Label(tab1,text="ProcessID ")
            elif column == 1:
                label = Label(tab1,text=" Arrival Time")
            elif column==2:
                label = Label(tab1,text=" Burst Time")
            else:
                label = Label(tab1,text=" Priority")
            
            label.config(font=('Arial',14)) 
            label.grid(row=row,column=column, sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column, weight=1)
        else:
            label = Entry(tab1,text="Row "+str(row)+", Column:"+str(column))
            if column == 1:
                arr_t.append(label)
            elif column==2:
                b_t.append(label)
            elif column==3:
                prio.append(label)
            label.grid(row=row,column=column, sticky="nsew",padx=1,pady=1)
            tab1.grid_columnconfigure(column, weight=1)


tableayout.add(tab1 , text="TAB 1")
tableayout.pack(fill="both")
Compute = Button(root, text='Compute', command = Compute)
Compute.pack()
root.mainloop()


