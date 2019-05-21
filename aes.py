from Crypto.Cipher import AES
from Crypto import Random
from scipy.special import gammaincc
import textwrap
from math import sqrt
import numpy
from math import floor
from math import log
import utils
from testserial import Serial
from testfreq import Freq
from testcus import CuSum
from wszyfr import Wszyfr
import random



def average(lst): 
    return sum(lst) / len(lst) 

def itobytes (t):
    b=''
    br=''
    for i in range (0,16):
        if t!=0:
            if t%2==1:
                b+='1'
                t=(t-1)/2
            else:
                b+='0'
                t=t/2
        else:
            b+='0'
    for i in range (0,16):
        br+=b[4-i]
    return br

def itobytes2 (t):
    b=''
    br=''
    for i in range (0,100):
        if t!=0:
            if t%2==1:
                b+='1'
                t=(t-1)/2
            else:
                b+='0'
                t=t/2
        else:
            b+='0'
    for i in range (0,100):
        br+=b[4-i]
    return br
def my_xor (a,b):
    c=''
    for i in range (0,len(a)):
        if a[i]=='1' and b[i]=='1':
            c+='0'
        if a[i]=='1' and b[i]=='0':
            c+='1'
        if a[i]=='0' and b[i]=='1':
            c+='1'
        if a[i]=='0' and b[i]=='0':
            c+='0'
    return c



def tobits(s):
    result = ''
    for c in s:
        byte = format(ord(c), 'b')
        result += byte
    return result

def szyfrowanie_Aes(iv,p):
    key=numpy.random.bytes(16)
    msg=''
    #print (key)
    cipher = AES.new(key, 5, iv)
    msg += cipher.encrypt(p)
    return msg
print ("AES")
print ("--------------------------------")
print ("Zestaw 1")
tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []
for i in range (0,100):
    
    iv='0000000000000000'
    p='0000000000000000'
    e=szyfrowanie_Aes(iv,p)
    e = tobits(e)
    n=len(e)
    
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1
print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))



print ("--------------------------------")
print ("Zestaw 2")
tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []
for i in range (0,100):
    
    iv='0000000000000000'
    p= '1111111111111111'
    e=szyfrowanie_Aes(iv,p)
    e = tobits(e)
    n=len(e)
    #print(floor(log(n,2)))
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1
print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))


print ("--------------------------------")
print ("Zestaw 3")
tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []
iv='0000000000000000'
p= '1111111111111111'
for i in range (0,100):
    e=szyfrowanie_Aes(iv,p)
    e = tobits(e)
    n=len(e)
    #print(floor(log(n,2)))
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1
    p =  my_xor(p,'1111111111111111')
print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))



print ("--------------------------------")
print ("Zestaw 4")
tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []
iv='1111111111111111'
p= '0101010101010101'
for i in range (0,100):
    e=szyfrowanie_Aes(iv,p)
    e = tobits(e)
    n=len(e)
    #print(floor(log(n,2)))
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1
    p =  my_xor(p,'1010101010101010')
print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))



print ("--------------------------------")
print ("Zestaw 5")
tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []
iv='1111111111111111'
for i in range (0,100):
    if i%4==0:
        p='1111111111111111'
    if i%4==1:
        p='0000000000000000'
    if i%4==2:
        p='0101010101010101'
    if i%4==3:
        p='1010101010101010'
    e=szyfrowanie_Aes(iv,p)
    e = tobits(e)
    n=len(e)
    #print(floor(log(n,2)))
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1
print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))



print ("--------------------------------")
print ("Zestaw 6")
tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []
iv='1111111111111111'
pp=[]
pp.append('0010010010010010')
p1='0010010010010010'
p2='0110110110110110'
p3='1111111111111111'

for i in range (0,35):
    pp.append(my_xor(p1,pp[1+3*i-1]))
    pp.append(my_xor(p2,pp[2+3*i-1]))
    pp.append(my_xor(p3,pp[3+3*i-1]))
for i in range (0,100):

    e=szyfrowanie_Aes(iv,pp[i])
    e = tobits(e)
    n=len(e)
    #print(floor(log(n,2)))
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1
print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))


print ("----------------------------------")
print ("----------------------------------")
print ("Funkcja rand")
tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []
for i in range (0,100):
    a=random.getrandbits(100)
    e=itobytes2(a)
    #print (e)
    n=len(e)
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1
print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))



print ("--------------------------------")
print('----------Wszyfr----------')

print("Zestaw 1")

tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []

for i in range(0, 100):
    iv = '0' * 100
    p = '0' * 100
    e = Wszyfr.szyfrowanie(iv, p)
    n = len(e)
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1

print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))




print ("--------------------------------")
print("Zestaw 2")

tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []

for i in range(0,100):
    iv = '0'*100
    p = '1'*100
    e = Wszyfr.szyfrowanie(iv, p)
    n = len(e)
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1

print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))




print ("--------------------------------")
print("Zestaw 3")

tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []
iv ='0'*100
p = '1'*100

for i in range(0,100):
    e = Wszyfr.szyfrowanie(iv,p)
    n = len(e)
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1
    p =  utils.my_xor(p, '1'*100)

print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))




print ("--------------------------------")
print("Zestaw 4")

tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []
iv = '1'*100
p = '01'*50

for i in range(0, 100):
    e = Wszyfr.szyfrowanie(iv,p)
    n = len(e)
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1
    p = utils.my_xor(p, '10'*50)

print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))



print ("--------------------------------")
print("Zestaw 5")

tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []
iv = '1'*100



for i in range(0, 100):
    if i%4 == 0:
        p='1'*100
    if i%4 == 1:
        p='0'*100
    if i%4 == 2:
        p='01'*50
    if i%4 == 3:
        p='10'*50
    e = Wszyfr.szyfrowanie(iv, p)
    n = len(e)
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1

print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))


print ("--------------------------------")
print("Zestaw 6")

tests = 0
testf = 0
testc = 0
statistic_s = []
statistic_f = []
statistic_c = []
iv = '1'*100
pp = []
pp.append('001'*33+'0')
p1 = '001'*33 + '0'
p2 = '011'*33 + '0'
p3 = '1'*100

for i in range(0, 35):
    pp.append(utils.my_xor(p1, pp[1+3 * i-1]))
    pp.append(utils.my_xor(p2, pp[2+3 * i-1]))
    pp.append(utils.my_xor(p3, pp[3+3 * i-1]))

for i in range(0, 100):
    e = Wszyfr.szyfrowanie(iv,pp[i])
    n = len(e)
    retval, cond = Serial.test(3, n, e)
    statistic_s.append(retval)
    if cond is True:
        tests+=1
    
    retval, cond = Freq.test(e, 40, len(e))
    statistic_f.append(retval)
    if cond is True:
        testf+=1
    
    retval, cond = CuSum.test(e, len(e), 0)
    statistic_c.append(retval)
    CuSum.test(e, len(e), 0)
    if cond is True:
        testc+=1

print ("Na 100 prob\n")
print ("Serial Test: ")
print ("Max P_Value = {}".format(max(statistic_s)))
print ("Min P_Value = {}".format(min(statistic_s)))
print ("Mediana = {}".format(numpy.median(statistic_s)))
print ("Srednia P_Value = {}".format(average(statistic_s)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_s, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(tests))

print ("Freq Test: ")
print ("Max P_Value = {}".format(max(statistic_f)))
print ("Min P_Value = {}".format(min(statistic_f)))
print ("Mediana = {}".format(numpy.median(statistic_f)))
print ("Srednia P_Value = {}".format(average(statistic_f)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_f, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testf))

print ("CuSum Test: ")
print ("Max P_Value = {}".format(max(statistic_c)))
print ("Min P_Value = {}".format(min(statistic_c)))
print ("Mediana = {}".format(numpy.median(statistic_c)))
print ("Srednia P_Value = {}".format(average(statistic_c)))
print ("Odchylenie Standardowe = {}".format(numpy.std(statistic_c, axis=0)))
print ("Liczba ciagow losowych = {}\n".format(testc))