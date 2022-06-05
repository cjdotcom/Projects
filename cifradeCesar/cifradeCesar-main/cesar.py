def cifrar(palavra, key):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if key == '':
        key = 0
        
    cipher_text = ''
    for ch in palavra:
        if ch in alfabeto:
            idx = alfabeto.find(ch) + key
            if idx >= 26:
                idx -= 26
            cipher_text += alfabeto[idx]

    return cipher_text

def decifrar(palavra, key):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if key == '':
        key = 0

    cipher_text = ''
    for ch in palavra:
        if ch in alfabeto:
            idx = alfabeto.find(ch) - key
            cipher_text += alfabeto[idx]
            
    return cipher_text