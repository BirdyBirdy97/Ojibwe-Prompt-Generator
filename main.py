################################# Welcome to the Prompt Generator! ##########################################

### This can be used to practice conjugating verbs in various languages
### The original dictionary is for Nishnaabemowin/Ojibwe, but can be altered for other languages
### Please feel free to upload your own dictionary of tenses, pronouns, words, and any other info to begin

#############################################################################################################

import random
import lib

def lib_len(lib_type):
    num_of_words = len(lib[lib_type])
    return num_of_words

def num_generator(lib_len):
    choice = random.randint(0, lib_len)
    return choice

def get_selection(lib_type, rand_num):
    element = lib_type[rand_num]
    return element


print("Welcome! Please answer a few questions to begin.\n")
eng = input("Would you like to see the English Translation of words? (Yes/No\n").lower()


