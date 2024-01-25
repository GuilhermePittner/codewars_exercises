def solution(s):
    
    word = ''
    for c in s:
        
        if c.isupper():
            print(f'{c} é maiúsculo')
            word += f' {c}'
            
        else:
            print(f'{c} é minúsculo')
            word += c
        
    print(word)
    return word