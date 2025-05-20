infp=None
instr=""

infp=open("C:\\Users\\사용자\\Downloads\\.dist\\FileTest\\data1.txt","r",encoding='UTF8')

instr=infp.readline()
print(instr,end="")

instr=infp.readline()
print(instr,end="")

instr=infp.readline()
print(instr,end="")

infp.close()

