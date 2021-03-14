table=[29,0,0,23,4,3,0,0,0,9]
N=len(table)
sum=0
count=0
for i in range(N):
    if table[i]!=0:
        value=table[i]%10
        step=(N+i-value+1)%10
        count=count+1
        sum=sum+step
avg=sum/count
print(avg)        
