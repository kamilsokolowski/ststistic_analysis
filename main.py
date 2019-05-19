import numpy
import random
import utils

from math import floor
from math import log

from szyfr import Wszyfr

from testserial import Serial
from testfreq import Freq
from testcus import CuSum

print('---------- AES ----------')

print("Zestaw 1")

tests = 0
testf = 0
testc = 0

for i in range(0, 100):
    iv = '0000000000000000'
    p = '0000000000000000'
    e = utils.szyfrowanie_Aes(iv, p)
    e = utils.tobits(e)
    n = len(e)
    m = numpy.random.randint(2, floor(log(n, 2)) - 2)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1

print("Na 100 prob")
print(
	"Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
		tests, testf, testc
	)
)


print("Zestaw 2")

tests = 0
testf = 0
testc = 0

for i in range(0,100):
    iv = '0000000000000000'
    p = '1111111111111111'
    e = utils.szyfrowanie_Aes(iv, p)
    e = utils.tobits(e)
    n = len(e)
    m = numpy.random.randint(2, floor(log(n, 2)) - 2)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1

print("Na 100 prob")
print(
	"Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
		tests, testf, testc
	)
)


print("Zestaw 3")

tests = 0
testf = 0
testc = 0
iv ='0000000000000000'
p = '1111111111111111'

for i in range(0,100):
    e = utils.szyfrowanie_Aes(iv,p)
    e = utils.tobits(e)
    n = len(e)
    m = numpy.random.randint(2, floor(log(n, 2)) - 2)
    if Serial.test(3,n,e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1
    p =  utils.my_xor(p, '1111111111111111')

print("Na 100 prob")
print(
	"Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
		tests, testf, testc
	)
)


print("Zestaw 4")

tests = 0
testf = 0
testc = 0
iv = '1111111111111111'
p = '0101010101010101'

for i in range(0, 100):
    e = utils.szyfrowanie_Aes(iv,p)
    e = utils.tobits(e)
    n = len(e)
    m = numpy.random.randint(2, floor(log(n, 2)) - 2)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1
    p = utils.my_xor(p, '1010101010101010')

print("Na 100 prob")
print(
	"Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
		tests, testf, testc
	)
)


print("Zestaw 5")

tests = 0
testf = 0
testc = 0
iv = '1111111111111111'

for i in range(0, 100):
    if i%4 == 0:
        p='1111111111111111'
    if i%4 == 1:
        p='0000000000000000'
    if i%4 == 2:
        p='0101010101010101'
    if i%4 == 3:
        p='1010101010101010'
    e = utils.szyfrowanie_Aes(iv, p)
    e = utils.tobits(e)
    n = len(e)
    m = numpy.random.randint(2, floor(log(n, 2)) - 2)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1

print("Na 100 prob")
print(
	"Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
		tests, testf, testc
	)
)


print("Zestaw 6")

tests = 0
testf = 0
testc = 0
iv = '1111111111111111'
pp = []
pp.append('0010010010010010')
p1 = '0010010010010010'
p2 = '0110110110110110'
p3 = '1111111111111111'

for i in range(0, 35):
    pp.append(utils.my_xor(p1, pp[1+3 * i-1]))
    pp.append(utils.my_xor(p2, pp[2+3 * i-1]))
    pp.append(utils.my_xor(p3, pp[3+3 * i-1]))

for i in range(0, 100):
    e = utils.szyfrowanie_Aes(iv,pp[i])
    e = utils.tobits(e)
    n = len(e)
    m = numpy.random.randint(2, floor(log(n, 2)) - 2)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1

print("Na 100 prob")
print(
	"Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
		tests, testf, testc
	)
)

print("--------------- Funkcja rand -------------------")
tests = 0
testf = 0
testc = 0
for i in range(0, 100000):
    a = random.getrandbits(10000)
    e = utils.itobytes(a)
    n = len(e)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1

print("Na 100 prob")
print(
	"Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
		tests, testf, testc
	)
)

print('---------- Wszyfr ----------')

print("Zestaw 1")

tests = 0
testf = 0
testc = 0

for i in range(0, 100):
    iv = '0' * 100
    p = '0' * 100
    e = Wszyfr.szyfrowanie(iv, p)
    n = len(e)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1

print("Na 100 prob")
print(
    "Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
        tests, testf, testc
    )
)


print("Zestaw 2")

tests = 0
testf = 0
testc = 0

for i in range(0,100):
    iv = '0' * 100
    p = '1' * 100
    e = Wszyfr.szyfrowanie(iv, p)
    n = len(e)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1

print("Na 100 prob")
print(
    "Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
        tests, testf, testc
    )
)


print("Zestaw 3")

tests = 0
testf = 0
testc = 0
iv ='0' * 100
p = '1' * 100

for i in range(0, 100):
    e = Wszyfr.szyfrowanie(iv, p)
    n = len(e)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1
    p =  utils.my_xor(p, '1'*100)

print("Na 100 prob")
print(
    "Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
        tests, testf, testc
    )
)


print("Zestaw 4")

tests = 0
testf = 0
testc = 0
iv = '1' * 100
p = '01' * 50

for i in range(0, 100):
    e = Wszyfr.szyfrowanie(iv,p)
    n = len(e)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1
    p = utils.my_xor(p, '10'*50)

print("Na 100 prob")
print(
    "Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
        tests, testf, testc
    )
)

print("Zestaw 5")

tests = 0
testf = 0
testc = 0
iv = '1' * 100

for i in range(0, 100):
    if i%4 == 0:
        p = '1' * 100
    if i%4 == 1:
        p = '0' * 100
    if i%4 == 2:
        p = '01' * 50
    if i%4 == 3:
        p = '10' * 50
    e = Wszyfr.szyfrowanie(iv, p)
    n = len(e)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1

print("Na 100 prob")
print(
    "Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
        tests, testf, testc
    )
)

print("Zestaw 6")

tests = 0
testf = 0
testc = 0
iv = '1' * 100
pp = []
pp.append('001'*33 + '0')
p1 = '001'*33 + '0'
p2 = '011'*33 + '0'
p3 = '1' * 100

for i in range(0, 35):
    pp.append(utils.my_xor(p1, pp[1+3 * i-1]))
    pp.append(utils.my_xor(p2, pp[2+3 * i-1]))
    pp.append(utils.my_xor(p3, pp[3+3 * i-1]))

for i in range(0, 100):
    e = Wszyfr.szyfrowanie(iv,pp[i])
    n = len(e)
    if Serial.test(3, n, e) is True:
        tests += 1
    if Freq.test(e, 40, n) is True:
        testf += 1
    if CuSum.test(e, n, 0) is True:
        testc += 1

print("Na 100 prob")
print(
    "Losowych ciagow wedlug test Serial: {} /Freq: {} /CuSum: {}".format(
        tests, testf, testc
    )
)
