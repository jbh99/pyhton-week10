mystr="파이썬은 재미있다. 매일 공부하고싶다.^^"
strPosList=[]
index=0

while True:
   try:
    index=mystr.index("파이썬",index)
    strPosList.append(index)
    index= index+1
   except:
    break

print("파이썬 글자 위치-->",strPosList)