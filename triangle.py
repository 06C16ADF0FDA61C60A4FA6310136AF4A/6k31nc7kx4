class Plex:
    def __init__(self,size):
        bitdata = []
        numdata = []
        for r in range(size):
            bit = []
            num = []
            for n in range(r+1):
                bit+=[0]
                num+=[0]
            bitdata+=[bit]
            numdata+=[num]
        self.bitdata = bitdata
        self.numdata = numdata
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


plex = Plex(8)

while 1:
    print()
    path = plex.tracePath(0,0)
    print( path )
    print()
    display(plex.bitdata)
    input()


import random, string


s=string.lowercase+string.digits
a=''.join(random.sample(s,10))

print( a )
