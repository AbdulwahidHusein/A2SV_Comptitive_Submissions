def not_working(st, leng):
    not_w = {}
    for w in st:
        not_w[w] = False
    i = 0  
    while i <len(st)-1:
        if st[i] == st[i+1]:
            not_w[st[i]] = True
            i += 2
        else:
            not_w[st[i]] = False
            i += 1

    
    if st[leng-1]!=st[leng-2]:
        not_w [st[-1]] == False
        print(not_w[st[leng-1]])
        
    ss = ""        
    for l in not_w:
        if not not_w[l]:
            ss += l
            
    return ""

print(not_working("zzaaz", 5))
            
    
    