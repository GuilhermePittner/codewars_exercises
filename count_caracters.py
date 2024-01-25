def count(s):
    
    res = {}
    
    if len(s) == 0:
        return res
    
    else:
        
        for w in s:
            
            l_count = s.count(w)
            #print(f'{w} aparece em {s} {l_count} vezes')
            res[w] = l_count
            
        return res