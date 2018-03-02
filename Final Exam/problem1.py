def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flattened = []
    contains_lists = False
    for i in xrange(len(aList)):
        if type(aList[i]) == list:
            contains_lists = True
        else:
            pass
    if contains_lists == False:
        return aList
    else:
        for i in xrange(len(aList)):
            if type(aList[i]) == list:
                newlist = flatten(aList[i])
                for j in xrange(len(newlist)):
                    flattened.append(newlist[j])
            else:
                flattened.append(aList[i])
        return flattened


aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print flatten(aList)
        