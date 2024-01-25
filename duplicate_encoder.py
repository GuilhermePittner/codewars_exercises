def duplicate_encode(word):
    
    final = ''
    word = word.lower()
    
    for x in word:
        
        total = word.count(x.lower())
        
        if total == 1:
            final += '('
        else:
            final += ')'
            
    print(final)
    return final
    
    
"""
def duplicate_encode(word):
    
    final = ''
    appeared = []
    
    for x in word:
        
        if not x.lower() in appeared:
            
            final += '('
            appeared.append(x.lower())
        else:
            final += ')'
            
    print(final)
"""