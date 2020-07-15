"""Generate Markov text from text files."""

from random import choice

import sys

input_path = sys.argv[1]

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_name = open(file_path)
    text_in_file = file_name.read().split()
    #print(file_name)
    file_name.close()

    return text_in_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    text_string.append(None)

    for i in range(len(text_string)-2):

        key_n_gram = (text_string[i], text_string[i+1]) #Tuple
        next_word = text_string[i+2] #Word after the bi
        #print("chains:", chains)
        
        #Could refactor with get 
        if key_n_gram not in chains: #Check if key is already in dictionary
            chains[key_n_gram] = []
    
        chains[key_n_gram].append(next_word) #For this key, append to list value
        #print("chains:", chains)
    
    #for key, value in chains.items():     
    #    print(f"{key}, {value}")
        
    return chains


def make_text(chains):
    """Return text from chains."""  
    
    #Choice works on lists, not dictionaries, so converted keys to a list
    key = choice(list(chains.keys())) 
    #print("initial key:", key)
    #words.extend([initial_key[0], initial_key[1]]) #extend takes >1 arg
    words = [key[0], key[1]]
    #print("words:", words)
    #print("chains:", chains)
    next_word = choice(chains[key])
    #print("next word:", next_word)
    words.append(next_word)
    #print("words:", words)
    
    while next_word is not None: #Unknown length of loop
        key = (key[1],next_word) #Second word in key tuple and random list value 
        #print("next key:", key)
        words.append(next_word)
        #print("words:", words)
        next_word = choice(chains[key])
        #print("next_word:", next_word)
        

    #print("words:", words) #List of words built with Markov chains

    return " ".join(words)


#input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
