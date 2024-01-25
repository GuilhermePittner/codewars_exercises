# i couldn't optimize the code, so i asked GPT to do it.


def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    
    max_divisor = int(num**0.5) + 1
    
    for x in range(3, max_divisor, 2):
        if num % x == 0:
            return False
    
    return True



"""
def is_prime(num):
    
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
        
    else:
        
        for x in range(3, round(num/2), 2):
            
            if num%x == 0:
                return False
    
    return True
"""