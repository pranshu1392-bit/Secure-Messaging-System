def check_word(check):
    
    if not check :        # if variable is empty 
        raise ValueError ("Message can't not be empty")       # error will be raised
        return check         # returns to the same step again for correct input

def check_b(check2):
    
    if check2 != "code" and check2 != "decode":        # if input is neither "code" nor "decode"
        raise ValueError("Input must be in code or decode only")       # error will be raised
        return check2        # returns to the same step again for correct input
 