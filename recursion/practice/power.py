def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    return fast_pow(x,n)

def fast_pow(x,n):
    if n < 0:
        return fast_pow(1/x,-n)
    elif n == 0:
        return 1.0
    elif n == 1:
        return x
    elif n % 2 == 0:
        return fast_pow(x*x,n/2)
    else:
        return fast_pow(x*x,n/2)*x
