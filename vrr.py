f=open("input")
quantum=0
processes=[]
for x in f:
	temp=x.split()
	if(len(temp)==1):
		quantum=int(temp[0])
	else:
		record={"Process":temp[0],"Arrival":int(temp[1]),"Burst":int(temp[2]),"IO Burst":int(temp[3]),"Const IO Burst":int(temp[3]),"IO Wait":int(temp[4]),"Const IO Wait":int(temp[4]),"Quantum":quantum}
		processes.append(record)
def myfunc(e):
	return e["Arrival"]

processes.sort(key=myfunc)
print(processes)

clock=0
tt=[]
ready=[]
aq=[]
wq=[]
i=0
while(processes!=[]):
	print(clock)
	print(wq)
	for x in wq:
		if(x["IO Wait"]==-1):
			x["IO Burst"]=x["Const IO Burst"]
			x["IO Wait"]=x["Const IO Wait"]
			wq.remove(x)
			if(x["Quantum"]==0):
				ready.append(x)
			elif(x["Quantum"]>0):
				aq.append(x)
	print(wq)
	print("aq")
	print(aq)
	while(i<len(processes) and clock==processes[i]["Arrival"]):
		ready.append(processes[i])
		i=i+1
	print(ready)
	if(aq!=[]):
		while(aq[0]["Quantum"]>0):
			for x in wq:
				if(x["IO Wait"]==-1):
					x["IO Burst"]=x["Const IO Burst"]
					x["IO Wait"]=x["Const IO Wait"]
					wq.remove(x)
					if(x["Quantum"]==0):
						ready.append(x)
					elif(x["Quantum"]>0):
						aq.append(x)
			print("IN AQ LOOP Print Ready")
			print(ready)
			while(i<len(processes) and clock==processes[i]["Arrival"]):
				ready.append(processes[i])
				i=i+1
			print(ready)
			
			for x in wq:
				x["IO Wait"]-=1

			if(aq[0]["Burst"]==0):
				temp={"Process is ":ready[0]["Process"],"Turnaround Time":clock-ready[0]["Arrival"]}
				tt.append(temp)
				aq.pop(0)
				processes.pop(0)
				i=i-1
				break
			if(aq[0]["IO Burst"]==0):
				wq.append(aq[0])
				aq.pop(0)
				break
			if(aq!=[]):
				aq[0]["Burst"]-=1
				aq[0]["IO Burst"]-=1

			aq[0]["Quantum"]-=1
			clock+=1
		if(aq!=[]):
			if(aq[0]["Quantum"]==0):
				aq[0]["Quantum"]=quantum
				ready.append(aq[0])
				aq.pop(0)

	elif(ready!=[]):
		while(ready[0]["Quantum"]>0):
			for x in wq:
				if(x["IO Wait"]==-1):
					x["IO Burst"]=x["Const IO Burst"]
					x["IO Wait"]=x["Const IO Wait"]
					wq.remove(x)
					if(x["Quantum"]==0):
						ready.append(x)
					elif (x["Quantum"]>0):
						aq.append(x)
			print("IN READY LOOP Print Ready")
			print(ready)
			while(i<len(processes) and clock==processes[i]["Arrival"]):
				ready.append(processes[i])
				i=i+1
			print(ready)
			
			for x in wq:
				x["IO Wait"]-=1

			if(ready[0]["Burst"]==0):
				temp={"Process is ":ready[0]["Process"],"Turnaround Time":clock-ready[0]["Arrival"]}
				tt.append(temp)
				ready.pop(0)
				processes.pop(0)
				i=i-1
				break
			if(ready[0]["IO Burst"]==0):
				wq.append(ready[0])
				ready.pop(0)
				break
			if(ready!=[]):
				ready[0]["Burst"]-=1
				ready[0]["IO Burst"]-=1

			ready[0]["Quantum"]-=1
			clock+=1
		if(ready!=[]):
			if(ready[0]["Quantum"]==0):
				ready[0]["Quantum"]=quantum
				ready.append(ready[0])
				ready.pop(0)
	else:
		clock+=1
		for x in wq:
			x["IO Wait"]-=1

sum=0	
for x in tt:
	sum=sum+x["Turnaround Time"]
	print(x)

print("Average turnaround time= "+str(sum/len(tt)))



