size=10
alphabet=[chr(i) for i in range(97,123)]
#print(alphabet)
alphabet=alphabet[:size]
#print(alphabet)
l=list(range(size))
l=l[:-1]+l[::-1]
#print(l)
for i in l:
    start=i+1
    origina=alphabet[-start:]
    reverse=origina[::-1]
    row=reverse +origina[1:]
    row="-".join(row)
    width=size*4-3
    row=row.center(width,"-")
    print(row)