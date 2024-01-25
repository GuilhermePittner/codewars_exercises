def friend(x):
    
    my_friends = []
    
    for name in x:
        
        if len(name) == 4:
            my_friends.append(name)
    
    return my_friends