import random
import struct
from AES import AES
class WorkMode(AES):
    def readInChunks(self,fileObj, chunkSize=2048):
        """Lazy function to read a file piece by piece.
        Default chunk size: 2kB."""
        while True:
            data = fileObj.read(chunkSize)
            if not data:
                break
            yield data

    def ECB(self,path='IMG_20160506_7.jpg.aes',key=[0x0f470caf,0x15d9b77f,0x71e8ad67,0xc959d698],state='E'):
        key=super().keyall(key)
        f=open(path,'rb')
        if state=='E':
            function=super().AES_E
            path+='.aes'
        elif state=='D':
            function=super().AES_D
            path=path[:len(path)-4]
        else:
            print('状态参数错误！')
            return
        g=open(path,'wb+')
        i=0;j=1
        print(0)
        for temp in self.readInChunks(f,16):
            if len(temp)==16:
                i+=1
                temp=list(struct.unpack('IIII',temp))
                temp=function(temp,key)
                g.write(struct.pack('IIII',temp[0],temp[1],temp[2],temp[3]))
                g.flush()
                if i==6400:
                    print(j)
                    j+=1
                    i=0
        if state=='E':              #最后分组填充并加密
            x=len(temp)
            temp+=bytes(random.sample(range(256),16-x))
            temp=list(struct.unpack('IIII',temp))
            temp=function(temp,key)
            g.write(struct.pack('IIII',temp[0],temp[1],temp[2],temp[3]))
            #存储上一分组中非填充字节数并加密
            temp=bytes(random.sample(range(256),15)+[x])
            temp=list(struct.unpack('IIII',temp))
            temp=function(temp,key)
            g.write(struct.pack('IIII',temp[0],temp[1],temp[2],temp[3]))

        else:
            g.seek(-1,2)
            temp=g.read()
            temp+=bytes(3)
            temp=struct.unpack('I',temp)[0]
            g.seek(temp-32,2)
            g.truncate()
        g.close()

"""    def CBC(self,path='key.txt',key=[0x0f470caf,0x15d9b77f,0x71e8ad67,0xc959d698],state='E'):
        key=super().keyall(key)
        f=open(path,'rb')
        xor=addRoundKey
        if state=='E':
            function=super().AES_E
            IV=bytes(random.sample(range(256),16))
            g=open(path+'.IV','wb')
            g.write(IV)
            g.close()
            path+='.aes'
        elif state=='D':
            function=super().AES_D
            path=path[:len(path)-4]
            g=open(path+'.IV','rb')
            IV=g.read()
            g.close()            
        else:
            print('状态参数错误！')
            return
        IV=list(struct.unpack('IIII',IV))
        g=open(path+'.aes','wb+')
        temp=f.read(16)
        temp=list(struct.unpack('IIII',temp))
        IV[0]^temp[0];IV[1]^temp[1];IV[2]^temp[2];IV[3]^temp[3]
        i=0;j=1
        print(0)
        while True:#len(temp)==16:
            i+=1
            temp=function(temp,key)
            temp=struct.pack('IIII',temp[0],temp[1],temp[2],temp[3])
            g.write(temp)
            g.flush()
            temp=f.read(16)
            xor(temp,IV,'E')
            if i==6400:
                print(j)
                j+=1
                i=0
        if state=='E':
            x=len(temp)
            temp+=bytes(random.sample(range(256),16-x))
            temp=list(struct.unpack('IIII',temp))
            temp=function(temp,key)
            g.write(struct.pack('IIII',temp[0],temp[1],temp[2],temp[3]))
            
            temp=bytes(random.sample(range(256),15)+[x])
            temp=list(struct.unpack('IIII',temp))
            temp=function(temp,key)
            g.write(struct.pack('IIII',temp[0],temp[1],temp[2],temp[3]))

        else:
            g.seek(-1,2)
            temp=g.read()
            temp+=bytes(3)
            temp=struct.unpack('I',temp)[0]
            g.seek(temp-32,2)
            g.truncate()
        g.close()"""
                
a=WorkMode()
a.ECB('IMG_20160506_7.jpg.aes',[0x0f470caf,0x15d9b77f,0x71e8ad67,0xc959d698],'D')
print('ok')
