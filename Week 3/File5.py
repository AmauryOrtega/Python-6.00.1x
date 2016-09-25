# -*- coding: utf-8 -*-
"""
Created on 25/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

'''
Things that can be done to strings, range, list or tuple
being seq the name of any of the above variable
-----OPERATIONS-----
seq[i]
len(seq)
seq1 + seq2 (not range)
n*seq (not range)
seq[start:end]
e in seq
e not in seq
for e in seq

-----PROPERTIES-----
-----   type    mutable
str     char    not mutable
tuple   any     not mutable
range   int     not mutable
list    any     yes mutable
'''

# Dictionaries
'''
-----PROPERTIES-----
Value
    any type (mutable and not mutable)
Key
    unique
    not mutable type (int, float, string, tuple, bool)
        really it needs and hashable type, all immutable types are hashable
'''
grades = {'Ana': 'B', 'John': 'A+', 'Denise': 'A', 'Katy': 'A'}
grades['John']
grades['Sylvan'] = 'A'
'John' in grades
del (grades['Ana'])
grades.keys()
grades.values()

d = {4: {1: 0}, (1, 3): "twelve", 'const': [3.14, 2.7, 8.44]}


# Analyze song lyrics
def lyrics_to_frecuencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

                 'you', 'think', "you've", 'lost', 'your', 'love',
                 'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
                 "it's", 'you', "she's", 'thinking', 'of',
                 'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

                 'she', 'says', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'she', 'said', 'you', 'hurt', 'her', 'so',
                 'she', 'almost', 'lost', 'her', 'mind',
                 'and', 'now', 'she', 'says', 'she', 'knows',
                 "you're", 'not', 'the', 'hurting', 'kind',

                 'she', 'says', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',

                 'you', 'know', "it's", 'up', 'to', 'you',
                 'i', 'think', "it's", 'only', 'fair',
                 'pride', 'can', 'hurt', 'you', 'too',
                 'pologize', 'to', 'her',

                 'Because', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'Yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'yeah', 'yeah', 'yeah',
                 'yeah', 'yeah', 'yeah', 'yeah'
                 ]

beatles = lyrics_to_frecuencies(she_loves_you)


def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


(w, b) = most_common_words(beatles)


def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del (freqs[w])
        else:
            done = True
    return result


print(words_often(beatles, 5))
