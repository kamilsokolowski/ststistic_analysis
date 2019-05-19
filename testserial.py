from scipy.special import gammaincc


class Serial:
    """
    A class thats implements Serial
    statistics test.
    ...
    Methods
    -------
    test(m, n, e)
        Performes test with on parameters.
    """
    @staticmethod
    def test(m,n,e):
        """
        Performes test with on parameters.

        All parameters are required

        Parameters
        ----------
        m : str,
            The length in bits of each block.

        n : int
            The length in bits of the bit string.

        e : str
            Sequence of bits.
        """
        e = list(e)
        dlugosc_ciagu=m
        ep=e
        ep.append('0')
        ep.append('0')
        v = [0] * 3
        for i in range(3):
            v[i] = [0] * (2**m)
        for z in range (0,dlugosc_ciagu):
            ciag_testowany=[]
            for i in range (0,m):
                ciag_testowany.append('0')
            for i in range (0,2**m):
                mp=m
                while mp>0:
                    if ciag_testowany[mp-1]=='0':
                        ciag_testowany[mp-1]='1'
                        mp=0
                    else:
                        ciag_testowany[mp-1]='0'
                        mp=mp-1
                v[z][i]=Serial.szukanie_ciagow(ep,ciag_testowany)
            m=m-1
            del ep[len(ep)-1]
        psi=Serial.funkcja_psi_kwadrat(v,dlugosc_ciagu,n)
        delta=psi[0]-psi[1]
        delta_kwadrat=psi[0]-2*psi[1]+psi[2]
        pValue1= gammaincc(2**(dlugosc_ciagu-2),delta/2)
        pValue2= gammaincc(2**(dlugosc_ciagu-3),delta_kwadrat/2)
        if pValue1>=0.01 and pValue2>=0.01:
            return True
        else:
            return False

    @staticmethod
    def szukanie_ciagow(e,ct):
        l=0
        el=len(e)
        cl=len(ct)
        for i in range (0,el-cl+1):
            test=0
            for j in range (0,cl):
                if e[i+j]!=ct[j]:
                    test=1
            if test==0:
                l=l+1
        return l

    @staticmethod
    def funkcja_psi_kwadrat(v,m,n):
        psi_tab=[0,0,0]
        for j in range (0,3):
            psi=0
            for i in range (0,2**m):
                psi+=(v[j][i])**2
            psi=(psi*2**m)/n-n
            m=m-1
            psi_tab[j]= psi
        return psi_tab
