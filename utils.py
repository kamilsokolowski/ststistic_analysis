from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

def my_xor(a, b):
    c = ''
    for i in range (0, len(a)):
        if a[i] == '1' and b[i] == '1':
            c += '0'
        if a[i] == '1' and b[i] == '0':
            c += '1'
        if a[i] == '0' and b[i] == '1':
            c += '1'
        if a[i] == '0' and b[i] == '0':
            c += '0'
    return c

def tobits(s):
    result = ''
    for c in s:
        byte = format(ord(c), 'b')
        result += byte
    return result

def itobytes(t):
        b=''
        br=''
        for i in range (0,5):
            if t!=0:
                if t%2==1:
                    b+='1'
                    t=(t-1)/2
                else:
                    b+='0'
                    t=t/2
            else:
                b+='0'
        for i in range (0,5):
            br+=b[4-i]
        return br

def szyfrowanie_Aes(iv, p):
    key = get_random_bytes(16)
    cipher = AES.new(
    	key, 
    	AES.MODE_OFB, 
    	iv
    )
    msg = iv + cipher.encrypt(p)
    return msg
