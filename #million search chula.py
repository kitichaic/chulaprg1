#million search chula
#f = open("million.txt","r")
f=open("million-sorted.txt","r")
sites= []
pos = 0
name="chula.ac.th"
for x in f:
    site = x.strip()
    sites.append(site)
    
   

f.close()
print (len(sites))


