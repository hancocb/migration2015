def list2dict(mylist):
    ret = {}
    i = 0
    for ele in mylist:
        ret[i] = ele
        i = i+1
    return ret