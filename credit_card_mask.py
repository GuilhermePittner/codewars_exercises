# return masked string
def maskify(cc):
    
    secret = ''
    total = len(cc)
    
    for x in cc:
        
        if total <= 4:
            secret += x
        
        else:
            secret += '#'
   
        total -= 1
    
    return secret
