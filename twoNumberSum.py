def perm(lst):
    if len(lst)==0:
        return []
    elif len(lst)==1:
        return lst
    else:
        l=[]
        for i,val in enumerate(lst):
            xs=lst[:i]+lst[i+1:]


lst=[1,2,3]
for i,val in enumerate(lst):
    print(lst[:i]+lst[i+1:])
