class AES:
    s_box=[
    [0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76],
    [0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0],
    [0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15],
    [0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75],
    [0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84],
    [0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf],
    [0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8],
    [0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2],
    [0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73],
    [0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb],
    [0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79],
    [0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08],
    [0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a],
    [0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e],
    [0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf],
    [0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16]]
    #逆s盒
    s_boxs=[
    [0x52,0x09,0x6a,0xd5,0x30,0x36,0xa5,0x38,0xbf,0x40,0xa3,0x9e,0x81,0xf3,0xd7,0xfb],
    [0x7c,0xe3,0x39,0x82,0x9b,0x2f,0xff,0x87,0x34,0x8e,0x43,0x44,0xc4,0xde,0xe9,0xcb],
    [0x54,0x7b,0x94,0x32,0xa6,0xc2,0x23,0x3d,0xee,0x4c,0x95,0x0b,0x42,0xfa,0xc3,0x4e],
    [0x08,0x2e,0xa1,0x66,0x28,0xd9,0x24,0xb2,0x76,0x5b,0xa2,0x49,0x6d,0x8b,0xd1,0x25],
    [0x72,0xf8,0xf6,0x64,0x86,0x68,0x98,0x16,0xd4,0xa4,0x5c,0xcc,0x5d,0x65,0xb6,0x92],
    [0x6c,0x70,0x48,0x50,0xfd,0xed,0xb9,0xda,0x5e,0x15,0x46,0x57,0xa7,0x8d,0x9d,0x84],
    [0x90,0xd8,0xab,0x00,0x8c,0xbc,0xd3,0x0a,0xf7,0xe4,0x58,0x05,0xb8,0xb3,0x45,0x06],
    [0xd0,0x2c,0x1e,0x8f,0xca,0x3f,0x0f,0x02,0xc1,0xaf,0xbd,0x03,0x01,0x13,0x8a,0x6b],
    [0x3a,0x91,0x11,0x41,0x4f,0x67,0xdc,0xea,0x97,0xf2,0xcf,0xce,0xf0,0xb4,0xe6,0x73],
    [0x96,0xac,0x74,0x22,0xe7,0xad,0x35,0x85,0xe2,0xf9,0x37,0xe8,0x1c,0x75,0xdf,0x6e],
    [0x47,0xf1,0x1a,0x71,0x1d,0x29,0xc5,0x89,0x6f,0xb7,0x62,0x0e,0xaa,0x18,0xbe,0x1b],
    [0xfc,0x56,0x3e,0x4b,0xc6,0xd2,0x79,0x20,0x9a,0xdb,0xc0,0xfe,0x78,0xcd,0x5a,0xf4],
    [0x1f,0xdd,0xa8,0x33,0x88,0x07,0xc7,0x31,0xb1,0x12,0x10,0x59,0x27,0x80,0xec,0x5f],
    [0x60,0x51,0x7f,0xa9,0x19,0xb5,0x4a,0x0d,0x2d,0xe5,0x7a,0x9f,0x93,0xc9,0x9c,0xef],
    [0xa0,0xe0,0x3b,0x4d,0xae,0x2a,0xf5,0xb0,0xc8,0xeb,0xbb,0x3c,0x83,0x53,0x99,0x61],
    [0x17,0x2b,0x04,0x7e,0xba,0x77,0xd6,0x26,0xe1,0x69,0x14,0x63,0x55,0x21,0x0c,0x7d]]


    #字节代替，传入4个32bit整数与代替的盒
    def substitute_bytes(self,x=[],s='E'):
        if s=='E':
            box=self.s_box
        elif s=='D':
            box=self.s_boxs
        else:
            print('输入错误')
            return
        for i in range(4):                                      #i作为x的标号
            x_temp=0
            for j in range(4):
                temp=x[i]>>(24-j*8)&0b11111111                  #每次取出8bit
                x_temp=x_temp<<8|box[temp>>4][temp&0b1111]      #取左4bit为行标，右4bit为列标，在盒中找出对应位置的值并拼接在x_temp中
            x[i]=x_temp                                         #拼接完成后放回原位，假装什么都没发生的样子
        return x
            
    #行移位变换
    def shiftrows(self,x=[],s=''):
        #第一行不变
        if s=='E':
            i=1;j=3
        elif s=='D':
            i=3;j=1
        else:
            print('输入错误')
            return
        #第二行移动
        temp=0
        temp=temp<<8|(x[i]>>16&0b11111111)                      #取出8bit
        temp=temp<<8|(x[i]>>8&0b11111111)
        temp=temp<<8|(x[i]&0b11111111)
        temp=temp<<8|(x[i]>>24)
        x[i]=temp

        #第三行移动
        temp=0
        temp=temp<<8|(x[2]>>8&0b11111111)                       #取出8bit
        temp=temp<<8|(x[2]&0b11111111)
        temp=temp<<8|(x[2]>>24)
        temp=temp<<8|(x[2]>>16&0b11111111)
        x[2]=temp

        #第四行移动
        temp=0
        temp=temp<<8|(x[j]&0b11111111)                          #取出8bit
        temp=temp<<8|(x[j]>>24)
        temp=temp<<8|(x[j]>>16&0b11111111)
        temp=temp<<8|(x[j]>>8&0b11111111)
        x[j]=temp
        
        return(x)

    #对系数来自GF(2)域的多项式进行求模运算
    def mod(self,a=127,b=23):
        if b==0: return(0,float('inf'))
        while len(bin(a))>=len(bin(b)):
            temp=len(bin(a))-len(bin(b))
            a=a^(b<<temp)
        return(a)

    #多项式乘法
    def mul(self,a=127,b=23):
        sum=0                               
        temp=list(bin(a))
        temp.reverse()
        for i in range(len(temp)-2):
            if(temp[i]=='1'):              
                sum=sum^b<<i
        return(self.mod(sum,283))

    #列混淆
    def mixColumns(self,x=[0x87f24d97,0x6e4c90ec,0x46e74ac3,0xa68cd895],sta=''):
        if sta=='E':
            s=[2,3,1,1,
               1,2,3,1,
               1,1,2,3,
               3,1,1,2] 
        elif sta=='D':
            s=[0xe,0xb,0xd,0x9,
               0x9,0xe,0xb,0xd,
               0xd,0x9,0xe,0xb,
               0xb,0xd,0x9,0xe]
        else:
            print('输入错误')
            return

        t=[0 for i in range(4)]                             #初始化列表用于存放矩阵乘积
        for i in range(4):                                  #经典的矩阵相乘三重循环
            for j in range(4):
                temp_t=0
                for k in range(4):
                    temp=x[k]>>(24-j*8)&0b11111111          #取出第k行第j个bit的值
                    temp_t=temp_t^self.mul(s[i*4+k],temp)        #s[i][k]与取出的temp相乘并累加
                t[i]=t[i]<<8|temp_t                         #把乘积矩阵中同行的元素拼接成一个32bit的数值数据存储
        return(t)
        
    #轮密钥加变换
    def addRoundKey(self,x=[],k=[],s=''):
        if s=='D':
            k=self.mixColumns(k,'D')
        for i in range(4):
            x[i]=x[i]^k[i]
        return(x)

    #密钥扩展
    def keyExpansion(self,key=[0x0f470caf,0x15d9b77f,0x71e8ad67,0xc959d698],j=1,box=[]):
        """传入4个32bit数构成的列表和下一轮密钥的轮数"""
        #g函数变换
        kword=[0 for i in range(4)]                         #初始化一个数组，用于存放g变换后的word3
        #移位
        kword[3]=key[0]&0b11111111
        kword[3]=box[kword[3]>>4][kword[3]&0b1111]
        kword[0]=key[1]&0b11111111
        kword[0]=box[kword[0]>>4][kword[0]&0b1111]
        kword[1]=key[2]&0b11111111
        kword[1]=box[kword[1]>>4][kword[1]&0b1111]
        kword[2]=key[3 ]&0b11111111
        kword[2]=box[kword[2]>>4][kword[2]&0b1111]
        #轮常量
        rc=[0x1,0x2,0x4,0x8,0x10,0x20,0x40,0x80,0x1b,0x36]
        
        kword[0]^=rc[j]
        #密钥扩展
        for i in range(4):                                  #按行操作，相当于把每列拆分成四部分操作，i控制行
            temp0=key[i]>>24^kword[i]                       #取出前8bit并做异或运算
            temp1=key[i]>>16&0b11111111^temp0
            temp2=key[i]>>8&0b11111111^temp1
            temp3=key[i]&0b11111111^temp2
            key[i]=(temp0<<24)|(temp1<<16)|(temp2<<8)|temp3 #将取出后变换完的数再次拼接成32bit的数放回key[i]
        return(key)

    #获取所有密钥    
    def keyall(self,key=[0x0f470caf,0x15d9b77f,0x71e8ad67,0xc959d698]):
        """返回一个包含每轮密钥的列表"""
        key=[key[:]]
        for i in range(10):
            key.append(self.keyExpansion(key[i][:],i,self.s_box))
##        for i in range(11):
##            print(hex(key[i][0])+'\n'+hex(key[i][1])+'\n'+hex(key[i][2])+'\n'+hex(key[i][3])+'\n')
        return key
