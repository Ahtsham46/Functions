def prnt_list(lisst,idx):
    if idx == len(lisst):
        return
    print(lisst[idx], end=" ")
    prnt_list(lisst,idx+1)






lisst = ['a','b','c','d','e','f']
prnt_list(lisst, 0)