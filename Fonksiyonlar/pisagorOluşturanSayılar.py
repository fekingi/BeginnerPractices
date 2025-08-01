def pisagorkenar():
    pisagorlist = []
    for i in range(1,101):
        for j in range(1,101):
            c = (i**2+j**2)**0.5
            if c == int(c):
                pisagorlist.append((i,j,int(c)))
    return pisagorlist

for i in pisagorkenar():
    print(i)