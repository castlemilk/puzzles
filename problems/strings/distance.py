def LD(s, t):
    """
    Determine whether string1 and string2 are within a given edit radius
    :param string1:
    :param string2:
    :return:
    """
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    return min(LD(s[:-1], t) +1,
              LD(s, t[:-1]) +1,
              LD(s[:-1], t[:-1]) + cost)



