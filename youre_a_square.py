from math import sqrt

def is_square(n):    
    
    if n == 0:
        return True
    
    elif n < 0:
        return False
    
    else:
        n_math = n ** 0.5
        
        if int(n_math*n_math) == n:
            return True
        else:
            return False