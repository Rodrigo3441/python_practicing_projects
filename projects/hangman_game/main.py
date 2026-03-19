import console_treat as console
import file_handling as file

secret_word = file.choose_random_word()
secret_word_blank = '_' * len(secret_word)
life_position = 0
used_letters = ''
user_letter = ''
life_image = ['  _______\n |/      |\n |\n |\n |\n |\n |\n_|___\n',
               '  _______\n |/      |\n |      (_)\n |\n |\n |\n |\n_|___\n',
               '  _______\n |/      |\n |      (_)\n |      \ /\n |\n |\n |\n_|___\n',
               '  _______\n |/      |\n |      (_)\n |      \ /\n |       |\n |\n |\n_|___\n',
               '  _______\n |/      |\n |      (_)\n |      \ /\n |       |\n |      /\n |\n_|___\n',
               '  _______\n |/      |\n |      (_)\n |      \ /\n |       |\n |      / \\\n |\n_|___\n\n Game over!',
            ]

def update_used_letters() -> str:
    return used_letters + user_letter

def print_used_letters():
    # just start printing used letters after getting at least one letter on the string
    if used_letters != '':
        print(f'\nUsed letters: \n{used_letters}')

def letter_enter_point() -> str:
    while True:
        letter = input('\nWhat letter you choose?\n').strip().lower()

        if not letter.isalpha() or len(letter) > 1:
            console.clear()
            print('Enter only one letter.')
        
        elif letter in used_letters:
            console.clear()
            print('You already have used this letter, Choose another one.')
            print_used_letters()
        else:
            return letter


# main game part
while True:
    console.clear()
    # game title
    print('/****************/\n/    Hangman    */\n/****************/')
    print(life_image[life_position])

    # win case
    if secret_word == secret_word_blank:
        print(secret_word)

        print('\nYou win!')
        print('Now you can choose a new word to add on database:')
        file.add_new_word()
        break

    # game over break point
    if life_position == 5:
        break

    print(secret_word_blank)

    print_used_letters()

    # section for user enter a letter
    user_letter = letter_enter_point()

    # counter for the loop go through all positions of the string
    str_position = 0

    # boolean var to store if at least one letter was found
    position_found = False
    while True:
        position_letter = secret_word.find(user_letter, str_position)

        if position_letter != -1:
            # replace letters blanks with the correct letter
            secret_word_blank = secret_word_blank[:position_letter] + user_letter + secret_word_blank[position_letter+1:]

            position_found = True
            str_position += 1

        elif position_found is True:
            print('Success! Now enter another letter')
            used_letters = update_used_letters()
            console.pause()
            break

        else:
            life_position += 1
            print('too bad! try another letter')
            used_letters = update_used_letters()
            console.pause()
            break