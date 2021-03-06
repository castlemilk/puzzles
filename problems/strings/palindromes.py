def palindrome(text):
    """
    Check to see if there is a palindrome within the permutations of each word in the sentence
    """
    chars = text.replace(' ', '').lower()
    print(chars)
    if (len(chars) - 1) % 2 != 0:
        return False
    return len(set(chars)) == ((len(chars) - 1) / 2 + 1)
