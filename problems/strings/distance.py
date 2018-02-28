def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)

    helper.calls = 0
    helper.__name__ = func.__name__
    return helper


def memoize(func):
    mem = {}

    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]

    return memoizer


@memoize
@call_counter
def LD(s, t):
    """
    Determine the Levenshtein distance using a recursive function
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

    return min(LD(s[:-1], t) + 1,
               LD(s, t[:-1]) + 1,
               LD(s[:-1], t[:-1]) + cost)


def VLD(s, t):
    """
    Determine the Levenshtein distance using a vectorised function
    iterative_levenshtein(s, t) -> ldist
    ldist is the Levenshtein distance between the strings
    s and t.
    For all i and j, dist[i,j] will contain the Levenshtein
    distance between the first i characters of s and the
    first j characters of t
    :param s:
    :param t:
    :return:
    """
    rows = len(s) + 1
    cols = len(t) + 1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    for i in range(1, rows):
        dist[i][0] = i
    for j in range(1, cols):
        dist[0][j] = j
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] +1,
                                 dist[row][col-1]+1,
                                 dist[row-1][col-1] + cost
                                 )
    for r in range(rows):
        print(dist[r])

    return dist[row][col]
