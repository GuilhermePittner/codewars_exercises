def is_pangram(s):
    
    alphabet = 'abcdefghijklmnopqrstuvxyz'
    
    for x in s:
        
        if x.lower() in alphabet:
            
            print(f'{x} está no beto')
            alphabet = alphabet.replace(x.lower(), '-')
    
    if alphabet == '-------------------------':
        return True
    
    return False