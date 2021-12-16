"""
Word Occurences
Count the number of same words in a sentence
Created on 16-12-2021 by Richard Reynard
"""

word_to_count = {}
text = input("Text: ")
words = text.split()
for word in words:
    word_count = word_to_count.get(word, 0)
    word_to_count[word] = word_count + 1


