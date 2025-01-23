# Importing required libraries and functions
import json
import nltk

# Following code required only to be executed only once
# Use if ssl error occours during nltk download
import ssl
try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
   pass
else:
   ssl._create_default_https_context = _create_unverified_https_context
# Downloading aditional nltk data
nltk.download('punkt')
nltk.download('wordnet')


print("System start initiated.")
print("Loading JSON data.")

# Loading json data file into memory 
with open('data/data.json') as file:
    data = json.load(file)

words = []
classes = []
data_x = []
data_y = []


# Tokenizing and appending json data
for intent in data['intents']:
    for utterance in intent['utterances']:
        tokens = nltk.word_tokenize(utterance)
        words.extend(tokens)
        data_x.append(utterance)
        data_y.append(intent['tag'])

    if intent['tag'] not in classes:
        classes.append(intent['tag'])

words = sorted(set(words))
classes = sorted(set(classes))
