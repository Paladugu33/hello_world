dic = {1:'harsha',2:'mohan','shiva':'harsha'}
val=[]
val=dic.keys()
#val.append(dic.values())
print (val)

n= len(val)
print (n)
for i in range(0,n):
	for j in range(0,n):
		if i==j:
			pass
		elif dic[val[i]]==dic[val[j]]:
			dic[val[j]]=raw_input('enter a new value for %s '%val[j])
print(dic)


