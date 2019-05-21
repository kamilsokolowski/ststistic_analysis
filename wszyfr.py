#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils import my_xor, itobytes 
import random
class Wszyfr:

    @staticmethod
    def ciag_B_do_int(ciag):
        liczba = 0
        tablica = []
        for i in range(0, len(ciag)):
            if ciag[i] == '0':
                liczba = liczba*2
            else:
                liczba = liczba*2 + 1
            if i%5 == 4:
                tablica.append(liczba)
                liczba = 0
        return tablica

    @staticmethod
    def permute(block, permutation):
        newblock = [block[i] for i in permutation]
        return newblock

    @staticmethod
    def add_key(block, key):
        newblock = [(block[i] + key[i]) % 32 for i in range(len(block))]
        return newblock

    @staticmethod
    def substitute(block, substitution):
        newblock = [substitution[c] for c in block]
        return newblock

    @staticmethod
    def convert_input_character(_c):
        ic_table = { ' ' : 0, '.' : 27, ',' : 28, ':' : 29, '!' : 30, '\n' : 31, '?' : 27, '-' : 0, '\t' : 0}
        ogonki = {'ą' : 'a', 'ć' : 'c', 'ę' : 'e', 'ł' : 'l', 'ń' : 'n', 'ó' : 'o', 'ś' : 's', "ź" : 'z', 'ż' : 'z'}
        if _c in ogonki:
            _c = ogonki[_c]
        ret = None
        if _c in ic_table:
            ret = ic_table[_c]
        else:
            _tmp = ord(_c.lower())
            _tmp = _tmp - 96
            if _tmp >= 1 and _tmp <= 26:
                ret = _tmp
        return ret

    @staticmethod
    def cipher_block_generator(cipherstring, blocklen):
        buf = []
        for _cc in cipherstring:
            buf.append(_cc)
            if len(buf) == blocklen:
                yield buf
                buf = []
        if len(buf) > 0:
            while len(buf) < blocklen:
                buf.append(Wszyfr.convert_input_character(' '))
            yield buf
    @staticmethod
    def szyfrowanie(iv, pi):
        CIPHER_KEY = []
        for i in range (0,20):
            CIPHER_KEY.append(random.randint(0,20))
        support_tab=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        #CIPHER_KEY = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        PERMUTATION = []
        for i in range (0,20):
            a = random.randint(0,19-i)
            PERMUTATION.append(support_tab[a])
            del support_tab[a]
        SUBSTITUTION = []
        #PERMUTATION = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,0]
        support_tab=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        for i in range (0,32):
            a = random.randint(0,31-i)
            SUBSTITUTION.append(support_tab[a])
            del support_tab[a]
        #SUBSTITUTION = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,0]
        ROUND_COUNT = 1

        if len(PERMUTATION) == len(CIPHER_KEY):
            l = len(PERMUTATION)
        else:
            print("rozmiar permutacji i cipher_key roznia sie")

        t = Wszyfr.ciag_B_do_int(iv)
        ciag_zaszyfrowany = []

        for block in Wszyfr.cipher_block_generator(t, len(CIPHER_KEY)):
            for i in range(0,ROUND_COUNT):
                block = Wszyfr.add_key(block, CIPHER_KEY)
                block = Wszyfr.permute(block, PERMUTATION)
                block = Wszyfr.substitute(block, SUBSTITUTION)
            for i in range(0,len(block)):
                ciag_zaszyfrowany.append(block[i])

        wynik = ''
        #print (ciag_zaszyfrowany)
        for char in ciag_zaszyfrowany:
            wynik += itobytes(char)
        wynik = my_xor(wynik,pi)
        return wynik