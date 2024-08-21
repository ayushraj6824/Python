size=5
alphabet=[chr(i) for i in range(97,123)]
alphabet=alphabet[:size]
l=list(range(size))
l=l[:-1]+l[::-1]
for i in l:
    start=i+1
    origina=alphabet[-start:]
    reverse=origina[::-1]
    row=reverse +origina[1:]
    row="-".join(row)
    width=size*4-3
    row=row.center(width,"-")
    print(row)