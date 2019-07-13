def equalsWhenOneCharRemoved(x, y):
    if abs(len(x) - len(y)) != 1:
        return False

    length = len(y)
    target = y
    source = x
    if len(x) > len(y):
        length = len(x)
        target = x
        source = y

    i = j = 0
    valid = 0
    while (j < length - 1):
        if target[i] != source[j]:
            valid += 1
            if valid > 1:
                return False
            i += 1
        else:
            i += 1
            j += 1
    return True
