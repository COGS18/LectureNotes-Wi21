def atbash_decrypt(crypto):     
    """Decrypt Message using atbash method, returning reverse alphabetical position. 
    
    Parameters
    ----------
    crypto : string
        The string to be decrypted.
    
    Returns
    -------
    message : string
        The atbash decrypted message. 
    """
    
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    message = ''
    crypto = crypto.upper()
   
    for char in crypto:
        # if char in crypto is found, 
        # return indexed letters from reverse alpha
        if char in reverse_alpha:
            letter_index = reverse_alpha.find(char)
            message = message + alpha[letter_index]
        else: message = message + char
        
    return message


def atbash_encrypt(input_string):
    """Reverse alphabetical position of letters within a string. 
    
    Parameters
    ----------
    input_string : string
        string to be encrypthed
        
    Returns
    -------
    answer : string
        The encrypted string, storing the reverse alphabetical position of input string. 
    """
   
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alpha = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    output_string = ''
    
    for char in input_string:
        char = char.upper()  # covert to upper case
    
        if char.isalpha():
            index = alpha.index(char)  # get position
            output_string += reverse_alpha[index]
        else:
            output_string += char
        
    return output_string


        
def atbash_wrapper(input_string, method):
    """Reverse alphabetical position of letters within a string. 
    
    Parameters
    ----------
    input_string : string
        string to be encrypted or decrypted
    method: string
        The method to use ("encrypt" or "decrypt")
        
    Returns
    -------
    ouput : string
        The string, either encrypted or decrypted as indicated by method. 
    """
           
    if method == 'encrypt':
        output = atbash_encrypt(input_string)
    elif method == 'decrypt':
        output = atbash_decrypt(input_string)
    else:
        output = "Expecting method to be either 'encrypt' or 'decrypt'"
    
    return output
   