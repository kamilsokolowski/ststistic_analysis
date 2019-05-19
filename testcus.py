from scipy.stats import norm
from math import sqrt


class CuSum:
    """
    A class thats implements Cumulative sums
    statistics test.
    ...
    Methods
    -------
    test(e, n, mode)
        Performes test with on parameters.
    """
    @staticmethod
    def test(e, n, mode):
        """
        Performes test with on parameters.

        All parameters are required

        Parameters
        ----------
        e : str,
            Bit sequence concidered in the test

        n : int
            Length of bit sequence

        mode : int
            Mode of summing operation.
        """
        X = []
        S_k = []

        for b in e:
            X.append(2 * int(b) - 1)

        if mode == 0:
            S_k.append(X[0])
            for k in range(1, n):
                S_k.append(S_k[k-1] + X[k])
        elif mode == 1:
            S_k.append(X[n - 1])
            for k in range(1, n):
                S_k.append(S_k[k - 1] + X[n - k - 1])

        z = CuSum.z_max(S_k)
        p = CuSum.p_value(n, z)
        if p < 0.01:
            return False
        else:
            return True

    @staticmethod
    def p_value(n, z):
        k = (-n//z + 1)//4
        end = (n//z - 1)//4
        sigma1 = 0.0
        sigma2 = 0.0
        while k <= end:
            sigma1 += (
                norm.cdf(((4*k + 1)*z)/sqrt(n)) -
                norm.cdf(((4*k - 1)*z)/sqrt(n))
            )
            k += 1
        k = (-n//z - 3)//4
        end = (n//z - 1)//4
        while k <= end:
            sigma2 += (
                norm.cdf(((4*k + 3)*z)/sqrt(n)) -
                norm.cdf(((4*k + 1)*z)/sqrt(n))
            )
            k += 1
        return (1 - sigma1 + sigma2)

    @staticmethod
    def z_max(s_k):
        t = list(map(abs, s_k))
        return max(t)
