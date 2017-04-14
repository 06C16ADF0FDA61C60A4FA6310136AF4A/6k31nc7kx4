class Plex:
    def __init__(self,size):
        bdata = []
        ndata = []
        for r in range(size):
            b = []
            d = []
            for n in range(r+1):
                b+=[0]
                d+=[0]
            bdata+=[b]
            ndata+=[d]
        self.bitdata = bdata
        self.numdata = ndata
    def bitGet(a,b):
        return self.bitdata[a+b][b]
    def bitFlip(a,b):
        self.bitdata[a+b][b] = 1-self.bitdata[a+b][b]
    def numGet(a,b):
        return self.bitdata[a+b][b]
    def numAdd(a,b,n):
        self.bitdata[a+b][b] = 1-self.bitdata[a+b][b] 
    def tracePath(self,a,b):
        path = []
        data = self.bitdata
        while a+b<len(data):
            for r in range(len(data)):
                line = data[r]
                #print( line, b )
                line[b]=1-line[b]
                if line[b]:
                    a+=1
                    path+=[0]
                else:
                    b+=1
                    path+=[1]
        self.bitdata = data
        return path
                
def display(data):
    for l in range(len(data)):
        l = len(data)-l-1
        line = data[l]
        emp = ''
        for n in range(len(data)-len(line)):
            if n%2: emp+=' '
            else: emp+='  '
        print( emp+str(line) )
    print()

def compute(size):
    plex = Plex(size)
    index = []
    for n in range(2**size):
        index+=['']
    for n in range(2**size):
        path = plex.tracePath(0,0)
        a = "".join(str(x) for x in path)
        index[int(a,2)]+='|'+str(n)
        print( path, int(a,2) )
    print()
    return plex,index


plex, index = compute(4)




while 1:
    print()
    path = plex.tracePath(0,0)
    a = "".join(str(x) for x in path)
    print( path, int(a,2) )
    print()
    display(plex.bitdata)
    input()


import random, string


s=string.lowercase+string.digits
a=''.join(random.sample(s,10))

print( a )
