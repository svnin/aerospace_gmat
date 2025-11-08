x = list(input())
print (f"DNA: {"".join(x)}")
y=[]
for i in x:
    if i.lower() == "a":
        i = "T"
    elif i.lower()=="c":
        i= "G"
    elif i.lower() =="t":
        i="A"
    elif i.lower() == "g":
        i="C"
    else: 
        i == i
    y.append(i)

print(f"Complement: {"".join(y)}")

#reverse
o = ""
for i in range(len(y)):
    o = y[i] + o 

print(f'reverse complement ={o}')

 