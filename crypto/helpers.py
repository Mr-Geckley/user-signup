def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    output = alphabet.index(letter)
    
    return output

def rotate_character(char, rot):
    low_alpha = "abcdefghijklmnopqrstuvwxyz"
    up_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_position = 0
    
    if char.isalpha():
        new_position = (alphabet_position(char) + rot)
        if new_position > 25:
            new_position = new_position % 26
            
        if char.isupper():
            output = up_alpha[new_position]
        else: 
            output = low_alpha[new_position]
            
    else:
        output = char 
   
    return output