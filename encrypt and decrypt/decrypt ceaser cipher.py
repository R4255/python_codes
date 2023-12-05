#facing error in this code
def decrypt():
    
    #enter your encrypted message(string) below
    encrypted_message = input("Enter the message i.e to be decrypted: ")
    
    letters="abcdefghijklmnopqrstuvwxyz"
    chars1=letters.upper()
    #enter the key value to decrypt
    k = int(input("Enter the key to decrypt: "))
    decrypted_message = ""

    for ch in encrypted_message:

        if ch in letters :
            position = letters.find(ch)
            new_pos = (position - k) % 26
            new_char = letters[new_pos]
            decrypted_message += new_char
        elif ch in chars1:
            position = chars1.find(ch)
            new_pos = (position - k) % 26
            new_char = chars1[new_pos]
            decrypted_message += new_char
        else:
            decrypted_message += ch
    print("Your decrypted message is:\n")
    print(decrypted_message)
decrypt()
