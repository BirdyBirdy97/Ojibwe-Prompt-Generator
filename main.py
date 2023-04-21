################################# Welcome to the Prompt Generator! ##########################################

### This can be used to practice conjugating verbs in various languages
### The original dictionary is for Nishnaabemowin/Ojibwe, but can be altered for other languages
### Please feel free to upload your own dictionary of tenses, pronouns, words, and any other info to begin

#############################################################################################################

import random
import lib

QUESTIONS = []

def lib_len(lib_type):
    num_of_elements = len(lib_type)
    return num_of_elements

def num_generator(lib_len):
    choice = random.randint(0, lib_len - 1)
    return choice

def get_selection(lib_type, rand_num):
    element = lib_type[rand_num]
    return element

count = 0

while count < 20:
    count += 1
    num_in_lib = lib_len(lib.word_bank_nish)
    rand_num = int(num_generator(num_in_lib)) 

    nish_word = lib.word_bank_nish[rand_num]
    eng_word = lib.word_bank_eng[rand_num]

    tense_num = random.randint(0, len(lib.tense) - 1)
    pronoun_num = random.randint(0, len(lib.pronouns) - 1)
    tense_choice = lib.tense[tense_num]
    pronoun_choice = lib.pronouns[pronoun_num]

    print(f"{pronoun_choice} {tense_choice} {nish_word} ({eng_word})")



# print("Welcome! Please answer a few questions to begin.\n")
# trans = input("Would you like to see the Translation of the words? (Yes/No)\n").lower()
# test_length = int(input("How many selections would you like? Please provide an integer."))

# while not type(test_length) == int:
#     int(input("I didn't catch that, how many selections would you like? Please provide a number."))

# while len(QUESTIONS) < test_length:
#     new_q = get_selection(lib.word_bank_nish, num_generator)
#     QUESTIONS.append(new_q)

# print([QUESTIONS])