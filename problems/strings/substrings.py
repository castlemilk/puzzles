def is_permutation(text1, text2):
    """
    Determines if text2 is a permutation (some differently ordered string) of text1
    Assumes we can use the sorted build-in method of python. Alternatively we'd implement the sort function
    ourselves.
    :param text1: input text
    :param text2: potential permutation
    :return:
    """
    return sorted(list(text1)) == sorted(list(text2))
