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
    :type t: target string
    :type s: source string
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

    return min(LD(s[:-1], t) + 1,  # Remove
               LD(s, t[:-1]) + 1,  # Insert
               LD(s[:-1], t[:-1]) + cost)  # Replace


def VLD(s, t):
    """
    This is considered a dynamic programming based solution as we are effectively memoizing the previous
    results in the matrix and uses these to avoid re-calculating known results repeatedly.
    Time complexity = O(len(s) x len(t))
    Auxiliary Space = O(len(s) x len(t))
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
            if s[row - 1] == t[col - 1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row - 1][col] + 1,  # Insert
                                 dist[row][col - 1] + 1,  # Remove
                                 dist[row - 1][col - 1] + cost  # Replace
                                 )
    for r in range(rows):
        print(dist[r])

    return dist[row][col]


def distance_one(s, t):
    """
    Determine whether the distance between string s and string t is one
    1. If the length difference between s and t is greater than 1 then we can return false
    2. initialise the counts of edits as 0
    3. Start traversing both strings from first character
        a. if current characters dont match then:
            i. increment count of edits
            ii. if count exceeds 1 then return false
            iii. if length of one string is larger then we move ahead using the larger of the two
            iv. if length is the same, then only possible edit is to change a character, then we move ahead
                in both strings
        b. else move ahead in both strings
    :param s:
    :param t:
    :return:
    """
    m = len(s)
    n = len(t)
    if abs(m - n) > 1:
        return False

    count = 0  # initial count of edits
    i = 0
    j = 0

    while i < m and j < n:
        # if current characters dont match
        if s[i] != t[j]:
            if count == 1:
                # we are already at 1 edit required
                return False
            if m > n:
                # s is larger than t so we move ahead in s
                i += 1
            elif n > m:
                # t is larger than s so we move ahead in t
                j += 1
            else:
                # both ahead in both as they are equal length
                i += 1
                j += 1
            count += 1

        else:
            # move ahead in both strings
            i += 1
            j += 1

    if i < m or j < n:
        count += 1

    return count == 1
