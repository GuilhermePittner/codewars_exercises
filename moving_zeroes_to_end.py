def move_zeros(lst):
    
    cont = 0
    
    while 0 in lst:
        lst.remove(0)
        cont+=1
        
    for y in range(cont):
        lst.append(0)
    
    return lst


"""
def move_zeros(lst):
    
    cont = 0
    
    for id, x in enumerate(lst):

        if x == 0:
            cont += 1
    
    while 0 in lst:
        lst.remove(0)
        
    for y in range(cont):
        lst.append(0)
    
    return lst
"""