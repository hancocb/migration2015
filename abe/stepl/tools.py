def list2dict(mylist):
    ret = {}
    i = 0
    for ele in mylist:
        ret[i] = ele
        i = i+1
    return ret

def list2dictWthKey(key,mylist):
    ret = {}
    for ele in mylist:
        ret[ele[key]] = ele
    return ret

def extract(instance):
    ret = {}
    for fd in instance._meta.get_all_field_names():
        ret[fd] = getattr(instance,fd)
    return ret