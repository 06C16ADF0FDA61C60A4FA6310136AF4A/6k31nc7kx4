def tri(rows):
    data = []
    for r in range(rows):
        row = []
        for n in range(rows-r): row+=[0]
        data+=[row]
    return data

size = 8
for line in tri(size):
    emp = ''
    for n in range(size-len(line)):
        if n%2: emp+=' '
        else: emp+='  '
    print( emp+str(line) )
