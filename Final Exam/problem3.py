def f(a,b):
    return a>b
    
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    d1keys = d1.keys()
    d2keys = d2.keys()
    same = []
    different = {}
    for i in d1keys:
        if i in d2keys:
            same.append(i)
        else:
            different[i] = d1[i]
    for j in d2keys:
        if j not in d1keys:
            different[j] = d2[j]
        else:
            pass
    
    intersect = {}
    for i in same:
        intersect[i] = f(d1[i], d2[i])
    
    return (intersect, different)


d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print dict_interdiff(d1, d2)