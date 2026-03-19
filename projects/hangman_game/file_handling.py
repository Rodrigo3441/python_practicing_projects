import random
import console_treat as console
import csv
import os

#csv file name
csvfile = 'words.csv'

def retrieve_file_words() -> list:
    #array to store all words from file
    words = []

    if not os.path.exists(csvfile):
        with open(csvfile, 'w', newline='') as file:
            file.write('word\n')

    # open the file and jump the first line that is a header
    with open(csvfile, 'r') as file:
        next(file)
        #for every word inside the csv file, it will be appended on words array
        for word in file:
            words.append(word.strip())
        
    #function will return one random word between every all words from the file
    return words

def add_new_word():
    registered_words = retrieve_file_words()
    while True:
        word = input('\nEnter the new word: ').strip().lower()

        if not word.isalpha():
            console.clear()
            print('Use only letters for the new word.')

        elif len(word) < 3:
            console.clear()
            print('Enter a word with at least three letters.')

        elif word in registered_words:
            console.clear()
            print('This word is already registered, please choose another one.')

        else:
            with open(csvfile, 'a', newline='') as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow([word])
            print('New word registered successfully')
            break

def choose_random_word() -> str:
    words = retrieve_file_words()

    if (words == []):
        print('There are no registered words. Please add a new word to play the game.')
        add_new_word()
        words = retrieve_file_words()

    return random.choice(words)