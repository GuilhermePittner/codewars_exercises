def create_phone_number(n):
    
    my_phone_number = '('
    
    for id_x, x in enumerate(n):
        
        if id_x <= 2:
            my_phone_number += str(x)
            
            if id_x == 2:
                my_phone_number += ') '
                
        elif id_x >= 3 and id_x <= 5:
            my_phone_number += str(x)
            
            if id_x == 5:
                my_phone_number += '-'
                
        else:
            my_phone_number += str(x)
                
    print(my_phone_number)
    return my_phone_number
   