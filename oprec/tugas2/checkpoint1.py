x = input()
k = int(input())

p =[]

for i in range(len(x)):
        o =x[i]+""
        if i + k > (len(x)):
            continue

        for y in range(k-1): 
            o = o + x[i+y+1]  
        p.append(o)

print(p)


m =[]

for r in p:
     if r not in m:
          print(f'{r}:{p.count(r)}')
          m.append(r)
          

#CP2
sblmreverse= []
for i in p:
    jj=""
    for j in i:      
          if j.lower()== "a" :
               j = "T"
          elif j.lower()=="t":
               j="A"
          elif j.lower() == "c":
               j = "G"
          elif j.lower() == "g":
               j="C"
          else:
               j = j
          jj = jj + j
    sblmreverse.append(jj)      


stelahreverse =[]
for i in sblmreverse:
    ww =""
    for j in i:
          ww = j + ww
    stelahreverse.append(ww)


print("\ncheckpoint2")
sdhada = []
for i in range(len(p)):
    ori = p[i]
    rev = stelahreverse[i]

    if ori in sdhada or rev in sdhada:
        continue

    if rev in p:
        print(f"{ori} <-> {rev}")
        sdhada.append(ori)
        sdhada.append(rev)



          
          
          