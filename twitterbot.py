import sys
sys.path.append(r'/Users/alex/Documents/Coding_Projects/twitterbot')
import random
from genesiswords import genesis_words
from nltk.tokenize import sent_tokenize

def get_quote(words):

    sents = sent_tokenize(words)
    rand_index = random.randint(0,len(sents) - 1)
    curr_quote = sents[rand_index] + sents[rand_index+1]

    return curr_quote + "\n Brought to you by Genesis_Bot : Praise Be!"

print(get_quote(genesis_words))

if __name__ == "__main__":
    get_quote(genesis_words)