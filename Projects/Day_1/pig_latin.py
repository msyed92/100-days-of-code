##Translate a word to pig latin
import string
import re

cons = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'
numbers = '1234567890'

def pig_latin(word):

    word = word.lower()
    
    if ((word[0] in cons) and (word[1] in cons)):
        if len(word) > 2:
            return word[2:]+word[0]+word[1]+'ay'
        else:
            return word[1]+word[0]+'ay'
    
    elif word[0] in vowels:
        return word+'yay'
    
    elif ((word[0] in cons) and (word[1] in vowels)):
        return word[1:]+word[0]+'ay'
    
    else:
        'ERROR'

#Translate a long string of words to pig latin
from nltk.tokenize import TweetTokenizer
tokenizer = TweetTokenizer()

def pig_latin_text(text):
    words = tokenizer.tokenize(text)
    pig_words = []
    
    for i in range(0, len(words)):
        if words[i] in string.punctuation or any(n in words[i] for n in numbers):
            pig_words.append(words[i])
        else:
            pig_words.append(pig_latin(words[i]))
    
    pig_string = ''
    for i in range(0,len(pig_words)):
        if pig_words[i] in string.punctuation:
            pig_string += pig_words[i]+' '
        elif (pig_words[i] not in string.punctuation and pig_words[i+1] in string.punctuation) or i == 0 or i == len(pig_words):
            pig_string += pig_words[i]
        else:
            pig_string += ' '+pig_words[i]
    return pig_string
