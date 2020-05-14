'''from datetime import datetime

now = datetime.now().time() # time object
i=0
while i<223:
    now = datetime.now().time()
    print("now =", now)
    i+=1
#print("type(now) =", type(now))'''
import time
t=time.localtime()
h=int(time.strftime('%H'))
m=int(time.strftime('%M'))

def binar(h):
    binH=[]
    while int(h)>0:
        b=h%2
        binH.append(b)
        h//=2
    #if len(binH) < 6:
    while len(binH)<6:
        binH.append(0)
    binH.reverse()
    return binH



ore=list(binar(h))
minuti=list(binar(m))

#print(ore)
#print(minuti)


print('\t |'+' 32 '+' 16 '+' 8 '+' 4 '+' 2 '+ ' 1 ')
print(('\tH|'+'  {} '+'  {} '+' {} '+' {} '+' {} '+' {} ').format(ore[0],ore[1],ore[2],ore[3],ore[4],ore[5]))
print(('\tM|'+'  {} '+'  {} '+' {} '+' {} '+' {} '+' {} ').format(minuti[0],minuti[1],minuti[2],minuti[3],minuti[4],minuti[5]))
