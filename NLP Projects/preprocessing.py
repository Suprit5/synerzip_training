import nltk
import string
import numpy as np
stemmer=nltk.PorterStemmer()

def tokenize(sentence):
    no_punc=''.join([char for char in sentence if char not in string.punctuation])
    return nltk.word_tokenize(no_punc)

def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    tokenized_sentence=[stem(w) for w in tokenized_sentence]
    bow=np.zeros(len(all_words),dtype=np.float32)
    for idx,w in enumerate(all_words):
        # print(idx,w)
        # print(tokenized_sentence)
        if w in tokenized_sentence:
            bow[idx]=1.0

    return bow

# sentence=['hi','how','are','you']
# words=['hi','hello','I','you','bye','thank','cool']
# print(bag_of_words(sentence,words))