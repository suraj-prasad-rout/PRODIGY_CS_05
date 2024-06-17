import string
alphabet_list = list(string.ascii_lowercase)


def encrypt_decrypt(plain_text, shift_key, mode):
    result_text = ""
    for char in plain_text:
        if char in alphabet_list:
            postion = alphabet_list.index(char)
            if mode == "encrypt":
                new_postion = (postion+shift_key) % 26
            elif mode == "decrypt":
                new_postion = (postion-shift_key) % 26
            result_text += alphabet_list[new_postion]
        else:
            result_text += char
    return result_text


wana_do = True
while wana_do:
    what_to_do = input(
        "Type 'encrypt' for encryption, type 'decrypt' for decryption:\n").lower()

    if what_to_do == "encrypt" or what_to_do == "decrypt":
        text = input("Enter your text:\n").lower()
        shift = int(input("Enter shift key:\n"))

        if what_to_do == "encrypt":
            encrypted_text = encrypt_decrypt(text, shift, mode='encrypt')
            print(f"Encrypted text: {encrypted_text}")

        elif what_to_do == "decrypt":
            decrypted_text = encrypt_decrypt(text, shift, mode='decrypt')
            print(f"Decrypted text: {decrypted_text}")

    else:
        print("Invalid input")

    play_it_again = input(
        "Type 'yes' to go again. Otherwise type 'no':\n").lower()
    if play_it_again != "yes":
        wana_do = False
