import textwrap
from scipy.special import gammaincc


class Freq:
    """
    A class thats implements Frequency Test within a Block.
    ...
    Methods
    -------
    test(e, M, n)
        Performes test with on parameters.
    """
    @staticmethod
    def test(e, M, n):
        """
        Performes test with on parameters.

        All parameters are required

        Parameters
        ----------
        e : str,
            Bit sequence concidered in the test

        M : int
            The length of each block.

        n : int
            Length of bit sequence.
        """
        N = n//M
        subsequence = (textwrap.wrap(e, M))
        if len(e[-1]) != M:
            e = e[:-len(e[-1])]

        pi = []
        sigma = 0.0
        for i in range(0, N):
            for j in range(0, M):
                sigma += int(e[i*M+j-1])
            pi.append(sigma/M)
            sigma = 0.0

        x_2 = 0.0
        for i in range(0, N):
            x_2 += ((pi[i] - 0.5) ** 2)
        x_2 = x_2 * 4 * M
        p = Freq.p_value(N, x_2)
        if p >= 0.01:
            return p, True
        else:
            return p,  False

    @staticmethod
    def p_value(N, x_2):
        return gammaincc(float(N)/2, x_2/2)


#r = """1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"""

#print(Freq.test(r, 10, len(r)))
