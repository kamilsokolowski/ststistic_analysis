#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils import my_xor, itobytes


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
        CIPHER_KEY = [
            3, 0, 2, 1
        ]
        PERMUTATION = [
            3, 0, 2, 1
        ]
        SUBSTITUTION = [
                22,	8,	2,	3,	12,	5,	28,	7,
                1,	9,	10,	25,	4,	24,	14,	31,
                27,	17,	18,	6,	21,	20,	0,	23,
                13,	11,	26,	15,	19,	29,	30,	16
        ]
        ROUND_COUNT = 15

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
        for char in ciag_zaszyfrowany:
            wynik += itobytes(char)
        return my_xor(wynik, pi)
