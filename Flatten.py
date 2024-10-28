def flatten(input_list):
    res = []
    stk = [input_list]
    while stk:
        current = stk.pop(-1)
        if isinstance(current, list):
            stk.extend(current)
        else:
            res.append(current)
    res.reverse()
    return res