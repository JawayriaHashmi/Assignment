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
for x in processes:
	while(ready==[]):
		j=i
		while( i<len(processes) and clock>=processes[i]["Arrival"] ):
			ready.append(processes[i])
			if(i<len(processes)):
				i=i+1
			
		if(j==i):
			clock=clock+1
	
	ready.sort(key=myfunc1)
	clock=clock+ready[0]["Burst"]
	temp={"Process is ":ready[0]["Process"],"Turnaround Time":clock-ready[0]["Arrival"]}
	tt.append(temp)
	ready.pop(0);
sum=0	
for x in tt:
	sum=sum+x["Turnaround Time"]
	print(x)

print("Average turnaround time= "+str(sum/len(tt)))
