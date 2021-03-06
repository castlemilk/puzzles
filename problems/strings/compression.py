def compress(text):
    """
    Compress a string by replacing repeating occurances with a numerical representation
    i.e
        aabccccccaaa -> a2b1c5a3

    if the resultant string is larger than the original then return the original
    :param text:
    :return:
    """
    repeat = 0
    new_string = ''
    for i in range(1, len(text)):
        if text[i - 1] == text[i]:
            repeat += 1
        else:
            repeat += 1
            new_string += text[i-1] + str(repeat)
            repeat = 0
        if i + 1 == len(text):
            repeat += 1
            new_string += text[i] + str(repeat)
    print(new_string)
    return new_string if len(new_string) < len(text) else text
