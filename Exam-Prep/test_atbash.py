from atbash import atbash_decrypt, atbash_encrypt, atbash_wrapper

def test_atbash_decrypt():

    assert callable(atbash_decrypt)
    assert isinstance(atbash_decrypt("HMVZPB KBGSLM HMZPV"), str)
    assert atbash_decrypt("HMVZPB KBGSLM HMZPV") == "SNEAKY PYTHON SNAKE"

def test_atbash_encrypt():
    
    assert callable(atbash_encrypt)
    assert isinstance(atbash_encrypt("VCZN"), str)
    assert atbash_decrypt("VCZN") == "EXAM"
    
    
def test_atbash_wrapper():
    
    assert callable(atbash_wrapper)
    assert atbash_wrapper("HMVZPB KBGSLM HMZPV", "decrypt") == "SNEAKY PYTHON SNAKE"
    assert atbash_wrapper("SNEAKY PYTHON SNAKE", "encrypt") == "HMVZPB KBGSLM HMZPV"
    
