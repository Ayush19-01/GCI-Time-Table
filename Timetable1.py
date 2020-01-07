import random
import plotly.graph_objects as go
import time
print("""Welcome to School Time-Table Generator
Before continuing please keep this in mind that this problem is NP-Complete
In a nutshell one needs to explore all possible combinations to find the list of acceptable solutions, due to this 
the code gives output under very specific conditions  for smooth running of the program please try to abide by the following conditions:
1) Assign 2 teachers for each subject
2) Assign ateleast 20 periods for each teacher per week
3) You would be asked to enter names of the teacher 10 times assign different names for less confusion
The program will start in a moment. Please Wait...""")
time.sleep(30)
listofsubs=("Maths","Physics","Chemistry","Biology","Programming")
K=[]
Days=["Monday","Tuesday","Wednesday","Thursday","Friday"]
periods=["Period1","Period2","Period3","Period4"]
classes=["A","B","C","D","E","F"]
Main={"A":{},"B":{},"C":{},"D":{},"E":{},"F":{}}
Main2={}
CA={}
CB={}
CC={}
CD={}
CE={}
CF={}
tchrsM={}
tchrsP={}
tchrsC={}
tchrsB={}
tchrsPr={}
a=10
while a!=0:
    tmp0=input("Enter the name of the teacher:")
    tmp1=input("Subject they teach(Maths=M,Physics=P,Biology=B,Chemistry=C and programming=Pr):")
    tmp2=int(input("Number of periods taken throughout a week:"))
    if tmp1=="P" or tmp1=="p":
        tchrsP[tmp0]=tmp2
        a-=1
    if tmp1=="C" or tmp1=="c":
        tchrsC[tmp0]=tmp2
        a-=1
    if tmp1=="B" or tmp1=="b":
        tchrsB[tmp0]=tmp2
        a-=1
    if tmp1=="Pr" or tmp1=="pr":
        tchrsPr[tmp0]=tmp2
        a-=1
    if tmp1=="M" or tmp1=="m":
        tchrsM[tmp0]=tmp2
        a-=1
def base1():
    for i in Main:
        tmp_2=Main[i]
        for j in Days:
            tmp_list=[0,1,2,3,4]
            tmp_list1=[]
            while len(tmp_list)!=1:
                tmp_1=random.choice(tmp_list)
                tmp_list.remove(tmp_1)
                tmp_3=listofsubs[tmp_1]
                tmp_list1.append(tmp_3)
            tmp_2[j]=tmp_list1
    return Main
Main=base1()
for i in Main:
    tmp4=Main[i]
    for j in tmp4:
        tmp5=tmp4[j]
        tmp10=[]
        for k in tmp5:
            if k=="Maths":
                tmp6=list(tchrsM.keys())
                if i=="A" or i=="B" or i=="C":
                    tmp7=tmp6[0]
                if i=="D" or i=="E" or i=="F":
                    tmp7=tmp6[1]
                tmp8=tchrsM[tmp7]
                tmp8-=1
                tchrsM[tmp7]=tmp8
                if tmp8==0:
                    del tchrsM[tmp7]
                else:
                    tmp11=tmp7+"/"+"Maths"
                    tmp10.append(tmp11)
            if k=="Biology":
                tmp6=list(tchrsB.keys())
                if i == "A" or i == "B" or i == "C":
                    tmp7 = tmp6[0]
                if i == "D" or i == "E" or i == "F":
                    tmp7 = tmp6[1]
                tmp8=tchrsB[tmp7]
                tmp8-=1
                tchrsB[tmp7]=tmp8
                if tmp8==0:
                    del tchrsB[tmp7]
                else:
                    tmp11=tmp7+"/"+"Biology"
                    tmp10.append(tmp11)
            if k=="Physics":
                tmp6=list(tchrsP.keys())
                if i == "A" or i == "B" or i == "C":
                    tmp7 = tmp6[0]
                if i == "D" or i == "E" or i == "F":
                    tmp7 = tmp6[1]
                tmp8=tchrsP[tmp7]
                tmp8-=1
                tchrsP[tmp7]=tmp8
                if tmp8==0:
                    del tchrsP[tmp7]
                else:
                    tmp11=tmp7+"/"+"Physics"
                    tmp10.append(tmp11)
            if k=="Chemistry":
                tmp6=list(tchrsC.keys())
                if i == "A" or i == "B" or i == "C":
                    tmp7 = tmp6[0]
                if i == "D" or i == "E" or i == "F":
                    tmp7 = tmp6[1]
                tmp8=tchrsC[tmp7]
                tmp8-=1
                tchrsC[tmp7]=tmp8
                if tmp8==0:
                    del tchrsC[tmp7]
                else:
                    tmp11=tmp7+"/"+"Chemistry"
                    tmp10.append(tmp11)
            if k=="Programming":
                tmp6=list(tchrsPr.keys())
                if i == "A" or i == "B" or i == "C":
                    tmp7 = tmp6[0]
                if i == "D" or i == "E" or i == "F":
                    tmp7 = tmp6[1]
                tmp8=tchrsPr[tmp7]
                tmp8-=1
                tchrsPr[tmp7]=tmp8
                if tmp8==0:
                    del tchrsPr[tmp7]
                else:
                    tmp11=tmp7+"/"+"Programming"
                    tmp10.append(tmp11)
        tmp4[j]=tmp10
    Main2[i]=tmp4
for i in Main2:
    tmp1=Main2[i]
    mon=tmp1['Monday']
    tue=tmp1['Tuesday']
    wed=tmp1['Wednesday']
    thur=tmp1['Thursday']
    fri=tmp1['Friday']
    fig = go.Figure(data=[go.Table(header=dict(values=['Periods/Days','Monday', 'Tuesday','Wednesday','Thursday','Friday']),
                                   cells=dict(values=[[1,2,3,4],mon,tue,wed,thur,fri ]))])
    fig.update_layout(title="Time-Table for class:"+i)
    fig.show()
    time.sleep(5)
