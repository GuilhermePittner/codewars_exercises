def spin_words(sentence):
    
    tratar = sentence.split(' ')
    final_string = ''
    
    for w in tratar:
            
        if len(w) >= 5:
            print('needs spinning')
            
            final_string += f'{w[::-1]},'
            
        else:
            print('do not spin')
            
            final_string += f'{w},'
    
    final_string = final_string.replace(',', ' ')
    print(final_string)
    return final_string[:-1]