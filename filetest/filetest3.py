infp=None
inList=""

infp=open("C:\\Users\\사용자\\Downloads\\.dist\\FileTest\\data1.txt","r",encoding='UTF8')

inList=infp.readlines()
for inStr in inList:
    print(inStr,end="")

infp.close()