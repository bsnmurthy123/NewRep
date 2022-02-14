n=list(map(int, input().split()))

e=[]
o=[]

for i in n:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)

for i in e:
    print(i, end=" ")
print()

for i in o:
    print(i, end=" ")
