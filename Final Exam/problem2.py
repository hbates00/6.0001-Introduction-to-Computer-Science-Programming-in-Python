def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    newdict = {}
    
    for i in d:
        if d[i] not in newdict:
            newdict[d[i]] = [i]
        elif d[i] in newdict:
            item = newdict[d[i]]
            item.append(i)
            item.sort()
            newdict[d[i]] = item
        else:
            pass
    
    return newdict
    
d = {4:True, 2:True, 0:True}
print dict_invert(d)
        