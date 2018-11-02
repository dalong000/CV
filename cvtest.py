import cv2
import numpy as np

import matplotlib.pyplot as plt




h = 8
w = 8
def avgHash(img):

    '''
    均值哈希算法
    1.缩放：图片缩放为8*8保留结构，除去细节。
    2.灰度化：转换为256阶灰度图
    3.求平均值：计算灰度图所有像素的平均值
    4.比较:像素值大于平均值记作1，平均值小于平均值记作0，共64位。
    5.生成hash：将上述步骤生成的1和0顺序组合起来即是图片的指纹(hash)。顺序不固定，但是比较的时候必须是相同的顺序。
    6.对比指纹：将两幅图的指纹对比，计算汉明距离，即两个64位的hash值有多少位是不一样的，不相同的位数越少，图片越相似。

    :param img:
    :return:
    '''
    #缩放
    img = cv2.resize(img,(h,w),interpolation = cv2.INTER_CUBIC)
    #转换为灰度图
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #s为像素和初值为0，hash_str为hash值初值为''
    s = 0
    hash_str = ''
    for i in range(h):
        for j in range(w):
            s = s+gray[i,j]
    #求平均灰度
    avg = s/64
    #灰度大于平均值为1相反为0生成图片的hash值
    for i in range(h):
        for j in range(w):
            if gray[i,j] > avg:
                hash_str =hash_str + '1'
            else:
                hash_str = hash_str + '0'



    return hash_str


def dhahs(img):

    #缩放9*8
    img = cv2.resize(img,(9,8),interpolation = cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    hash_str =''

    #每前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if gray[i,j] > gray[i,j+1]:
                hash_str = hash_str+'1'
            else :
                hash_str = hash_str + '0'


    return  hash_str

def getdiff(img):
    #定义边长
    Sidelength = 30
    #图像缩放
    img = cv2.resize(img, (Sidelength, Sidelength), interpolation=cv2.INTER_CUBIC)
    #灰度处理
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #保存每行像素的平均值
    avglist = []
    #计算每行平均值，保存到avglist列表
    for i in range(Sidelength):
        avg =sum(gray[i]/len(gray[i]))
        avglist.append(avg)

    return avglist




def getss(list):
    #计算平均值
    avg = sum(list)/len(list)
    #定义方差变量ss，初值为0
    ss =0
    #计算方差
    for l in list:
        ss += (l - avg)*(1 - avg)/len(list)
        #返回方差
        return ss








def cmpHash(hash1,hash2):
    n = 0
    #hash长度不同则返回-1代表传参出错
    if len(hash1)!=len(hash2):
        return -1
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            n = n+1
    return  n



img1 = cv2.imread('990436704.jpg')
img2 = cv2.imread('1526285226.jpg')

hash1 = avgHash(img1)
hash2 = avgHash(img2)

print(hash1)
print(hash2)


n = cmpHash(hash1,hash2)
print(n)


hash1 = dhahs(img1)
hash2 = dhahs(img2)

print(hash1)
print(hash2)
n = cmpHash(hash1,hash2)
print(n)



#读取测试图片
img1=cv2.imread('990436704.jpg')
diff1=getdiff(img1)
print('img1:',getss(diff1))


img2=cv2.imread('1526285226.jpg')
diff2=getdiff(img2)
print('img1:',getss(diff2))

r = range(30)

x=range(30)

plt.figure("avg")
plt.plot(x,diff1,marker="*",label="$walk01$")
plt.plot(x,diff2,marker="*",label="$walk03$")
plt.title("avg")
plt.legend()
plt.show()



plt.show()


