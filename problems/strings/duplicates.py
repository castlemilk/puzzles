def duplicates1(text):
    """
    Will evaluate a string for the uniqueness of all characters
    :param text:
    :return:
    """
    return len(text) == len(set(text))
