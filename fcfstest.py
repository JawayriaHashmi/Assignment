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

processes.sort(key=myfunc)
clock=processes[0]["Arrival"]
sum=0
tt=[]
check=clock
for x in processes:
	while(clock<x["Arrival"]):
		clock=clock+1
	while((check+x["Burst"]>clock and x["Arrival"]<=check)or (x["Arrival"]+x["Burst"]>clock and x["Arrival"]>check)):
		clock=clock+1

	tt.append(clock-x["Arrival"])
	
	check=clock
	print(clock)
	print(x["Arrival"])

for x in tt:
	sum=sum+x
	print("Turnaround time="+str(x))

print("Average turnaround time= "+str(sum/len(tt)))
