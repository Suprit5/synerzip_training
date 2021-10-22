import json
from preprocessing import stem, tokenize, bag_of_words
import numpy as np
with open('NLP Projects\intents.json','r') as f:
    intents=json.load(f)

all_words = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        words = tokenize(pattern)
        all_words.extend(words)
        xy.append((words,tag))
    
all_words=[stem(words) for words in all_words]

all_words=sorted(set(all_words))
#print(all_words)

tags=sorted(set(tags))
# print(tags)
#print(xy)

x_train=[]
y_train=[]

for (pattern_sentence,tag) in xy:
    bow=bag_of_words(pattern_sentence, all_words)
    x_train.append(bow)

    label=tags.index(tag)
    y_train.append(label)

print(x_train)
print('--------------------------------------------------------------------------------------------')

print(y_train)

x_train = np.array(x_train)
y_train = np.array(y_train)
print('--------------------------------------------------------------------------------------------')
print(x_train)
print('--------------------------------------------------------------------------------------------')

print(y_train)