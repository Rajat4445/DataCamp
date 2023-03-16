'''
You are presented with one of the earliest known encryption techniques - Caesar cipher. It is based on a simple shift of each letter in a message by a certain number of positions down the given alphabet.
For example, given the English alphabet, a shift of 1 for 'xyz' would imply 'yza' and vice versa in case of decryption. Notice that 'z' becomes 'a' in this case.

Thus, encryption/decryption requires two arguments: text and an integer key denoting the shift (key = 1 for the example above).
Your task is to create an encryption function given the English alphabet stored in the alphabet string.'''

def encrypt(text, key):
  
    encrypted_text = ''

    # Fill in the blanks to create an encrypted text
    for char in text.lower():
        idx = (alphabet.index(char) + key) % len(alphabet)
        encrypted_text = encrypted_text + alphabet[idx]

    return encrypted_text

# Check the encryption function with the shift equals to 10
# print(encrypt("datacamp", 10))                              ( To check )
