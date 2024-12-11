the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here
def rephrase_boolean(bool):
    if bool == 1:
        return 'wiki'
    elif bool == 0:
        return 'woko'
    else:
        return 'error'
    
result = list(map(rephrase_boolean,the_bools))
print(result)