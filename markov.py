"""Generate Markov text from text files."""

from random import choice

import sys

input_path = sys.argv[1]

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_name = open(file_path).read().split()
    #print(file_name)

    return file_name


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

    for i in range(len(text_string)-2):

        key_bigram = (text_string[i], text_string[i+1]) #Tuple
        next_word = text_string[i+2] #Word after the bi
        #print("chains:", chains)
        
        #Could refactor with get 
        if key_bigram not in chains: #Check if key is already in dictionary
            chains[key_bigram] = []
    
        chains[key_bigram].append(next_word) #For this key, append to list value
        #print("chains:", chains)
    
    for key, value in chains.items():     
        print(f"{key}, {value}")
        
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []
    
    #Choice works on lists, not dictionaries, so converted keys to a list
    initial_key = choice(list(chains.keys())) 
    #print("initial_bigram:", initial_bigram)
    words.extend([initial_key[0], initial_key[1]]) #extend takes >1 arg
    #print("words:", words)
    #print("chains:", chains)
    next_word = choice(chains[(words[0],words[1])])
    #print("next word:", next_word)
    words.append(next_word)
    #print("words:", words)
    
    for i, word in enumerate(chains): #Need index, so use enumerate
        try:
            next_key = (words[i+1],words[i+2])
            #print("next tuple:", next_tuple)
            next_word = choice(chains[next_key])
            #print("next_word:", next_word)
            words.append(next_word)

        except:
            print("")
            break

    #print("words:", words) #List of words built with Markov chains

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
