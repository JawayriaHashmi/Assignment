f=open("input")

processes=[]
for x in f:
	temp=x.split()
	ar=int(temp[1])
	burst=int(temp[2])
	record={"Process":temp[0],"Arrival":ar,"Burst":burst}
	processes.append(record)
def myfunc(e):
	return e["Arrival"]

def myfunc1(e):
	return e["Burst"]

processes.sort(key=myfunc)
clock=0
ready=[]
tt=[]
i=0

while(processes!=[]):
	while(i<len(processes) and clock==processes[i]["Arrival"]):
		ready.append(processes[i])
		i=i+1
	ready.sort(key=myfunc1)
	if(ready!=[]):
		if(ready[0]["Burst"]==0):
			temp={"Process is ":ready[0]["Process"],"Turnaround Time":clock-ready[0]["Arrival"]}
			tt.append(temp)
			ready.pop(0)
			processes.pop(0)
			i=i-1
		if(ready!=[]):
			ready[0]["Burst"]-=1
	clock+=1
sum=0	
for x in tt:
	sum=sum+x["Turnaround Time"]
	print(x)

print("Average turnaround time= "+str(sum/len(tt)))


