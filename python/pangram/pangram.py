def is_pangram(str):
    for i in xrange(97,123):
        if chr(i) not in str.lower():
            return False

    return True

