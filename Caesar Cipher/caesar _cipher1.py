alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#encryption
def encrypt(original_text,shift_amount):
  cipher_text =""
  for letters in original_text:
    shifted_position = alphabet.index(letters)+shift_amount
    #to iterate to the begining if we try to shift after "z"
    shifted_position = shifted_position % len(alphabet)
    cipher_text += alphabet[shifted_position]
  print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        #to iterate to the begining if we try to shift before "a"
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")
  
