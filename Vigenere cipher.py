import string
alphabets = string.ascii_lowercase      # assigns alphabets


def encode():
    word = input('Enter word/sentence here: ').lower()  # retrieves word/sentence
    key = input('Provide keyword or phrase: ').lower()  # retrieves keyword/phrase
    key_storage = []  # stores repeat of keyword/phrase as it matches word from user
    position = []
    position_key = []
    encrypted_word = []  # stores final result

    # Handle key sequence counting only letters
    key_count = 0
    for char in word:
        if char.isalpha():
            key_storage.append(key[key_count % len(key)])
            key_count += 1
        else:
            key_storage.append(char)

    # Get positions, preserving punctuation
    for char in word:
        if char.isalpha():
            position.append(alphabets.index(char))
        else:
            position.append(char)

    #for char_1 in key_storage:              # stores position of each letter in key_storage
        #position_key.append(alphabets.index(char_1))

        # Get key positions, preserving punctuation
    for char in key_storage:
        if char.isalpha():
            position_key.append(alphabets.index(char))
        else:
            position_key.append(char)

        # Encrypt only letters
    for i in range(len(word)):
        if word[i].isalpha():
            new_pos = (position[i] + position_key[i]) % 26
            encrypted_word.append(alphabets[new_pos])
        else:
            encrypted_word.append(word[i])

    return ''.join(encrypted_word)


def decode():
    change = input('Enter word/sentence here: ').lower()  # retrieves word/sentence
    key_1 = input('Provide keyword or phrase: ').lower()  # retrieves keyword/phrase
    key_storage = []  # stores repeat of keyword/phrase as it matches word from user
    position = []
    position_key = []
    decrypted_word = []  # stores final result


    # Handle key sequence counting only letters
    key_count = 0
    for char in change:
        if char.isalpha():
            key_storage.append(key_1[key_count % len(key_1)])
            key_count += 1
        else:
            key_storage.append(char)

    # Get positions, preserving punctuation
    for char in change:
        if char.isalpha():
            position.append(alphabets.index(char))
        else:
            position.append(char)

    # Get key positions, preserving punctuation
    for char in key_storage:
        if char.isalpha():
            position_key.append(alphabets.index(char))
        else:
            position_key.append(char)

    # Decrypt only letters
    for i in range(len(change)):
        if isinstance(position[i], int) and isinstance(position_key[i], int):  # ensures that mathematical operations are performed on integers
            new_pos = (position[i] - position_key[i]) % 26  # subtraction for decoding
            decrypted_word.append(alphabets[new_pos])
        else:
            decrypted_word.append(change[i])

    return ''.join(decrypted_word)


# WELCOME MESSAGE
print('***WELCOME TO THE VIGENERE CIPHER PROGRAM***')
while True:
    user_choice = input('\nSELECT OPTION\n1 -> ENCODE(Press E)\n2 -> DECODE(Press D)\n3 -> QUIT PROGRAM(Press Q)\n').lower()
    if user_choice == 'e':
        print(f'Encrypted: "{encode()}"')
    elif user_choice == 'd':
        print(f'Decrypted: "{decode()}"')
    elif user_choice == 'q':
        break
    else:
        print('enter a valid option')
print('Thanks for ciphering!\nSee you next time.')




