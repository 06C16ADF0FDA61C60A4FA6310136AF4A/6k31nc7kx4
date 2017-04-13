class Plex:
    def __init__(self):
        pass

def tri(rows):
    data = []
    for r in range(rows):
        row = []
        for n in range(r+1): row+=[0]
        data+=[row]
    return data


def iterate(data,a,b):
    while a+b<len(data):
        for r in range(len(data)):
            line = data[r]
            #print( line, b )
            line[b]=1-line[b]
            if line[b]: a+=1
            else: b+=1
    return data
                


def display(data):
    size = 8
    for l in range(len(data)):
        l = len(data)-l-1
        line = data[l]
        emp = ''
        for n in range(size-len(line)):
            if n%2: emp+=' '
            else: emp+='  '
        print( emp+str(line) )
    print()

triangle = tri(8)
display(triangle)
display(iterate(iterate(iterate(triangle,0,0),0,0),0,0))
