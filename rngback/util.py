def clamp(n, nmin, nmax):
    '''
    Clamps a number so that it is within the specified range.

    Args:
        n: A number.
        nmin: The bottom of the range.
        nmax: The top of the range.

    Returns:
        The clamped value of n. It is guaranteed to be within nmin and nmax.
    '''

    if n < nmin:
        return nmin
    elif n > nmax:
        return nmax
    else:
        return n
