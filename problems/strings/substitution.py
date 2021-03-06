def substitute(text, match, replace_string):
    """
    Replace all occurances of the matching pattern with the replacement string
    :param replace_string:
    :param text1: input text
    :param text2: potential permutation
    :return:
    """
    return ''.join(replace_string if c == match else c for c in text)
