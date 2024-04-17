#million search chula
#f = open("million.txt","r")
f=open("million-sorted.txt","r")
pos = 0
for x in f:
    site = x.strip()
    pos = pos+1
    if site=="chula.ac.th":
        break
        print(x.strip())
f.close()

print(pos)

