def is_isogram(str):
    for i in str:
        if str.count(i) > 1:
            return false

    return true
