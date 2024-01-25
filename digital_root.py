def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

"""
def digital_root(n):
    
    iterar = str(n)
    for_iterar = 0
    
    while len(iterar) >= 2:
        
        #print(f'entrando no for com iterar {iterar}')
        for x in iterar:
            for_iterar += int(x)
            #print(f'montando meu for_iterar {for_iterar}')
            
        iterar = str(for_iterar)
        
    #print(f'cabou a vida {iterar}')
    return int(iterar)
"""